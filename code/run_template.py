import wx.grid
import pandas as pd

import matplotlib
matplotlib.use('WXAgg')

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
import matplotlib.pyplot as plt

df = pd.read_csv('Food_Nutrition_Dataset.csv')

from template_frame import MyFrame1 as MyFrame

class MyMainFrame(MyFrame):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.meal_plan = {}

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
        pass

    def display_meal_plan(self, event):
        food_name = self.m_textCtrl51.GetValue()
        quantity = self.m_textCtrl52.GetValue()

        try:
            quantity = int(quantity.strip())
            nutritional_info = self.get_nutritional_info(food_name)
            if not nutritional_info:
                wx.MessageBox("Food item not found or has no nutritional information.", "Error", wx.OK | wx.ICON_ERROR)
                return

            food_name, quantity = self.generate_meal_plan(food_name, quantity)
            total_calories = self.generate_total_calories()
            self.m_staticText59.SetLabel(f"                 {total_calories}")


        except ValueError:
            wx.MessageBox("Please enter a valid number for quantity.", "Error", wx.OK | wx.ICON_ERROR)
            return

    def display_food(self, event):
        pass


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
            c_total = caloric_value * value

        return c_total

    def remove_food_from_meal_plan(self, event):
        food_name = self.m_staticTextAddFood.GetValue()
        del self.meal_plan[food_name]



if __name__ == "__main__":
    app = wx.App()
    frame = MyMainFrame()
    app.MainLoop()

