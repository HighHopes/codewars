"""his function should test if the factor is a factor of base.

Return true if it is a factor or false if it is not.

Information
Factors are numbers you can multiply together to get another number.

2 and 3 are factors of 6 because:

2 * 3 = 6"""


def check_for_factor(base, factor):
    return base % factor == 0

print(check_for_factor(10,2))
