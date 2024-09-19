from colorama import Fore, Style
from tabulate import tabulate

# Header for the table
header = ('Price', 'Calories', 'Beneficials', 'Quantity', 'Reference', 'Weight', 'Freshness', 'Expiracy', 'AGGREGATE Values')

# Data for the table (note: replaced 'wheight' typo with 'weight')
meals = [
    ('yogurt', 'cereals', 'white meat', 'milk', 'vegetables', 'fruits', 'no white bread', 'potatoes boiled', 'AGGREGATE_VALUE')
]

# Table display
print(Fore.GREEN + "Meals Information Table" + Style.RESET_ALL)
print(tabulate(meals, headers=header, tablefmt='fancy_grid'))
