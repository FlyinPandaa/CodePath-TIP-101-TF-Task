# Set 1

# PROBLEM 7

# 1. Share 2 questions you would ask to help understand the question:
#    What if the rating is empty?
#    How do we grab the look at only the rating in the list of inputs?

# 2. Write out in plain English what you want to do:
#    Loop through the list, and find the ratings of all the items in the list. Find the highest rating and set that to result.

# 3. Translate each sub-problem into pseudocode:
#    if not books: return None
#    set res = books[0]
#    Loop through list:
#       compare current element to the current highest rated book
#         replace the highest rating book if needed
#    return the res

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(n)

def highest_rated(books):
    if not books: 
        return None
    
    res = books[0]
    
    for i in books[1:]:
        if i['rating'] > res['rating']:
            res = i
            
    return res

# PROBLEM 8

# 1. Share 2 questions you would ask to help understand the question:
#    What if the list is empty?
#    Do we need to use a hashmap?

# 2. Write out in plain English what you want to do:
#    Turn a list of values into a map.

# 3. Translate each sub-problem into pseudocode:
#    iv_map = {}
#    loop through the list:
#       turn the list of values into a map
#    return iv_map

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(1)

def index_to_value_map(lst):
    iv_map = {}
    
    for i in range(len(lst)):
        iv_map[i] = lst[i]
        i += 1
        
    return iv_map
    pass



# Set 2

# PROBLEM 7

# 1. Share 2 questions you would ask to help understand the question:
#    What if the 'ratings' is blank/empty?
#    Can the entire movies list be empty?

# 2. Write out in plain English what you want to do:
#    Create two dictionaries. One for mapping genre to rating, and another mapping genre to number of movies.

# 3. Translate each sub-problem into pseudocode:
#    Create two count/rating dictionaires
#    loop through the movie list:
#       Add the movie rating to rating total
#       Increment the movie total by 1
#    Else, add the rating as a new genre
#    set avg_rating to 0
#    Loop through each of the genres:
#       Calculate the avgerage rating for each genre
#       compare current highest rating to the current value
#    Return highest rating by genre

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(n)

def most_popular_genre(movies):
    genreRating = {}
    movieTotal = {}
    
    for movie in movies:
        curr_genre = movie['genre']
        if curr_genre not in genreRating:
            genreRating[curr_genre] = movie['rating']
            movieTotal[curr_genre] = 1
        else:
            genreRating[curr_genre] += movie['rating']
            movieTotal[curr_genre] += 1
            
    res = 0
    most_popular_genre = None
    
    for genre in genreRating:
        avgRating = genreRating[genre] / movieTotal[genre]
        
        if avgRating > res:
            res = avgRating
            most_popular_genre = genre
            
    return most_popular_genre
    pass



# PROBLEM 8

# 1. Share 2 questions you would ask to help understand the question:
#    How do we create a new dictionary to return the correct key-value pair.
#    What if 'threshold' is empty?

# 2. Write out in plain English what you want to do:
#    Loop through the list of products and compare their scores to the threshold. Assign pass or fail and add the elements to a new dictionary.

# 3. Translate each sub-problem into pseudocode:
#    Create product dictionary
#    Loop through the list of products:
#       If below threshold: "fail"
#       If above threshold: "pass"
#    Return the product dictionary

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(n)

def quality_control(product_scores, threshold):
    catProduct = {}
    
    for i in product_scores:
        if product_scores[i] >= threshold:
            catProduct[i] = "pass"
        else:
            catProduct[i] = "fail"
            
    return catProduct
    pass

