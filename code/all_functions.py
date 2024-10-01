import wx.grid
import pandas as pd
import matplotlib.pyplot as plt

MAX_SLICES = 8
EVEN_ROW_COLOUR = '#CCE6FF'

def load_data(file_path):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        raise FileNotFoundError

df = load_data('Food_Nutrition_Dataset.csv')

def search_food_by_name(food_name):
    global df
    found = food_name in df['food'].values
    return found

def get_nutritional_info(food_name):
    if not food_name or food_name.isdigit() or not search_food_by_name(food_name):
        raise ValueError
    global df
    food_row = df[df['food'] == food_name].iloc[0]
    nutritional_info = food_row.to_dict()
    nutritional_info.pop('food', None)
    return nutritional_info

def filter_nutritional_info(nutritional_info):
    if not nutritional_info:
        raise ValueError
    else:
        filtered_nutritional_info = {k: v for k, v in nutritional_info.items() if v != 0.0}
        categories = list(filtered_nutritional_info.keys())
        sizes = list(filtered_nutritional_info.values())
        sorted_items = sorted(zip(categories, sizes), key=lambda x: x[1], reverse=True)
        large_items = sorted_items[:MAX_SLICES]
        other_items = sorted_items[MAX_SLICES:]
        filtered_categories = [item[0] for item in large_items] + ['Others']
        filtered_sizes = [item[1] for item in large_items] + [sum(item[1] for item in other_items)]

        explode = [0.1] + [0.0] * (len(filtered_categories) - 1)

        return filtered_categories, filtered_sizes, explode

def create_pie_chart(filtered_sizes, filtered_categories, explode, ax):
    if not filtered_sizes or not filtered_categories:
        raise ValueError
    wedges, texts, autotexts = ax.pie(filtered_sizes, labels=filtered_categories, autopct="%1.1f%%", explode=explode,
                                     textprops={'fontsize': 5}, shadow=True)
    return wedges, texts, autotexts

def create_bar_graph(filtered_categories, filtered_sizes, ax):
    if not filtered_categories or not filtered_sizes:
        raise ValueError
    ax.bar(filtered_categories, filtered_sizes, color='skyblue')
    ax.set_xlabel('Nutrients', fontsize=6)
    ax.set_ylabel('Values', fontsize=8)
    plt.yticks(rotation=0)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    return ax.bar

def filter_food_by_nutrient_range(nutrient, min_val, max_val):
    if not min_val or not max_val or min_val >= max_val:
        raise ValueError

    filtered_range = df[(df[nutrient] >= min_val) & (df[nutrient] <= max_val)]
    filtered_range = filtered_range.sort_values(by='food')
    return filtered_range[['food', nutrient]]

def filter_food_by_nutrient_level(nutrient, level):
    if level not in ['Low', 'Mid', 'High']:
        raise ValueError

    max_value = df[nutrient].max()
    low_threshold = max_value * 0.33
    mid_threshold = max_value * 0.66

    if level == 'Low':
        filtered_level = df[df[nutrient] <= low_threshold]
    elif level == 'Mid':
        filtered_level = df[(df[nutrient] > low_threshold) & (df[nutrient] <= mid_threshold)]
    else:
        filtered_level = df[df[nutrient] > mid_threshold]

    filtered_level = filtered_level.sort_values(by='food')
    return filtered_level[['food', nutrient]]

def get_food_details(food_name, meal_plan):
    if not food_name in meal_plan or food_name.isdigit():
        raise ValueError

    food_key = [key for key in meal_plan.keys() if key.lower() == food_name][0]  # Get original name
    quantity = meal_plan[food_key]
    food_row = df[df['food'].str.strip().str.lower() == food_name]
    caloric_value = food_row.iloc[0]['Caloric Value']
    total_calories = caloric_value * quantity
    return food_key, quantity, total_calories

def generate_meal_plan(meal_plan, food_name, quantity):
    if not search_food_by_name(food_name) or quantity <= 0 or quantity > 50:
        raise ValueError

    if food_name in meal_plan:
        meal_plan[food_name] += quantity
    else:
        meal_plan[food_name] = quantity

    return food_name, quantity

def generate_total_calories(meal_plan):
    total_calories = 0
    global df
    if not isinstance(meal_plan, dict):
        raise ValueError
    if not meal_plan:
        return total_calories

    for key, value in meal_plan.items():
        food_row = df[df['food'] == key].iloc[0]
        caloric_value = food_row['Caloric Value']
        total_calories += caloric_value * value

    return total_calories

def remove_food_from_meal_plan(meal_plan, food_name, quantity):
    if food_name not in meal_plan:
        raise KeyError
    if meal_plan[food_name] <= quantity:
        del meal_plan[food_name]
    else:
        meal_plan[food_name] -= quantity

class DataTable(wx.grid.GridTableBase):
    def __init__(self, data=None):
        wx.grid.GridTableBase.__init__(self)
        self.headerRows = 1
        self.data = data

    def GetNumberRows(self):
        return len(self.data.index)

    def GetNumberCols(self):
        return len(self.data.columns)

    def GetValue(self, row, col):
        return self.data.iloc[row, col]

    def SetValue(self, row, col, value):
        self.data.iloc[row, col] = value

    def GetColLabelValue(self, col):
        return self.data.columns[col]

    def GetAttr(self, row, col, prop):
        attr = wx.grid.GridCellAttr()
        if row % 2 == 1:
            attr.SetBackgroundColour(EVEN_ROW_COLOUR)
        return attr