from Elevator import Elevator
import json


class building:
    elevators = [Elevator]
    minfloor = 0
    maxfloor = 0

    def __init__(self, minfloor=0, maxfloor=0, elevators=0):

        self.minfloor = minfloor
        self.maxfloor = maxfloor
        self.elevators = []

    def read_json(self, file_path: str):
        try:
            with open(file_path, "r") as INPUT:
                # elv = []
                my_elev = json.load(INPUT)
                self.minFloor = my_elev["_minFloor"]
                self.maxFloor = my_elev["_maxFloor"]

                for e in my_elev["_elevators"]:
                    self.elevators.append(Elevator(e))
                    print(e)
        except IOError as e:
            print(e)

    def __str__(self) -> str:
        return f"Building:Min&Max floor: {self.minFloor}'-'{self.maxFloor} and"

    def __repr__(self) -> str:
        return f"Building:Min&Max floor: {self.minFloor}'-'{self.maxFloor} and "