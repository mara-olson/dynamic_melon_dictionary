
# STARTING OFF THE ASSIGNMENT:
# I want to create a dictionary for each melon type with keys:
#     name
#     seeds
#     price
# and also add these new keys with empty values: 
#     flesh color
#     rind color
#     average weight 
# And then also be able to add additional keys as they arise, such as:
#     source


from melons import melons_dict


# PREVIOUS INPUT, TO BE REPLACED WITH MORE EFFICIENT CODE THAT ALLOWS NEW ATTRIBUTES TO BE ADDED
# def print_melon(name, seedless, price):
#     """Print each melon with corresponding attribute information."""

#     have_or_have_not = 'have'
#     if seedless:
#         have_or_have_not = 'do not have'

#     print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}')




def print_melon(dictionary):
"""Print out all the melons in our inventory.""" 
    for melon_name, traits in dictionary.items():
    """For each melon in the dictionary..."""
        for trait, value in traits.items():
        """Access the trait & its value for each melon..."""
            print(f'{trait}: {value}')

       
    
print_melon(melons_dict)