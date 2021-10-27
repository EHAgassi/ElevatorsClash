package ex0.algo;

import ex0.Building;
import ex0.CallForElevator;
import ex0.Elevator;

public class myElev implements ElevatorAlgo {
    public static final int UP = 1, DOWN = -1;
    private int _direction;
    private Building _building;
    private mission_Table MT;
    private Integer[] finalDest;


    public myElev(Building building) {
        this._building = building;
        this.finalDest = new Integer[building.numberOfElevetors()];
        this.MT = new mission_Table(building.numberOfElevetors());
    }


    @Override
    public Building getBuilding() {
        return this._building;
    }

    public String algoName() {
        return "Our Online Elev Algorithm";
    }

    private double CalculateTime(Elevator elv, CallForElevator x) {

        double ans = 0;
        int existedCalls = 1;
        double floorTime = (elv.getStartTime() + elv.getStopTime()+elv.getTimeForOpen()+elv.getTimeForClose());

        if (MT.table[elv.getID()] != null && MT.table[elv.getID()].size() > 0) {
            existedCalls = MT.table[elv.getID()].size()+1;
        }

        ans += (floorTime * existedCalls);///
        ans += Math.abs(elv.getPos() - x.getSrc()) / elv.getSpeed();
        ans += Math.abs(x.getDest() - x.getSrc()) / elv.getSpeed();
        if (elv.getPos() == x.getSrc()) {
            ans -= (elv.getStartTime() + elv.getStopTime());
        }
        return ans;
    }

    private boolean CanStop(Elevator x, CallForElevator c) {
        boolean isLegal = false;
        if (x.getState() == 0){
           return true;}
        if (c.getType() == 1 && MT.table[x.getID()]instanceof minHeap||
                c.getType() == -1 && MT.table[x.getID()]instanceof maxHeap||MT.table[x.getID()]==null) {
            isLegal= true;}
        if (x.getState() == c.getType() && x.getState() == 1) {
            isLegal = (x.getPos() < c.getSrc());
        }
        if (x.getState() == c.getType() && x.getState() == -1) {
            isLegal = x.getPos() > c.getSrc();
        }
        return isLegal;
    }

    @Override
    public int allocateAnElevator(CallForElevator c) {
        double min = 999999999;//fix
        double time=0;
        int numOfElev = 0;

        for (int i = 0;  i>_building.numberOfElevetors() ; i++) {
            Elevator temp_elev = _building.getElevetor(i);
            if (temp_elev.getMaxFloor() > c.getDest() &&
                    temp_elev.getMinFloor() <= c.getDest() &&
                    temp_elev.getMaxFloor() > c.getSrc() &&
                    temp_elev.getMinFloor() <= c.getSrc()) {
                time = CalculateTime(temp_elev, c);//
                if (CanStop(temp_elev, c)) {
                    if (time < min) {
                        min = time;
                        numOfElev = i;

                    }
                }
            }
        }
        MT.add(c.getSrc(), c.getDest(), numOfElev);
        if (finalDest[numOfElev] == null) finalDest[numOfElev] = c.getDest();
        else {
            int direction = c.getType(), desten = c.getDest(), elvDestination = finalDest[numOfElev];

            if (direction == -1) {
                if (elvDestination < desten) {
                    finalDest[numOfElev] = desten;
                }
            } else if (direction == 1) {
                if (elvDestination > desten) {
                    finalDest[numOfElev] = desten;
                }
            }
        }

        return numOfElev;
    }


    @Override
    public void cmdElevator(int elev) {
        if (MT.table[elev] == null) return;
        Elevator elv = this.getBuilding().getElevetor(elev);
        int direction = elv.getState();
        if (direction == 1 || direction == -1) {//המעלית בתנועה
            if (finalDest[elev] != null) {
                int GoTo = MT.table[elev].peek();// for debag
                elv.stop(GoTo);
            }
        } else if (elv.getState() == -2) {//המעלית תקולה
//            while (!MT.table[elev].isEmpty()){
//                allocateAnElevator(elv.)
//            }
        } else {  //המעלית במנוחה
            if (finalDest[elev] != null) {
                if (elv.getPos() == finalDest[elev]) {//המעלית בקומת היעד
                    finalDest[elev] = null;
                    MT.table[elev].delete();
                }
                if (this.MT.table[elev].isEmpty()) {//אין עוד משימות בהיפ

//                    double rest =  this._building.numberOfElevetors()/(this._building.maxFloor()-this._building.minFloor())*elv.getID();
//                    if (elv.getPos() != rest) elv.goTo((int)rest);
                    elv.goTo(0);//לך למנוחה
                } else {
                    elv.goTo(MT.table[elev].peek());
                    finalDest[elev] = MT.table[elev].peek();
                }
            }

//            Integer newMiss = closestCall(elv.getPos(), elev);
//            if (newMiss != null) {
//                elv.goTo(newMiss);
//                destMission[elev] = newMiss;
//            }
        }
    }
}

//
//
//    public Integer closestCall(int elvNum) {
//        return MT.table[elvNum].peek();
//    }
//
//    public Integer middleStop(int elvNum, int dest, int src, int direction) {
//        Integer num = null;
//        if (direction == 1) {
//            for (int f = src + 1; f < dest; f++) {
//                if (MT.table[elvNum][f]) {
//                    num = f;
//                    break;
//                }
//            }
//        } else if (direction == -1) {
//            for (int f = src - 1; f > dest; f--) {
//                if (MT.table[elvNum][f]) {
//                    num = f;
//                    break;
//                }
//            }
//        }
//        return num;
//    }

