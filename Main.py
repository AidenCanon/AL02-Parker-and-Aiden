
from Catalog_Data import BOOKS, validate_book_ids
    


def scan_lookup(records, book_id):
    """ 
    Look at one record at a time, in its original order.
    Compare its ID with the requested ID.
    Return the record immediately when it matches.
    Return None if you reach the end without a match.
    Do not change the input records. 
    """
    for record in records:
        if not record.get("id") == book_id:
            return None
        return record[0]
        



def build_index(records):
    index = {}
    for record in records:
        book_id = record.get("id")
        index[book_id] = record
    return index



def indexed_lookup(index, book_id):
    if book_id not in index:
        return None
    return index.get(book_id)

    




def main():




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