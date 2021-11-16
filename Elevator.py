#  def offlineAlgorithm (Building , Calls, output):
# # def offlineAlgorithm < Building.json > < Calls.csv > < output.csv >
import json


class Elevator:
    def __init__(self, dict):
        self.id = dict["_id"]
        self.speed = dict["_speed"]
        self.minFloor = dict["_minFloor"]
        self.maxFloor = dict["_maxFloor"]
        self.closeTime = dict["_closeTime"]
        self.openTime = dict["_openTime"]
        self.startTime = dict["_startTime"]
        self.stopTime = dict["_stopTime"]

    # for key, value in my_elev._elevators():
    #     self = elevator(**value)
    #     elevs[e.id] = e

    def __str__(self) -> str:
        return f"Elevator id is{self.id}\nspeed: {self.speed}\n Min&Max floor: {self.minFloor}'-'{self.maxFloor}"

    def __repr__(self) -> str:
        return f"Elevator id is{self.id}\nspeed: {self.speed}\n Min&Max floor: {self.minFloor}'-'{self.maxFloor}"
