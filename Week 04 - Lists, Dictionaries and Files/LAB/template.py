"""
RECORD CHECK  -  my version
===========================

Name  : Hetansh Patel
Lane  :  AI
Date  : 31/10/2026

Run it:   python template.py

"""

def check(value, limit):
   
    difference = limit - value
    percent = (value / limit) * 100

    if value > limit:
        status = "OVERLIMIT"

    else: 
        status = "OK"
    return difference, percent, status


def report(label, value, limit, difference, percent, status):
    print("Record:", label)
    print("Value:", value)
    print("Limit:", limit)
    print("Difference:", difference)
    print("Percentage:", round(percent, 2), "%")
    print("status", status)
    print("----------------------")


def load_records(path):
    records=[]

    with open(path, "r")as file:
        for line in file:
            line = line.strip()

            if line:
                label, value, limit = line.split(",")

                records.append({"label": label, "value": float(value), "limit": float(limit) })

    return records

records = load_records(r"C:\Users\Het\Documents\CST1510\Week 04 - Lists, Dictionaries and Files\LAB\results.txt") 

for record in records:
    difference , percent, status = check(
        record["value"], record["limit"]
    )

    report(
        record["label"],
        record["value"],
        record["limit"],
        difference,
        percent,
        status
    )




