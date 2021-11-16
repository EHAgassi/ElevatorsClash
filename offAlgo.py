import csv
from call_object import call_object
from building import building
import Elevator
import pandas

def write_calls():
    data_call =[]
        # 'matched_calls.csv'
    for c in calls:
        data_call.append(c.__dict__.values())
    with open("filename", 'w', newline="") as file:
        csvwriter = csv.writer(file)
        csvwriter.writerows(data_call)


if __name__ == '__main__':
    calls = []

    with open("calls_a.csv") as file:
        csvReader = csv.reader(file)
        for row in csvReader:
            calllist = call_object(name=row[0], time=row[1], src=row[2], dest=row[3], non=row[4], alloc=row[5])
            calls.append(calllist)

    print(calls)

    b = building()
    b.read_json("B2.json")
    print(b)

    #     here should matching the elev

    # new_calllist = []
    # for row in calls:
    #     new_calllist.append(row.__dict__.values())

    write_calls()
    # filename = 'matched_calls.csv'
    # with open(filename, 'w', newline="") as file:
    #     csvwriter = csv.writer(file)
    #     csvwriter.writerows(calls.__dict__)
