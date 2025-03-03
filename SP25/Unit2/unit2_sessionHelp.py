# def cast_vote(votes, candidate):
#    if candidate in votes:
#     votes[candidate] += 1
#    else:
#     votes[candidate] = 1
    
#     return votes

# # votes = {"bob":5,"mary":4}
# # cast_vote(votes,"mary")
# # print(votes)

# votes = {"Alice": 5, "Bob": 3}
# cast_vote(votes, "Alice")
# print(votes)
# cast_vote(votes, "Gina")
# print(votes)



## Section 6

def count_by_category(items):
    # 1. make empty dict
    result = {}

    # 2. loop through items
    for category, _ in items:
        # 3. if category is in dict, increment value by 1
        #    otherwise, add category to dict with value of 1
        categoryLower = category.lower()
        if categoryLower in result:
            result[categoryLower] += 1
        else:
            result[categoryLower] = 1

    # return dict
    return result

items = [("fruits", "apple"), ("vegetables", "carrot"), ("fruits", "banana")]
# expected output: {"fruits": 2, "vegetables": 1}
print(count_by_category(items))

items = []
print(count_by_category(items))

items = [("fruits", "apple"), ("vegetables", "carrot"), ("Fruits", "banana")]
# expected output: {"fruits": 2, "vegetables": 1}
print(count_by_category(items))