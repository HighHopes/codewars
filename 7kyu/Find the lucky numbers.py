"""Write a function filterLucky/filter_lucky() that accepts a list of integers and filters the list to only include the elements that contain the digit 7."""


def filter_lucky(lst):
    return [i for i in lst if "7" in str(i)]
