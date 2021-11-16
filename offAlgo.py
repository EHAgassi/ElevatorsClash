import csv

from building import building
from call_object import call_object


def write_calls():
    data_call =[]

    for c in calls:
        data_call.append(c.__dict__.values())
    file_name = "output.csv"
    with open(file_name, 'w', newline="") as file:
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

    #     here should matching the elev algorithm


    write_calls()
