"""
RECORD CHECK  -  my version
===========================

Name  : Hetansh Patel
Lane  :  AI and DS
Date  : 16/10/2026

Run it:   python template. 

"""

over_limit_count = 0

while True:
    label = input("Enter a label (name, hostname, or IP) or 'quit' to stop: ")
    
    if label.lower() == "quit":
        break
        
    value = float(input("Enter the current value: "))
    limit = float(input("Enter the limit : "))

    difference = value - limit
    percent = (value / limit) * 100 

    if percent >= 100:
        status = "OVER LIMIT"
        over_limit_count += 1
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    
    print(f"  Value:       {value:>10.2f}")
    print(f"  Limit:       {limit:>10.2f}")
    print(f"  Difference:  {difference:>10.2f}")
    print(f"  Percentage:  {percent:>10.2f}%")
    print(f"  Status:      {status:>10}")
    
    print("=" * 34)
    print()

print(f"Session ended. Total 'OVER LIMIT' records found: {over_limit_count}")
