def reverse_only_letters(s):
    #  Initialize letters
    letters = []
    
    # grab all letters
    for char in s:
        if char.isalpha():
            letters.append(char)

#   Store result
    result = ""
    
#   Ensure we are in the correct index
    l_index = len(letters) - 1

#   This reverses the string
    for char in s:
        if char.isalpha():
            result += letters[l_index]
            l_index -= 1
        else:
            result += char
        
    return result

pass

s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)