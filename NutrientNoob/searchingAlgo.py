#Here is where our searching algorithms for our nutrition/recipe database will be
# Here is where our searching algorithms for our nutrition/recipe database will be
import csv
import os


# First Attempt at searching ingredient by nutrition
def search_ingredients_by_nutrient(nutrient):
    print("Current working directory:", os.getcwd())
    csv_file_path ='NutrientNoob/RAW_nutrition.csv'
    ingredients = []
    
    # Open the CSV file and create a CSV reader object
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        
        # Iterate over each row in the CSV data
        for row in csv_reader:
            # Normalize header keys to prevent case and whitespace issues
            row = {k.strip().lower(): v for k, v in row.items()}
            nutrient_key = nutrient.strip().lower()
            # Check if the specified nutrient exists and has a non-zero value
            if nutrient_key in row and float(row[nutrient_key]) > 0:
                ingredients.append(row["description"])  # assuming "description" is correct
                
                # Stop searching after finding 20 ingredients
                if len(ingredients) == 20:
                    break
    
    return ingredients

# Get the nutrient input from the user
nutrient = input("Enter a nutrient to search for: ")

# Search for ingredients containing the specified nutrient
matching_ingredients = search_ingredients_by_nutrient(nutrient)

# Print the matching ingredients (up to 20)
if matching_ingredients:
    print(f"First 20 ingredients containing {nutrient}:")
    for ingredient in matching_ingredients:
        print(ingredient)
else:
    print(f"No ingredients found containing {nutrient}.")



# HELLO :)
    
    