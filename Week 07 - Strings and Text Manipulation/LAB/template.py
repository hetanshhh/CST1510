"""
RECORD CHECK  -  my version
===========================

Name  : Hetansh Patel
Lane  :  AI 
Date  : 08/11/2026

Run it:   python template.py

"""

# =================================================================== FUNCTIONS
def parse_line(raw_line):
    
    clean_line = raw_line.strip().lower()
    dataset_part, rest = clean_line.split(",", 1)

    record = {"dataset": dataset_part.strip()}

    for field in rest.split(","):
        key, value = field.split("=", 1)
        record[key.strip()] = float(value.strip())

    return record


def status_of(record):
    """Flag ratings outside 1–5 or negative ages."""
    if not 1 <= record["rating"] <= 5 or record["age"] < 0:
        return "FLAGGED"

    return "OK"


#%%
raw_records = []

with open(r"C:\Users\Het\Documents\CST1510\Week 07 - Strings and Text Manipulation\Week 07 - Strings and Text Manipulation\LAB\own_messy.csv", "r", encoding="utf-8") as file:
    for line in file:
        if line.strip():
            raw_records.append(line)


#%% 
record_count = 0
flagged_count = 0

for raw_record in raw_records:
    record = parse_line(raw_record)
    status = status_of(record)

    print(record, status)

    record_count += 1

    if status == "FLAGGED":
        flagged_count += 1

print(f"\nSummary: {record_count} records, {flagged_count} flagged.")


#%% 
bad_record = "Survey_test, rating=unknown, age=23"

try:
    print(parse_line(bad_record))
except ValueError as error:
    print(f"ValueError: {error}")

