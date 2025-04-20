# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

# Example: (Input --> Output)

# "Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

# isIsogram "Dermatoglyphics" = true
# isIsogram "moose" = false
# isIsogram "aba" = false

def create_phone_number(n):
    first = ''
    second = ''
    third = ''

    for i in range(3):
        first += str(n[i])
    for i in range(3,6):
        second += str(n[i])
    for i in range(6,10):
        third += str(n[i])
    
    return '(' + first + ')' + ' ' + second + '-' + third

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

# optimal_solution >
# def create_phone_number(n):
# 	return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


