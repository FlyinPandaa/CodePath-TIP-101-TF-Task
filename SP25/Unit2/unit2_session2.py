# PROBLEM 6 [Version 1]

# 1. Share 2 questions you would ask to help understand the question:
#    Can there be more than two duplicates?
#    Can list 'nums' be empty?

# 2. Write out in plain English what you want to do:
#    Create an empty dictionary to keep track of the elements. When we find an element for a 2nd time, we can check if the index is within a certain range of each other.

# 3. Translate each sub-problem into pseudocode:
#    recentIndex = {}
#    Loop through the nums list:
#       if current index is in recentIndex:
#    calculate the difference in index placement
#       if the difference is less than k:
#           return True
#       set the current value to i
#    return False if reaching the end of the function and haven't found a duplicate that falls within the criterias.

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(n)

def hasDuplicates(nums, k):
    recentIndex = {}
    
    for i in range(len(nums)):
        if nums[i] in recentIndex:
            diff = i - recentIndex[nums[i]]
            
            if diff <= k:
                return True
            
        recentIndex[i] = i
        
    return False



# PROBLEM 7 [Version 1]

# 1. Share 2 questions you would ask to help understand the question:
#    Would we return false if the one element has more than one pair?
#    Will we be given negative elements?

# 2. Write out in plain English what you want to do:
#    Utilize a frequency map to check if there are pairs that satisfy the conditions.

# 3. Translate each sub-problem into pseudocode:
#    Create empty dictionary
#    Loop through each num:
#       Add 1 to frequency map
#    for each count in the frequency map:
#    if count is odd: return False
#    All count is even: return True

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(n)

def divideList(nums):
    freqMap = {}
    
    for num in nums:
        freqMap[num] = freqMap.get(num, 0) + 1
        
    for count in freqMap.values():
        if count % 2 != 0:
            return False
    
    return True
    pass

# PROBLEM 6 [Version 2]

# 1. Share 2 questions you would ask to help understand the question:
#    What if the list 'nums' is empty?
#    What if nums[i] is less than nums[j]?

# 2. Write out in plain English what you want to do:
#    Sort list from smallest to largest values. The smallest number after the list is sorted will be the smallest element. Rearrange the results back into original order.

# 3. Translate each sub-problem into pseudocode:
#    Create sorted list
#    Create empty dictionary
#    Loop through each index in list 'nums':
#       if value not in dictionary: map val  to index
#       else skip
#    Create empty list to store results
#    for each num in the original list:
#       Use dictionary to count
#       Add count value to our res list
#    Return res


# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(n)

def smallerNumbersThanCurrent(nums):
    sorted_nums = sorted(nums)
    
    smallCountMap = {}
    for i in range(len(sorted_nums)):
        num = sorted_nums[i]
        
        if num not in smallCountMap:
            smallCountMap[num] = i
            
    res = []
    for num in nums:
        res.append(smallCountMap[num])
        
    return res
    pass


# PROBLEM 7 [Version 2]

# 1. Share 2 questions you would ask to help understand the question:
#    What if list is empty?
#    Does the list of integers given be positive?

# 2. Write out in plain English what you want to do:
#    Find out how many of each element are in the list. Calculate how many good pairs can be made.

# 3. Translate each sub-problem into pseudocode:
#    Create a frequency map
#    Create a variable that can hold pairs
#    Loop through each value in frequency map:
#       Calculate good pairs
#    return the total number of good pairs

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(n)

def numIdenticalPairs(nums):
    freq_map = {}
    
    for num in nums:
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1
    
    good_pairs = 0
    for i in freq_map.values():
        good_pairs += i * (i - 1) // 2
        
    return good_pairs
    pass


# PROBLEM 1 [Version 2]

# 1. Share 2 questions you would ask to help understand the question:
#    What if points are always negative/positive integers?
#    What if we are given an empty input?

# 2. Write out in plain English what you want to do:
#    If player exists in dictionary, add point to the score. Otherwise add the player to the dictionary.

# 3. Translate each sub-problem into pseudocode:
#    Check if player is in dictionary
#       If yes: add points to player's current score
#    Otherwise, add player to the dictionary
#    Return the dictionary

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(1)
# Space Complexity: O(n)

def update_score(scores, player, points):
    if player in scores:
        scores[player] += points
    else:
        scores[player] = points
    return scores
