import pandas as pd

df = pd.read_csv('Food_Nutrition_Dataset.csv')

def search_food_by_name(food_name):
    result = df[df['food'] == food_name]
    if result.empty:
        return False
    else:
        return result


