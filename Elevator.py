
from call_object import call_object

UP = True
DOWN = False


class Elevator:
    pos = None
    call_queue = None

    def __init__(self, dict):
        self.id = dict["_id"]
        self.speed = dict["_speed"]
        self.minFloor = dict["_minFloor"]
        self.maxFloor = dict["_maxFloor"]
        self.closeTime = dict["_closeTime"]
        self.openTime = dict["_openTime"]
        self.startTime = dict["_startTime"]
        self.stopTime = dict["_stopTime"]
        self.diraction = None
        self.pos = 0
        self.call_queue = None  #

    def current_pos(self, c):
        curr_time = 0
        curr_pos = self.pos
        if (self.call_queue != None):
            temp_queue = self.call_queue.copy()
            floor_time = self.openTime + self.stopTime+self.closeTime + self.startTime

            while (curr_time <= c.time) and (temp_queue):
                call = temp_queue.pop()
                dist = abs(curr_pos - call.src)
                dist += abs(call.src - call.dest)
                curr_time += floor_time + (dist / self.speed)
                curr_pos = call.dest
        self.pos = curr_pos

    def add_call(self, c: call_object):

        if self.call_queue is None:
            self.call_queue = [c]
        else:
            self.call_queue.append(c)

    # def __str__(self) -> str:
    #     return f"\n\tElevator id is: {self.id} speed: {self.speed} Min-Max floor: {self.minFloor}-{self.maxFloor}"
    #
    # def __repr__(self) -> str:
    #     return f"\n\tElevator id is: {self.id} speed: {self.speed} Min-Max floor: {self.minFloor}-{self.maxFloor}"
