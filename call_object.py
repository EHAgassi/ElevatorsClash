class call_object:

    def __init__(self, name : str, time, src, dest, non,alloc) -> None:
        self.name = name
        self.time = float(time)
        self.src = int(src)
        self.dest = int(dest)
        self.non = non
        self.alloc = -1

    def allocate (self ,num):
        self.alloc = num

    def matchelev(self, elevnum):
        self.elev = elevnum

    def __str__(self) -> str:
        return f"Time: {self.time}, Src floor:{self.src}, Destination floor: {self.dest}, Allocated Elevator: {self.alloc}"

    def __repr__(self) -> str:
        return f"Time: {self.time}, Src floor:{self.src}, Destination floor: {self.dest}, Allocated Elevator: {self.alloc}"
