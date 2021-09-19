'''
DIRECTIONS
==========

1. Given the list `friend_favorites`, create 
a new data structure in the function `create_new_candy_data_structure` 
that describes the different kinds of candy paired with a list of friends that 
like that candy. 

friend_favorites = [
    [ "Sally", [ "lollipop", "bubble gum", "laffy taffy" ]],
    [ "Bob", [ "milky way", "licorice", "lollipop" ]],
	[ "Arlene", [ "chocolate bar", "milky way", "laffy taffy" ]],
	[ "Carlie", [ "nerds", "sour patch kids", "laffy taffy" ]]
]

2. In `get_friends_who_like_specific_candy()`, return friends who like lollipops.

3. In, `create_candy_set()`, return a set of all the candies from
the data structure made in `create_new_candy_data_structure()`.

4. Write tests for all of the functions in this exercise.

'''


def create_new_candy_data_structure(data):
    """
    Function takes a list of lists. list object always
    contains names at postion 0 and list of candy preferences
    in index 1. function returns ditionary of names as keys and
    values as list of candy preferences
    """
    # friends_candy_preferences = []


    # for i in data:
    #     dict_of_friend = {}
    #     dict_of_friend["name"] = i[0]
    #     dict_of_friend["candy preferences"] = i[1]

    # friends_candy_preferences.append(dict_of_friend)

    # return friends_candy_preferences

    friends_candy_preferences_dict = {}

    for i in data:
        friends_candy_preferences_dict[i[0]] = i[1]

    return friends_candy_preferences_dict

def get_friends_who_like_specific_candy(data, candy_name):
    """
    function takes data, dictionary,keys are names and values are candy preferences
    returns list of names that like candy_name. takes two args dict and candyname
    """
    list_of_friends_that_like_candyname = []

    for friend in data:
        if candy_name in data[friend]:
            list_of_friends_that_like_candyname.append(friend) 

    return list_of_friends_that_like_candyname

def create_candy_set(data):
    
    candy_set = set()

    for key,value in data.items():
        candy_set.update(value)

    return candy_set