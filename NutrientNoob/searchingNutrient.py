import csv
import os
import random

# Function for random ingredient list
def search_ingredients_by_nutrient(nutrient):
    csv_file_path = 'NutrientNoob/RAW_nutrition.csv'
    ingredients = []
    
    # Only checking for the first 20 ingredients
    while len(ingredients) < 20:
        rand_row = random.randint(2, 7414)  
        current_row = 1  

        # Open the CSV file and create a CSV reader object
        with open(csv_file_path, 'r') as file:
            csv_reader = csv.DictReader(file)
            
            for row in csv_reader:
                current_row += 1
                if current_row == rand_row:

                    row = {k.strip().lower(): v for k, v in row.items()}
                    nutrient_key = nutrient.strip().lower()
                    
                    # Check if the ingredient includes the nutrient
                    if nutrient_key in row and float(row[nutrient_key]) > 0:
                        # If it includes the nutrient add it to the list
                        ingredients.append(row["description"]) 
                        
                        break
    # Return randomized list of ingredients
    return ingredients

# REPLACE WITH THE DROP DOWN VALUES!!! :)
nutrient = input("Enter a nutrient to search for: ")

# Gets list from function
matching_ingredients = search_ingredients_by_nutrient(nutrient)

# REPLACE!!! Prints on terminal the list of 20 ingredients
if matching_ingredients:
    print(f"20 ingredients containing {nutrient}:")
    for ingredient in matching_ingredients:
        print(ingredient)
else:
    # This will be removed because of the drop down feature
    print(f"No ingredients found containing {nutrient}.")
