"""Optional English-first starter; one recognition-level app across three days."""

from catalog_data import BOOKS, validate_book_ids

# MONDAY - Implement equivalent lookups after Monday's instruction.


def find_Book(records, book_id):
    """Return the first matching book, or None when absent."""
    # Look at one record at a time, in its original order.
    # Compare its ID with the requested ID.
    # Return the record immediately when it matches.
    # Return None if you reach the end without a match.
    # Do not change the input records.
    for book in records:
        if book["id"] == book_id:
            return book
    return None


def build_index(records):
    """Map each previously validated catalog ID to its book record."""
    # Begin with an empty dictionary.
    # Visit each book once; use its ID as the key and its record as the value.
    # Return the completed index without changing the original records.
    # Use the supplied ID precheck before building; do not resolve duplicates.
    index = {}
    for book in records:
        index[book["id"]] = book
    return index


def indexed_lookup(index, book_id):
    """Return the indexed book or None when the catalog ID is absent."""
    # Check whether the requested ID is a dictionary key.
    # Return the associated book when present; otherwise return None.
    # Do not rebuild the dictionary here.
    if book_id in index:
        return index[book_id]
    return None


def record_builder(size):
    """Build a catalog with the requested number of records."""
    return [{"id": book_id} for book_id in range(size)]


def find_Book(records, book_id):
    """Return the scan result and the number of ID comparisons."""
    comparisons = 0
    for book in records:
        if book["id"] == book_id:
            return book
    return None


def main():
    """Show the examples for the lookup functions you have completed."""
    # Begin a fresh shared project; do not choose either partner's AL01 code.
    # Use the supplied BOOKS list and validate its catalog IDs.
    # Build an index once; look up every ID supplied by the catalog.
    # Compare both lookup answers and show ID, title, author, or a not-found message.
    # Replace this message when the Monday functions are ready.
    validate_book_ids(BOOKS)
    index = build_index(BOOKS)

    for book in BOOKS:
        book_id = book["id"]
        scan_result = find_Book(BOOKS, book_id)
        index_result = indexed_lookup(index, book_id)
        print("Looking up", book_id)
        print("  Same answer from both lookups:", scan_result == index_result)
        if scan_result is None:
            print("  Not found.")
        else:
            print("  ID:", scan_result["id"])
            print("  Title:", scan_result["title"])
            print("  Author:", scan_result["author"])

    print("\nWhen every query misses:")
    # Two fixed queries stay O(n); n queries become O(n^2).
    for size in (4, 8):
        scan_result = find_Book(record_builder(size), -1)
        print(
            f"n={size}: 2 fixed queries -> {2}; n queries -> {size * 1}"
        )
    print("Fixed q: O(n). If q grows with n: O(n^2).")


# TUESDAY - Recognize growth; wait for Tuesday's instruction.



# Inspect first_id, all_ids, ordered_pairs, and halving_sizes in growth_examples.py.
# Ask whether each examines one item, visits every item, visits every pair,
# or repeatedly reduces the remaining size.
# Give each a Big-O label and one brief reason in your README.
# Explain how a first-match scan differs from a last-match or absent-ID scan.
# Finish focused tests for empty input, repeated queries, order, and unchanged data.
# No counter function, timer, benchmark runner, or experiment report is needed.

# THURSDAY - Choose qualitatively and submit after Thursday's instruction.
# Consider a patron's one first-book request when the catalog list is available.
# Contrast it with a circulation desk's repeated IDs when an index can be reused.
# Explain construction and extra storage, not a measured speed winner.
# Add brief choices, learning, contribution, and assistance notes to the README.
# Copy the full app, data, growth examples, tests, and imported support modules
# into your own class repository; test the copy and submit your own URL.
# Keep this same main.py all week; no artificial extra feature or report.


if __name__ == "__main__":
    main()
