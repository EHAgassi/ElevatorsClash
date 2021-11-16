class call_object:
    def __init__(self, name='name', time=0, src=0, dest=0, non=0, alloc=-1) -> None:
        self.name = name
        self.time = time
        self.src = src
        self.dest = dest
        self.non = non
        self.alloc = alloc


    def matchelev(self, elevnum):
        self.elev = elevnum


    def __str__(self) -> str:
        return f"Time: {self.time}, Src floor:{self.src}, Destination floor: {self.dest}, Allocated Elevator: {self.alloc}"


def __repr__(self) -> str:
    return f"Time: {self.time}, Src floor:{self.src}, Destination floor: {self.dest}, Allocated Elevator: {self.alloc}"
