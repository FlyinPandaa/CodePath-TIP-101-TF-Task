# File to help students during breakout sessions

# ------------------------------------------------------------------------------------------------

# Session 1

def first_uniq_char(myStr):
    # Initialize a dictionary to store all the frequency of each character
    d = {}
    
    # Loop through each character in the input string myStr
    for char in myStr:
        # Check if the current character "char" is already in the dictionary "d"
        if char in d:
            # If character exists, add 1 to the frequency count
            d[char] += 1
        else:
            # Otherwise, add the new character to the dictionary, and set the count to 1
            d[char] = 1

    # Find the first non-repeating character
    # Loop through myStr again using the enumerate method
        # index = Position of the character in "myStr"
        # char = The actual character ('a', 'b', etc..)
    for index, char in enumerate(myStr):
        # If there is only one count of a character, that is a unique character
        # Return the index
        if d[char] == 1:
            return index
    
    # If we run through the entire function, and a unique character doesn't exist
        # Return -1
    return -1


# Session 2

def reverse_only_letters(s):
    # Create an empty list to store all letters from the input string
    letters = []  
    
    # Loop through each character in the string
    for c in s:
        # If the character is a letter, add it to the letters list
        if c.isalpha():
            letters.append(c)
    
    # Initialize an empty string to store the final result
    result = ""
    
    # Start from the last index of the collected letters (reversed order)
    letters_index = len(letters) - 1  
    
    # Loop through the original string again
    for c in s:
        # If the character is a letter, replace it with the reversed letter
        if c.isalpha():
            result += letters[letters_index]  # Get the last stored letter
            letters_index -= 1  # Move to the previous letter
        # If the character is not a letter, keep it unchanged
        else:
            result += c  
    
    # Return the modified string with letters reversed but non-letters in place
    return result  

    
print(reverse_only_letters("a-bC-dEf-ghIj"))  
# Output: "j-Ih-gfE-dCba"

print(reverse_only_letters("Test1ng-Leet=code-Q!"))  
# Output: "Qedo1ct-eeLg=ntse-T!"

