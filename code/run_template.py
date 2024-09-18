import wx.grid
import pandas as pd
import re

import matplotlib
matplotlib.use('WXAgg')

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
import matplotlib.pyplot as plt

EVEN_ROW_COLOUR = '#CCE6FF'
GRID_LINE_COLOUR = '#ccc'

df = pd.read_csv('Food_Nutrition_Dataset.csv')

from template_frame import MyFrame1 as MyFrame

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


class MyMainFrame(MyFrame):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.meal_plan = {}
        self.selected_meal_food = ""
        self.ml = pd.DataFrame(list(self.meal_plan.items()), columns=['Food', 'Quantity'])

        self.table = DataTable(self.ml)
        self.m_grid1.SetTable(self.table, takeOwnership=True)
        self.m_grid1.AutoSize()
        self.Show(True)

        self.Layout()
        self.Show(True)

    def display_nutritional_info(self, event):
        food_name = self.m_textCtrlSearch.GetValue()
        food_name = food_name.lower()
        result = self.get_nutritional_info(food_name)
        if result == {}:
            wx.MessageBox("Food item not found or has no nutritional information.", "Error", wx.OK | wx.ICON_ERROR)
            return

        self.m_staticTextTitle.SetLabel(food_name.capitalize())
        self.m_richText2.SetValue(f'Caloric Value: {result.get("Caloric Value")}     Fat: {result.get("Fat")}     Vitamin D: {result.get("Vitamin D")}     Selenium: {result.get("Selenium")}     '
                                  f'Saturated Fats: {result.get("Saturated Fats")}     Monounsaturated Fats: {result.get("Monounsaturated Fats")}      Vitamin E: {result.get("Vitamin E")}     '
                                  f'Zinc: {result.get("Zinc")}     Polyunsaturated Fats: {result.get("Polyunsaturated Fats")}     Carbohydrates: {result.get("Carbohydrates")}     '
                                  f'Vitamin K: {result.get("Vitamin K")}     Density: {result.get("Nutrition Density")}     Sugars: {result.get("Sugars")}     Protein: {result.get("Protein")}     '
                                  f'Calcium: {result.get("Calcium")}     Dietary Fiber: {result.get("Dietary Fiber")}     Cholesteral: {result.get("Cholesterol")}     Copper: {result.get("Copper")}     '
                                  f'Sodium: {result.get("Sodium")}     Water: {result.get("Water")}     Iron: {result.get("Iron")}     Vitamin A: {result.get("Vitamin A")}     Vitamin B1: {result.get("Vitamin B1")}     '
                                  f"Magnesium: {result.get('Magnesium')}      Vitamin B12: {result.get('Vitamin B12')}      Vitamin B2: {result.get('Vitamin B2')}       Manganese: {result.get('Manganese')}"
                                  f"     Vitamin B3: {result.get('Vitamin B3')}     Vitamin B5: {result.get('Vitamin B5')}      Phosphorus: {result.get('Phosphorus')}      Vitamin B6: {result.get('Vitamin B6')}        "
                                  f"Vitamin C: {result.get('Vitamin C')}     Potassium: {result.get('Potassium')}")

        self.Layout()

    def search_food_by_name(self, name):
        found = name in df['food'].values
        return found

    def get_nutritional_info(self, name):
        if not self.search_food_by_name(name):
            return {}
        food_row = df[df['food'] == name].iloc[0]
        nutritional_info = food_row.to_dict()
        nutritional_info.pop('food', None)
        return nutritional_info

    def display_charts(self, event):
        food_name = self.m_textCtrl3.GetValue().lower()
        nutritional_info = self.get_nutritional_info(food_name)
        self.m_staticText58.SetLabel(food_name.capitalize())

        if not nutritional_info:
            wx.MessageBox("Food item not found or has no nutritional information.", "Error", wx.OK | wx.ICON_ERROR)
            return

        filtered_nutritional_info = {k: v for k, v in nutritional_info.items() if v != 0.0}

        categories = list(filtered_nutritional_info.keys())
        sizes = list(filtered_nutritional_info.values())

        fig, ax = plt.subplots(1, 2, figsize=(8, 4))
        ax1, ax2 = ax

        max_slices = 8
        if len(categories) > max_slices:
            sorted_items = sorted(zip(categories, sizes), key=lambda x: x[1], reverse=True)
            large_items = sorted_items[:max_slices]
            other_items = sorted_items[max_slices:]
            filtered_categories = [item[0] for item in large_items] + ['Others']
            filtered_sizes = [item[1] for item in large_items] + [sum(item[1] for item in other_items)]
        else:
            filtered_categories = categories
            filtered_sizes = sizes

        explode = [0.1] + [0.0] * (len(filtered_categories) - 1)
        if len(explode) != len(filtered_categories):
            explode = [0.0] * len(filtered_categories)

        ax1.pie(filtered_sizes, labels=filtered_categories, autopct="%1.1f%%", explode=explode,
                textprops={'fontsize': 5}, shadow=True)

        ax2.bar(filtered_categories, filtered_sizes, color=['blue', 'green', 'red', 'purple'])
        ax2.set_xlabel('Nutrients', fontsize=6)
        ax2.set_ylabel('Values', fontsize=8)
        plt.yticks(rotation=0)
        plt.xticks(rotation=45, ha='right')

        plt.tight_layout()

        h, w = self.m_panelFoodInfo.GetSize()
        fig.set_size_inches(h / fig.get_dpi(), w / fig.get_dpi())

        canvas = FigureCanvasWxAgg(self.m_panelFoodInfo, -1, fig)
        canvas.SetSize((h, w))
        self.Layout()

    def filter_food_by_nutrition_range(self, event):
        nutrient = self.m_choiceNutrientRange.GetStringSelection()

        #min & max values
        min_val = float(self.m_textCtrlMinVal.GetValue())
        max_val = float(self.m_textCtrlMaxVal.GetValue())

        df_1 = df[(df[nutrient] >= min_val) & (df[nutrient] <=max_val)]

        tabel = DataTable(df_1)
        self.m_gridRangeFilter.ClearGrid()
        self.m_gridRangeFilter.SetTable(tabel, True)
        self.m_gridRangeFilter.AutoSize()
        self.Layout()

    def display_meal_plan(self, event):
        food_name = self.m_textCtrl9.GetValue().lower()
        quantity = self.m_textCtrl8.GetValue()

        try:
            quantity = int(quantity.strip())
            nutritional_info = self.get_nutritional_info(food_name)
            if not nutritional_info:
                wx.MessageBox("Food item not found or has no nutritional information.", "Error", wx.OK | wx.ICON_ERROR)
                return

            self.generate_meal_plan(food_name, quantity)
            total_calories = self.generate_total_calories()
            self.m_staticText38.SetLabel(f"{total_calories}")

            self.m_grid1.ClearGrid()
            self.ml = pd.DataFrame(list(self.meal_plan.items()), columns=['Food', 'Quantity'])
            self.table = DataTable(self.ml)
            self.m_grid1.SetTable(self.table, takeOwnership=True)
            self.m_grid1.AutoSize()
            self.m_grid1.ForceRefresh()

            self.Show(True)

        except ValueError:
            wx.MessageBox("Please enter a valid number for quantity.", "Error", wx.OK | wx.ICON_ERROR)
            return

    def display_food(self, event):
        food_name = self.m_textCtrl10.GetValue().strip().lower()
        if not food_name:
            wx.MessageBox("Please enter a food name to search.", "Error", wx.OK | wx.ICON_ERROR)
            return

        meal_found = False
        if food_name in [key.lower() for key in self.meal_plan.keys()]:
            meal_found = True

        if meal_found:
            food_key = [key for key in self.meal_plan.keys() if key.lower() == food_name][0]  # Get original name
            quantity = self.meal_plan[food_key]
            food_row = df[df['food'].str.strip().str.lower() == food_name]
            if not food_row.empty:
                caloric_value = food_row.iloc[0]['Caloric Value']
                total_calories = caloric_value * quantity

                self.m_staticText43.SetLabel(f"{food_name}")
                self.m_staticText47.SetLabel(f"     {quantity}  ")
                self.m_staticText44.SetLabel(f"  {total_calories} calories")
                self.selected_meal_food = food_name


    def generate_meal_plan(self, name, quantity):
        if name in self.meal_plan:
            self.meal_plan[name] += quantity
        else:
            self.meal_plan[name] = quantity

        return name, quantity


    def generate_total_calories(self):
        c_total = 0
        for key, value in self.meal_plan.items():
            food_row = df[df['food'] == key].iloc[0]
            caloric_value = food_row['Caloric Value']
            c_total += caloric_value * value

        return c_total

    def remove_food_from_meal_plan(self, event):
        del self.meal_plan[self.selected_meal_food]

        self.m_grid1.ClearGrid()
        self.ml = pd.DataFrame(list(self.meal_plan.items()), columns=['Food', 'Quantity'])
        self.table = DataTable(self.ml)
        self.m_grid1.SetTable(self.table, takeOwnership=True)
        self.m_grid1.AutoSize()
        self.m_grid1.ForceRefresh()

        self.Show(True)



if __name__ == "__main__":
    app = wx.App()
    frame = MyMainFrame()
    app.MainLoop()

