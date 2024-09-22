import wx.grid
import pandas as pd
import matplotlib.pyplot as plt

MAX_SLICES = 8
EVEN_ROW_COLOUR = '#CCE6FF'

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

def load_data(file_path):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        raise FileNotFoundError

def search_food_by_name(name):
    df = pd.read_csv('Food_Nutrition_Dataset.csv')
    return name in df['food'].values

def get_nutritional_info(name):
    df = pd.read_csv('Food_Nutrition_Dataset.csv')
    if not search_food_by_name(name):
        return {}
    food_row = df[df['food'] == name].iloc[0]
    nutritional_info = food_row.to_dict()
    nutritional_info.pop('food', None)
    return nutritional_info

def filter_nutritional_info(categories, sizes):
    if len(categories) > MAX_SLICES:
        sorted_items = sorted(zip(categories, sizes), key=lambda x: x[1], reverse=True)
        large_items = sorted_items[:MAX_SLICES]
        other_items = sorted_items[MAX_SLICES:]
        filtered_categories = [item[0] for item in large_items] + ['Others']
        filtered_sizes = [item[1] for item in large_items] + [sum(item[1] for item in other_items)]
    else:
        filtered_categories = categories
        filtered_sizes = sizes

    explode = [0.1] + [0.0] * (len(filtered_categories) - 1)
    if len(explode) != len(filtered_categories):
        explode = [0.0] * len(filtered_categories)

    return filtered_categories, filtered_sizes, explode

def create_pie_chart(filtered_sizes, filtered_categories, explode, ax):
    ax.pie(filtered_sizes, labels=filtered_categories, autopct="%1.1f%%", explode=explode,
            textprops={'fontsize': 5}, shadow=True)
    return ax.pie

def create_bar_graph(filtered_categories, filtered_sizes, ax):
    ax.bar(filtered_categories, filtered_sizes, color='skyblue')
    ax.set_xlabel('Nutrients', fontsize=6)
    ax.set_ylabel('Values', fontsize=8)
    plt.yticks(rotation=0)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    return ax.bar

def filter_food_by_nutrition(df, nutrient, min_val, max_val):
    df_filtered = df[(df[nutrient] >= min_val) & (df[nutrient] <= max_val)]
    df_filtered = df_filtered.sort_values(by='food')
    return df_filtered[['food', nutrient]]

def get_food_details(df, food_name, meal_plan):
    meal_found = False
    if food_name in [key.lower() for key in meal_plan.keys()]:
        meal_found = True

    if meal_found:
        food_key = [key for key in meal_plan.keys() if key.lower() == food_name][0]  # Get original name
        quantity = meal_plan[food_key]
        food_row = df[df['food'].str.strip().str.lower() == food_name]
        if not food_row.empty:
            caloric_value = food_row.iloc[0]['Caloric Value']
            total_calories = caloric_value * quantity
            return food_key, quantity, total_calories
    return None, None, None

def generate_meal_plan(meal_plan, name, quantity):
    if name in meal_plan:
        meal_plan[name] += quantity
    else:
        meal_plan[name] = quantity

    return name, quantity

def generate_total_calories(meal_plan):
    df = pd.read_csv('Food_Nutrition_Dataset.csv')
    c_total = 0
    for key, value in meal_plan.items():
        food_row = df[df['food'] == key].iloc[0]
        caloric_value = food_row['Caloric Value']
        c_total += caloric_value * value

    return c_total

def remove_food_from_meal_plan(meal_plan, selected_meal_food):
    del meal_plan[selected_meal_food]