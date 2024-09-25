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

df = load_data('Food_Nutrition_Dataset.csv')

class MyMainFrame(MyFrame):
    def __init__(self, parent=None):
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
        food_name = self.m_textCtrlSearch.GetValue().strip().lower()
        result = get_nutritional_info(food_name)
        if not result:
            wx.MessageBox("Food item not found or has no nutritional information.", "Error", wx.OK | wx.ICON_ERROR)
            return

        self.m_staticTextTitle.SetLabel(food_name.capitalize())

        df_nutritional_info = pd.DataFrame(result.items(), columns=['Nutrient', 'Value'])

        table = DataTable(df_nutritional_info)
        self.m_grid4.ClearGrid()
        self.m_grid4.SetTable(table, takeOwnership=True)
        self.m_grid4.AutoSize()
        self.Layout()

    def display_charts(self, event):
        food_name = self.m_textCtrl3.GetValue().lower()
        nutritional_info = get_nutritional_info(food_name)
        self.m_staticText58.SetLabel(food_name.capitalize())

        if not nutritional_info:
            wx.MessageBox("Food item not found or has no nutritional information.", "Error", wx.OK | wx.ICON_ERROR)
            return

        fig, ax = plt.subplots(1, 2, figsize=(8, 4))
        ax1, ax2 = ax

        filtered_categories, filtered_sizes, explode = filter_nutritional_info(nutritional_info)
        create_pie_chart(filtered_sizes, filtered_categories, explode, ax1)
        create_bar_graph(filtered_categories, filtered_sizes, ax2)

        plt.tight_layout()

        h, w = self.m_panelFoodInfo.GetSize()
        fig.set_size_inches(h / fig.get_dpi(), w / fig.get_dpi())

        canvas = FigureCanvasWxAgg(self.m_panelFoodInfo, -1, fig)
        canvas.SetSize((h, w))
        self.Layout()

    def display_range(self, event):
        nutrient = self.m_choiceNutrientRange.GetStringSelection()

        min_val_check = self.m_textCtrlMinVal.GetValue().strip()
        max_val_check = self.m_textCtrlMaxVal.GetValue().strip()

        # check to see if min and max inputs are empty
        if not min_val_check:
            wx.MessageBox("Minimum value is not given.", "Error", wx.OK | wx.ICON_ERROR)
            return

        if not max_val_check:
            wx.MessageBox("Maximum value is not given.", "Error", wx.OK | wx.ICON_ERROR)
            return

        # check to see if min and max inputs are numbers
        if min_val_check.isalpha():
            wx.MessageBox("Please enter valid numeric value for minimum.", "Error", wx.OK | wx.ICON_ERROR)
            return
        else:
            min_val = float(min_val_check)  # convert minimum string to float

        if max_val_check.isalpha():
            wx.MessageBox("Please enter valid numeric value for maximum.", "Error", wx.OK | wx.ICON_ERROR)
            return
        else:
            max_val = float(max_val_check)  # convert maximum string to float

        df_display = filter_food_by_nutrient_range(df, nutrient, min_val, max_val)

        table = DataTable(df_display)
        self.m_gridRangeFilter.ClearGrid()
        self.m_gridRangeFilter.SetTable(table, True)
        self.m_gridRangeFilter.AutoSize()
        self.Layout()

    def display_level(self, event):
        nutrient = self.m_choiceNutrientLevel.GetStringSelection()

        if self.m_radioBtnLow.GetValue():
            level = 'Low'
        elif self.m_radioBtnMedium.GetValue():
            level = 'Mid'
        elif self.m_radioBtnHigh.GetValue():
            level = 'High'
        else:
            level = None

        if level == None:
            wx.MessageBox("Please select a nutrient level.", "Error", wx.OK | wx.ICON_ERROR)
            return
        filtered_df = filter_food_by_nutrient_level(df, nutrient, level)

        table = DataTable(filtered_df)
        self.m_gridLevelFilter.ClearGrid()
        self.m_gridLevelFilter.SetTable(table, True)
        self.m_gridLevelFilter.AutoSize()
        self.Layout()

    def display_meal_plan(self, event):
        food_name = self.m_textCtrl9.GetValue().lower()
        quantity = self.m_textCtrl8.GetValue()

        try:
            quantity = int(quantity.strip())
            nutritional_info = get_nutritional_info(food_name)
            if not nutritional_info:
                wx.MessageBox("Food item not found or has no nutritional information.", "Error", wx.OK | wx.ICON_ERROR)
                return

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
            wx.MessageBox("Please enter a valid number for quantity.", "Error", wx.OK | wx.ICON_ERROR)
            return

    def display_food(self, event):
        food_name = self.m_textCtrl10.GetValue().strip().lower()
        if not food_name:
            wx.MessageBox("Please enter a food name to search.", "Error", wx.OK | wx.ICON_ERROR)
            return

        food_key, quantity, total_calories = get_food_details(df, food_name, self.meal_plan)

        if food_key:
            self.m_staticText43.SetLabel(f"{food_key}")
            self.m_staticText47.SetLabel(f"     {quantity}  ")
            self.m_staticText44.SetLabel(f"  {total_calories} calories")
            self.selected_meal_food = food_name
        else:
            wx.MessageBox("Food item not found in the meal plan.", "Error", wx.OK | wx.ICON_ERROR)

    def display_removed_food(self, event):
        remove_food_from_meal_plan(self.meal_plan, self.selected_meal_food)
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

