import pandas as pd

df = pd.read_csv('Food_Nutrition_Dataset.csv')

result = df[df['food'] == 'cream cheese']
print(result)

