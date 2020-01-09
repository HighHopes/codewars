"""Write a function with the signature shown below:

def is_int_array(arr):
    return True
returns true / True if every element in an array is an integer or a float with no decimals.
returns true / True if array is empty.
returns false / False for every other input."""

def is_int_array(arr):
    def is_int_array(arr):
    if arr == []:
        return True
    if arr == None or arr == "":
        return False
    elif None in arr:
        return False
    else:
        r = 0
        for i in arr:
            if isinstance(i, int):
                r += 1
            elif isinstance(i, float) and i % 1 == 0:
                r += 1
            else:
                return False

        if r == len(arr):
            return True


print(is_int_array([]))  # True, "Input: []")
print(is_int_array([1, 2, 3, 4]))  # True, "Input: [1, 2, 3, 4]")
print(is_int_array([-11, -12, -13, -14]))  # True, "Input: [-11, -12, -13, -14]")
print(is_int_array([1.0, 2.0, 3.00001]))  # True, "Input: [1.0, 2.0, 3.0]")
print(is_int_array([1, 2, None]))  # False, "Input: [1,2, None]")
print(is_int_array(None))  # False, "Input: [1,2, None]")
print(is_int_array([None]))  # False, "Input: [1,2, None]")
print(is_int_array(["-1"]))  # False, "Input: [1,2, None]")
