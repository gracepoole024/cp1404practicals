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
INDEX_CHAMPION = 2
INDEX_CHAMPION_COUNTRY = 3


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


def format_wimbledon_records(wimbledon_records):
    champion_to_count = {}
    countries = set()
    for record in wimbledon_records:
        countries.add[INDEX_CHAMPION_COUNTRY]
        champion_to_count[record[INDEX_CHAMPION]] += 1
    return champion_to_count, countries


main()
