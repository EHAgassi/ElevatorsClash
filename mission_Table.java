package ex0.algo;

import java.util.Comparator;
import java.util.PriorityQueue;

class minHeap implements MinMaxHeap {
    PriorityQueue<Integer> minHeap = new PriorityQueue<>();

    public minHeap(int n) {
        minHeap.add(n);
    }

    @Override
    public void add(int a) {
        minHeap.add(a);
    }

    @Override
    public void delete() {
        minHeap.poll();
    }

    @Override
    public Integer peek() {
        return minHeap.peek();
    }

    @Override
    public boolean isEmpty() {
        return minHeap.isEmpty();
    }

    @Override
    public int size() {
        return minHeap.size();
    }
}

class maxHeap implements MinMaxHeap {
    PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Comparator.reverseOrder());

    public maxHeap(int n) {
        maxHeap.add(n);
    }

    @Override
    public void add(int a) {
        maxHeap.add(a);
    }

    @Override
    public void delete() {
        maxHeap.poll();
    }

    @Override
    public Integer peek() {
        return maxHeap.peek();
    }

    @Override
    public boolean isEmpty() {
        return maxHeap.isEmpty();
    }

    @Override
    public int size() {
        return maxHeap.size();
    }
}

public class mission_Table {
    MinMaxHeap[] table;

    public mission_Table(int elveNum) {
        this.table = new MinMaxHeap[elveNum];
    }



    public void add(int src, int dest, int elevNum) {
        if (this.table[elevNum] == null) {
            if (src - dest <= 0) table[elevNum] = new minHeap(src);
            else table[elevNum] = new maxHeap(src);
        }
        else {
            table[elevNum].add(src);
        }
        table[elevNum].add(dest);
    }



//    public int stopsToDest(mission_Table MT, int elvNum, int dest, int srcFloor) {
//        int num = 0;
//        for (boolean f : MT.table[elvNum])
//            if (f) num++;
//        return num;
//    }


//    public boolean[][] getTable() {
//        return table;
//    }

//    public void setTabletrue(int floor, int elev) {
//        this.table[floor][elev] = true;
//    }
}
