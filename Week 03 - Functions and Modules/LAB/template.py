"""
RECORD CHECK  -  my version
===========================

Name  : Hetansh Patel
Lane  :  AI 
Date  :09/10/2026

Run it:   python template.py


"""

# ============================================================= FUNCTIONS

def status_of(percent):
    """Return status based on the percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Return the difference and percentage."""
    difference = limit - value
    percent = (value / limit) * 100
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    """Print the formatted report."""
    border = "=" * 29
    print(border)
    print(f"  RECORD CHECK  -  {label}")
    print(border)
    print(f"  {'Used':<10} : {value:>10.2f}")
    print(f"  {'Total':<10} : {limit:>10.2f}")
    print(f"  {'Free':<10} : {difference:>10.2f}")
    print(f"  {'Percent':<10} : {percent:>10.2f} %")
    print(f"  {'Status':<10} : {status:>10}")
    print(border)

over_limit_count = 0

while True:
    label = input("Enter dataset name (or 'quit' to stop): ").strip()
    if label.lower() == "quit":
        break

    rows_loaded = float(input("Enter rows loaded: "))
    rows_expected = float(input("Enter rows expected: "))

    difference, percent = check(rows_loaded, rows_expected)
    status = status_of(percent)

    if status == "OVER LIMIT":
        over_limit_count += 1

    print_report(label, rows_loaded, rows_expected, difference, percent, status)
    print()

print(f"Total records OVER LIMIT: {over_limit_count}")