def is_nested(paren_s):
    # Base case: empty string is valid
    if paren_s == "":
        return True

    # Check outermost parentheses using recursion
    elif paren_s[0] == "(" and paren_s[-1] == ")":
        return is_nested(paren_s[1:-1])
    
    # All other cases(if we reach this point) is invalid nesting
    else:
        return False

# Tests:
paren_s = "(())"
print(is_nested(paren_s))  # Output: True

print(is_nested("(()())") ) # Output: False
print(is_nested("(()") ) # Output: False


# Session 6:

def letter_case_permutation(s):
    result = [""]  # Empty string

    for char in s:
        if char.isalpha():
            # Branch for each letter for lowercase and uppercase
            result = [prefix + char.lower() for prefix in result] + \
                     [prefix + char.upper() for prefix in result]
        else:
            # For digits, just append to all current strings
            result = [prefix + char for prefix in result]

    return result


# Test Cases:

print(letter_case_permutation("a1b"))
# Expected: ['a1b', 'a1B', 'A1b', 'A1B']

print(letter_case_permutation("a1B2"))
# Expected: ['a1b2', 'a1B2', 'A1b2', 'A1B2']

print(letter_case_permutation(""))
# Expected: ['']  # One empy string