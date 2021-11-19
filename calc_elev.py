from building import building
from Elevator import Elevator
from call_object import call_object


def match_elev(b: building, calls: [call_object]):
    global chosen
    for c in calls:
        time = 999999 #calc_time(c, b.elevators[0])
        for e in b.elevators:
            elv_time = calc_time(c, e)
            if elv_time < time:
                time = elv_time
                chosen = b.elevators[e.id]
        chosen.add_call(c)
        c.alloc = chosen.id


def calc_time(c: call_object, e: Elevator):
    cur = e.current_pos(c)
    floor_time = e.openTime + e.stopTime + e.closeTime + e.startTime
    dist = abs(cur - c.src) * e.speed
    sum = (dist / e.speed) + floor_time
    return sum
