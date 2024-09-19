import wx.grid
import pandas as pd

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

def search_food_by_name(name):
    df = pd.read_csv('Food_Nutrition_Dataset.csv')
    found = name in df['food'].values
    return found

def get_nutritional_info(name):
    df = pd.read_csv('Food_Nutrition_Dataset.csv')
    if not search_food_by_name(name):
        return {}
    food_row = df[df['food'] == name].iloc[0]
    nutritional_info = food_row.to_dict()
    nutritional_info.pop('food', None)
    return nutritional_info

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