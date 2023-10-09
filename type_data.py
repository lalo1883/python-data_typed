from typing import List, Set, Dict

# To define a type we can use the following syntax
number: int = 19


# Function using types
# With this type of functions, we can define the type of data we expect to receive in the parameters
# And the type of data that we expect to return.
def type_function(num: float) -> float:
    return num + 1


# List using types
# Python also accepts type on structures like lists, dictionaries, etc.
number_list: List[int] = [1, 2, 3]


# Set using types
number_set: Set[int] = {1, 2, 3}


# Dictionary using types
number_dictionary: Dict[int, str] = {
    1: 'One',
    2: 'Two'
}

