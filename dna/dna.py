import csv
import sys


def main():
    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python3 dna.py databases/name.csv sequences/name.txt")
        sys.exit(1)

    database_path = sys.argv[1]
    sequence_path = sys.argv[2]

    # TODO: Read database file into a variable
    database: list[dict] = []
    try:
        with open(database_path) as database_file:
            reader = csv.DictReader(database_file)
            for row in reader:
                database.append(row)
    except FileNotFoundError:
        print(f"Database file: '{database_path}' cannot be found!")
        sys.exit(2)

    # TODO: Read DNA sequence file into a variable
    sequence = []
    try:
        with open(sequence_path) as sequence_file:
            sequence = sequence_file.read()
    except FileNotFoundError:
        print(f"Sequence file: '{sequence_path}' cannot be found!")
        sys.exit(2)

    # TODO: Find longest match of each STR in DNA sequence
    AGATC_count = longest_match(sequence, "AGATC")
    AATG_count = longest_match(sequence, "AATG")
    TATC_count = longest_match(sequence, "TATC")

    # TODO: Check database for matching profiles
    for entry in database:
        if int(entry["AGATC"]) == AGATC_count and \
            int(entry["AATG"]) == AATG_count and \
            int(entry["TATC"]) == TATC_count:
            print(entry["name"])
            return

    print("No Match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):
        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:
            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
