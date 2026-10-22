"""Test cases for the catalog lookup functions.
"""

from Catalog_Data import BOOKS, validate_book_ids
from Main import find_Book, build_index, indexed_lookup, record_builder

# Test cases for the catalog lookup functions.
def test_find_Book():
    # Test the find_Book function with a small catalog.
    records = record_builder(5)
    # Validate the book IDs before running the tests.
    assert find_Book(records, 0) == {"id": 0}
    # Test the first and last valid IDs, and an absent ID.
    assert find_Book(records, 4) == {"id": 4}
    # Test a middle valid ID.
    assert find_Book(records, 5) is None
    
# Test the indexed_lookup function.
def test_indexed_lookup():
    # Test the indexed_lookup function with a small catalog.
    records = record_builder(5)
    # Validate the book IDs before building the index.
    index = build_index(records)
    # Test the first and last valid IDs, and an absent ID.
    assert indexed_lookup(index, 0) == {"id": 0}
    # Test a middle valid ID.
    assert indexed_lookup(index, 4) == {"id": 4}
    # Test an absent ID.
    assert indexed_lookup(index, 5) is None

# Test the validate_book_ids function.
def test_validate_book_ids():
    # Test the validate_book_ids function with the main BOOKS catalog.
    assert validate_book_ids(BOOKS) is None

if __name__ == "__main__":
    test_find_Book()
    test_indexed_lookup()
    test_validate_book_ids()
    print("All checks passed.")