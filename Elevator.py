#  def offlineAlgorithm (Building , Calls, output):
# # def offlineAlgorithm < Building.json > < Calls.csv > < output.csv >


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



    def __str__(self) -> str:
        return f"\n\tElevator id is: {self.id} speed: {self.speed} Min-Max floor: {self.minFloor}-{self.maxFloor}"

    def __repr__(self) -> str:
        return f"\n\tElevator id is: {self.id} speed: {self.speed} Min-Max floor: {self.minFloor}-{self.maxFloor}"
