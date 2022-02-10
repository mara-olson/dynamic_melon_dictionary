"""Print out all the melons in our inventory."""


from math import remainder
from turtle import color, window_height
from melons import melon_names, melon_seedlessness, melon_prices


def print_melon(name, seedless, price):
    """Print each melon with corresponding attribute information."""

    have_or_have_not = 'have'
    if seedless:
        have_or_have_not = 'do not have'

    print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}')


for i in melon_names:
    print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])

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
    