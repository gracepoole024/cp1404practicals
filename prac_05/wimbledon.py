"""
CP1404/CP5632 Practical 5
Wimbledon Program
"""

"""
Emails
Estimate: 40 minutes
Actual:    43 minutes
"""

FILENAME = "wimbledon.csv"
INDEX_CHAMPION = 2
INDEX_CHAMPION_COUNTRY = 3


def main():
    """Read data file and print details about Wimbledon champions and countries."""
    wimbledon_records = load_wimbledon_records(FILENAME)
    champion_to_count, countries = format_wimbledon_records(wimbledon_records)
    display_wimbledon_results(champion_to_count, countries)


def load_wimbledon_records(filename):
    """Load Wimbledon.csv as nested list."""
    wimbledon_records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # skip heading
        for line in in_file:
            parts = line.strip().split(",")
            wimbledon_records.append(parts)
    return wimbledon_records


def format_wimbledon_records(wimbledon_records):
    """Format Wimbledon champions to number of wins as dictionary and countries as a set."""
    champion_to_count = {}
    countries = set()
    for record in wimbledon_records:
        countries.add(record[INDEX_CHAMPION_COUNTRY])
        try:
            champion_to_count[record[INDEX_CHAMPION]] += 1
        except KeyError:
            champion_to_count[record[
                INDEX_CHAMPION]] = 1  # Avoid KeyError error when a champion has first win(Key doesn't exist yet)
    return champion_to_count, countries


def display_wimbledon_results(champion_to_count, countries):
    """Display Wimbledon results."""
    print("Wimbledon Champions:")
    for champion, count in champion_to_count.items():
        print(champion, count)
    print(f"\nThese {len(countries)} have won Wimbledon:")
    print(",".join(sorted(countries)))


main()
