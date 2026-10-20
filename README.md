## Function First_ID(records)
This function only examines one item.  We believe that it is O of 1 for the reasons of it is a constant of scanning only one ID. 
---
## Function All_IDs(records)
This function examines every ID present in the code. We believe that it is O(n) because it runs through every record available only once.
---
## Function Ordered_Pairs(records)
This function examines every ID that is present twice and puts them into pairs and visits them. We believe that it is O(n^2) because it's running through the IDs twice and it creating ordered pairs in pairs of two.

---
## Functions Halving_Sizes(size)
This function examines every ID then repeatedly goes through them and reduces the remaining size of them. We believe that it is logarithmic, because it is not constant, linear, nor is it quadratic. 


# TUESDAY - Recognize growth; wait for Tuesday's instruction.
# Inspect first_id, all_ids, ordered_pairs, and halving_sizes in growth_examples.py.
# Ask whether each examines one item, visits every item, visits every pair, or repeatedly reduces the remaining size.
# Give each a Big-O label and one brief reason in your README.
# Explain how a first-match scan differs from a last-match or absent-ID scan.
# Finish focused tests for empty input, repeated queries, order, and unchanged data.
# No counter function, timer, benchmark runner, or experiment report is needed.

### Things to ask Cash:
* Can we move on to Thursday's stuff today?
    No
* Are we supposed to give our own explanation and reasoning's in our own README or the shared one?
    Yes
* Can we add the AI reasoning for the explanations and what we got wrong (if we did get something wrong) under each of the functions? If it agreed with us then just add that it helped us reassure our guess? 
    Yes, and yes.