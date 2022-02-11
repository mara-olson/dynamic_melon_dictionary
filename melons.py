# melon_names = {
#     1: 'Honeydew',
#     2: 'Crenshaw',
#     3: 'Crane',
#     4: 'Casaba',
#     5: 'Cantaloupe',
# }

# melon_prices = {
#     1: 0.99,
#     2: 2.00,
#     3: 2.50,
#     4: 2.50,
#     5: 0.99,
# }

# melon_seedlessness = {
#     1: True,
#     2: False,
#     3: False,
#     4: False,
#     5: False,
# }
# Instead of storing names together, prices together, seedlessness together, I'd like to tie each of these attributes to their corresponding melon. Therefore I will create a dictionary for each melon with these key-value pairs
melons_dict = {
    'Honeydew': {
    'name': 'Honeydew',
    'price': 0.99,
    'seedlessness': True,
    'flesh_color': None,
    'weight': None,
    'rind_color': None,
    },

    'Crenshaw': {
        'name': 'Crenshaw',
        'price': 2.00,
        'seedlessness': False,
        'flesh_color': None,
        'weight': None,
        'rind_color': None,
    },

    'Crane': {
        'name': 'Crane',
        'price': 2.50,
        'seedlessness': False,
        'flesh_color': None,
        'weight': None,
        'rind_color': None,
    },

    'Casaba': {
        'name': 'Casaba',
        'price': 2.50,
        'seedlessness': False,
        'flesh_color': None,
        'weight': None,
        'rind_color': None,
    },

    'Cantaloupe': {
        'name': 'Cantaloupe',
        'price': 0.99,
        'seedlessness': False,
        'flesh_color': None,
        'weight': None,
        'rind_color': None,
    },
}

# melon /s_dict = Honeydew, Crenshaw, Crane, Casaba, Cantaloupe
print(melons_dict)