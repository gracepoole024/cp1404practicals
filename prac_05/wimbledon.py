"""
CP1404/CP5632 Practical 5
Wimbledon
"""

"""
Emails
Estimate: 40 minutes
Actual:    minutes
"""

FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    """Read data file and print details about Wimbledon champions and countries."""
    pass

def load_wimbledon_records(filename):
    """Load Wibledon.csv as nested list"""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        wimbledon_records = []
        for line in in_file:
            parts = line.strip.split(",")
            wimbledon_records.append(parts)
    return wimbledon_records



main()
