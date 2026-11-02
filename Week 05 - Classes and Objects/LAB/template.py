"""
RECORD CHECK  -  my version
===========================

Name  : Hetansh patel
Lane  :  AI
Date  : 23/10/2026

Run it:   python template.py

"""
class Record:
  
    over_limit_count = 0 

    def __init__(self, label, value, limit):
        self.label = label
        self.value = float(value)
        self.limit = float(limit)
        
        if self.status() == "OVER LIMIT":
            Record.over_limit_count += 1

    def status(self):
        percentage = (self.value / self.limit) * 100
        
        if percentage >= 100:
            return "OVER LIMIT"
        elif percentage >= 90:
            return "WARNING"
        else:
            return "OK"

def load_records(path):
    loaded_records = []
    
    with open(path, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                label, value, limit = line.split(",")
                new_record = Record(label, value, limit)
                loaded_records.append(new_record)
                
    return loaded_records

records = load_records("Week 05 - Classes and Objects/LAB/records_sample.txt")

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    
    print(f"  Value:   {record.value}")
    print(f"  Limit:   {record.limit}")
    print(f"  Status:  {record.status()}")
    
    print("=" * 34)

print(f"\nTotal records OVER LIMIT across the system: {Record.over_limit_count}")