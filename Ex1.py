import csv
from calc_elev import match_elev
from building import building
from call_object import call_object

def open_csv(csv_filename):
    with open(csv_filename) as file:
        csvReader = csv.reader(file)
        for row in csvReader:
            calllist = call_object(name=row[0], time=row[1], src=row[2], dest=row[3], non=row[4], alloc=row[5])
            calls.append(calllist)

    print(calls)


def write_csv():
    data_call = []
    for c in calls:
        data_call.append(c.__dict__.values())
    file_name = "output.csv"
    with open(file_name, 'w', newline="") as file:
        csvwriter = csv.writer(file)
        csvwriter.writerows(data_call)


if __name__ == '__main__':
    b = building()
    calls = []
    ###
    open_csv("Calls_a.csv")
    b.read_json("B1.json")
    ###
    match_elev(b, calls)
    write_csv()
