# Unit 10 Session 2 Problem 2
def gcd_of_strings(str1, str2):
    # Always work with the shorter string first
    if len(str1) > len(str2):
        str1, str2 = str2, str1

    # Try all prefixes starting from the longest
    for i in range(len(str1), 0, -1):
        candidate = str1[:i]

        # Check if candidate can build str1
        repeated_str1 = candidate * (len(str1) // len(candidate))
        valid_str1 = repeated_str1 == str1

        # Check if candidate can build str2
        repeated_str2 = candidate * (len(str2) // len(candidate))
        valid_str2 = repeated_str2 == str2

        # If candidate builds both, return it
        if valid_str1 and valid_str2:
            return candidate

    return ""


# Test Cases

# Expected: "ABC"
print("Test 1:", gcd_of_strings("ABCABCABC", "ABCABC"))  
# Expected: "AB"
print("Test 2:", gcd_of_strings("ABABAB", "ABAB")) 
# Expected: ""      
print("Test 3:", gcd_of_strings("LEET", "CODE"))         