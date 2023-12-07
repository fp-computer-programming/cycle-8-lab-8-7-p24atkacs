"""
Create a Python file named lab_8-7.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Using the nested list rows from the "Nested Data" slide, write a function that prints each person's name 
BONUS: Make each name be possessive. Remember, if a name ends in s, only add an apostrophe. If the name does not end in s, add, 's.

"""
# Author: Andrew Tkacs

def print_possessive_names(rows):
    """
    Prints each person's name in possessive form.
    
    Args:
    - rows (list): Nested list containing person details with names.
    """
    for row in rows:
        name = row[0]

        # Check if the name ends with 's' to determine the possessive form
        possessive_name = name + ("'" if name.endswith('s') else "'s")

        # Print the possessive name
        print(possessive_name)

# Example usage with nested data
nested_data = [
    ["John", 25, "Engineer"],
    ["Alice", 30, "Doctor"],
    ["James", 22, "Student"],
    ["Charles", 28, "Artist"],
]

# Call the function with the provided nested data
print_possessive_names(nested_data)