import wx.grid
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
matplotlib.use('WXAgg')

from template_frame import MyFrame1 as MyFrame
from all_functions import DataTable, load_data, get_nutritional_info, filter_nutritional_info, create_pie_chart, create_bar_graph, filter_food_by_nutrient_range, generate_meal_plan, generate_total_calories, get_food_details, remove_food_from_meal_plan, filter_food_by_nutrient_level

EVEN_ROW_COLOUR = '#CCE6FF'
GRID_LINE_COLOUR = '#ccc'

class MyMainFrame(MyFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.selected_meal_food = ""
        self.selected_quantity = 0
        self.meal_plan = {}
        self.ml = pd.DataFrame(list(self.meal_plan.items()), columns=['Food', 'Quantity'])
        self.df = load_data('Food_Nutrition_Dataset.csv')

        self.table = DataTable(self.ml)
        self.m_grid1.SetTable(self.table, takeOwnership=True)
        self.m_grid1.AutoSize()
        self.Show(True)

        self.Layout()
        self.Show(True)

    def display_nutritional_info(self, event):
        food_name = self.m_textCtrlSearch.GetValue().strip().lower()
        try:
            result = get_nutritional_info(food_name)
            self.m_staticTextTitle.SetLabel(food_name.capitalize())
            df_nutritional_info = pd.DataFrame(result.items(), columns=['Nutrient', 'Value'])
            table = DataTable(df_nutritional_info)
            self.m_grid4.ClearGrid()
            self.m_grid4.SetTable(table, takeOwnership=True)
            self.m_grid4.AutoSize()
            self.Layout()
        except ValueError:
            wx.MessageBox("Error: Not valid input.", "Error", wx.OK | wx.ICON_ERROR)

    def display_charts(self, event):
        food_name = self.m_textCtrl3.GetValue().lower()
        try:
            nutritional_info = get_nutritional_info(food_name)
            self.m_staticText58.SetLabel(food_name.capitalize())
            fig, ax = plt.subplots(1, 2, figsize=(8, 4))
            ax1, ax2 = ax
            filtered_categories, filtered_sizes, explode = filter_nutritional_info(nutritional_info)
            create_pie_chart(filtered_sizes, filtered_categories, explode, ax1)
            create_bar_graph(filtered_categories, filtered_sizes, ax2)
            h, w = self.m_panelFoodInfo.GetSize()
            fig.set_size_inches(h / fig.get_dpi(), w / fig.get_dpi())
            canvas = FigureCanvasWxAgg(self.m_panelFoodInfo, -1, fig)
            canvas.SetSize((h, w))
            self.Layout()
        except ValueError:
            wx.MessageBox("Error: Not valid input.", "Error", wx.OK | wx.ICON_ERROR)

    def display_range(self, event):
        nutrient = self.m_choiceNutrientRange.GetStringSelection()
        min_val = self.m_textCtrlMinVal.GetValue().strip()
        max_val = self.m_textCtrlMaxVal.GetValue().strip()
        try:
            df_display = filter_food_by_nutrient_range(nutrient, float(min_val), float(max_val))
            table = DataTable(df_display)
            self.m_gridRangeFilter.ClearGrid()
            self.m_gridRangeFilter.SetTable(table, True)
            self.m_gridRangeFilter.AutoSize()
            self.Layout()
        except ValueError:
            wx.MessageBox("Error: Not valid input.", "Error", wx.OK | wx.ICON_ERROR)

    def display_level(self, event):
        nutrient = self.m_choiceNutrientLevel.GetStringSelection()
        level = None
        if self.m_radioBtnLow.GetValue():
            level = 'Low'
        elif self.m_radioBtnMedium.GetValue():
            level = 'Mid'
        elif self.m_radioBtnHigh.GetValue():
            level = 'High'
        try:
            filtered_df = filter_food_by_nutrient_level(nutrient, level)
            table = DataTable(filtered_df)
            self.m_gridLevelFilter.ClearGrid()
            self.m_gridLevelFilter.SetTable(table, True)
            self.m_gridLevelFilter.AutoSize()
            self.Layout()
        except ValueError:
            wx.MessageBox("Error: Not valid input.", "Error", wx.OK | wx.ICON_ERROR)

    def display_meal_plan(self, event):
        food_name = self.m_textCtrl9.GetValue().lower().strip()
        quantity = self.m_textCtrl8.GetValue().lower().strip()
        try:
            quantity = int(quantity)
            generate_meal_plan(self.meal_plan, food_name, quantity)
            total_calories = generate_total_calories(self.meal_plan)

            self.m_staticText38.SetLabel(f"{total_calories}")
            self.m_grid1.ClearGrid()
            self.ml = pd.DataFrame(list(self.meal_plan.items()), columns=['Food', 'Quantity'])
            self.table = DataTable(self.ml)
            self.m_grid1.SetTable(self.table, takeOwnership=True)
            self.m_grid1.AutoSize()
            self.m_grid1.ForceRefresh()
            self.Show(True)

        except ValueError:
            wx.MessageBox("Error: Not valid input.", "Error", wx.OK | wx.ICON_ERROR)

    def display_food(self, event):
        food_name = self.m_textCtrl10.GetValue().strip().lower()
        try:
            food_key, quantity, total_calories = get_food_details(food_name, self.meal_plan)
            if food_key:
                self.m_staticText43.SetLabel(f"{food_key}")
                self.m_staticText47.SetLabel(f"     {quantity}  ")
                self.m_staticText44.SetLabel(f"  {total_calories} calories")
                self.selected_meal_food = food_name
                self.selected_quantity = quantity
            else:
                wx.MessageBox("Food item not found in the meal plan.", "Error", wx.OK | wx.ICON_ERROR)
        except ValueError:
            wx.MessageBox("Error: Not valid input.", "Error", wx.OK | wx.ICON_ERROR)

    def display_removed_food(self, event):
        try:
            remove_food_from_meal_plan(self.meal_plan, self.selected_meal_food, self.selected_quantity)
            total_calories = generate_total_calories(self.meal_plan)

            self.m_staticText38.SetLabel(f"{total_calories}")
            self.m_grid1.ClearGrid()
            self.ml = pd.DataFrame(list(self.meal_plan.items()), columns=['Food', 'Quantity'])
            self.table = DataTable(self.ml)
            self.m_grid1.SetTable(self.table, takeOwnership=True)
            self.m_grid1.AutoSize()
            self.m_grid1.ForceRefresh()
            self.Show(True)

            self.m_staticText43.SetLabel("Food")
            self.m_staticText47.SetLabel("Quantity")
            self.m_staticText44.SetLabel("xxxx Calories")
        except KeyError:
            wx.MessageBox("Error: Not valid input.", "Error", wx.OK | wx.ICON_ERROR)

if __name__ == "__main__":
    app = wx.App()
    frame = MyMainFrame()
    app.MainLoop()

