import pytest
from candy_problem.main import * 


def test_create_candy_data_structure_type():
    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop”, “bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]

    # Act
    new_candy_data = create_new_candy_data_structure(friend_favorites)
    
    # Assert
    assert type(new_candy_data) == dict

def test_create_new_candy_data_structure_length():
    #Arrange
    friend_favorites = [
        ["Sally", [ "lollipop”, “bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]

    #Act
    new_candy_data = create_new_candy_data_structure(friend_favorites)

    #Assert
    assert len(new_candy_data) == len(friend_favorites)



def test_create_candy_data_structure_values():

    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop”, “bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]

    # Act
    new_candy_data = create_new_candy_data_structure(friend_favorites)
    
    # Assert
    assert type(new_candy_data.values) == list

def test_get_friends_who_like_specific_candy_returns_list_of_friends_that_like_lollipop():

    #Arrange
    friends_favorites_dict = {
        'Sally': ['lollipop', 'bubble gum', 'laffy taffy'],
        'Bob': ['milky way', 'licorice', 'lollipop'],
        'Arlene': ['chocolate bar', 'milky way', 'laffy taffy'],
        'Carlie': ['nerds', 'sour patch kids', 'laffy taffy']
    }

    #Act
    list_of_friends_that_like_lollipop = get_friends_who_like_specific_candy(friends_favorites_dict, "lollipop")

    #Assert
    assert "Sally" in list_of_friends_that_like_lollipop
    assert "Bob" in list_of_friends_that_like_lollipop
    assert len(list_of_friends_that_like_lollipop) == 2
def test_create_candy_set_type():

    # Arrange
    friends_favorites_dict = {
        'Sally': ['lollipop', 'bubble gum', 'laffy taffy'],
        'Bob': ['milky way', 'licorice', 'lollipop'],
        'Arlene': ['chocolate bar', 'milky way', 'laffy taffy'],
        'Carlie': ['nerds', 'sour patch kids', 'laffy taffy']
    }

    #Act
    new_candy_data = create_candy_set(friends_favorites_dict)

    #Assert
    assert type(new_candy_data) == set