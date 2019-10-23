def multiply_all(lst):
    def multiply_number(num):
        return [i * num for i in lst]
    
    return multiply_number


print(multiply_all([1, 2, 3])(2))
