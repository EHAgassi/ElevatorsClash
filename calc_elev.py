from building import building
from Elevator import Elevator
from call_object import call_object


def match_elev(b : building, calls : [call_object]):


    global chosen
    for c in calls:
        time = 99999
        num = -1
        for e in b.elevators:
            num = num+1
            elv_time = calc_time(c, e)
            if elv_time < time:
                time = elv_time
                chosen = b.elevators[num]
        chosen.add_call(c)
        y= 0-b.elevators[0].id
        c.alloc= chosen.id+y


def calc_time(c : call_object, e : Elevator):
    e.current_pos(c)
    floor_time = e.openTime + e.stopTime+e.closeTime + e.startTime
    dist = abs(e.pos - c.src) * e.speed
    sum = (dist / e.speed) + floor_time
    return sum
