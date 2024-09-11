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

        self.Layout()
        self.Show(True)

    def display_nutritional_info(self, event):
        food_name = self.m_textCtrlSearch.GetValue()
        food_name = food_name.lower()
        result = self.get_nutritional_info(food_name)
        if result == {}:
            wx.MessageBox("Food item not found or has no nutritional information.", "Error", wx.OK | wx.ICON_ERROR)
            return

        self.m_staticTextTitle.SetLabel(food_name)

        self.m_staticCaloricValue.SetLabel(f'Caloric Value: {result.get("Caloric Value")}')
        self.m_staticFat.SetLabel(f"Fat: {result.get('Fat')}")
        self.VitaminD.SetLabel(f"Vitamin D: {result.get('Vitamin D')}")
        self.Selenium.SetLabel(f"Selenium: {result.get('Selenium')}")

        self.m_staticSaturatedFats.SetLabel(f'Saturated Fats: {result.get("Saturated Fats")}')
        self.m_staticMonounFats.SetLabel(f'Monounsaturated Fats: {result.get("Monounsaturated Fats")}')
        self.VitaminE.SetLabel(f'Vitamin E: {result.get("Vitamin E")}')
        self.Zinc.SetLabel(f'Zinc: {result.get("Zinc")}')

        self.m_staticPolyFats.SetLabel(f'Polyunsaturated Fats: {result.get("Polyunsaturated Fats")}')
        self.m_staticCarbs.SetLabel(f'Carbohydrates: {result.get("Carbohydrates")}')
        self.VitaminK.SetLabel(f"Vitamin K: {result.get('Vitamin K')}")
        self.Density.SetLabel(f"Density: {result.get('Nutrition Density')}")

        self.m_staticSugars.SetLabel(f"Sugars: {result.get('Sugars')}")
        self.m_staticProtein.SetLabel(f"Protein: {result.get('Protein')}")
        self.Calcium.SetLabel(f'Calcium: {result.get("Calcium")}')

        self.m_DietaryFiber.SetLabel(f'Dietary Fiber: {result.get("Dietary Fiber")}')
        self.m_Cholesterol.SetLabel(f'Cholesteral: {result.get("Cholesterol")}')
        self.Copper.SetLabel(f'Copper: {result.get("Copper")}')

        self.m_Sodium.SetLabel(f"Sodium: {result.get('Sodium')}")
        self.m_Water.SetLabel(f"Water: {result.get('Water')}")
        self.Iron.SetLabel(f"Iron: {result.get('Iron')}")

        self.VitaminA.SetLabel(f"Vitamin A: {result.get('Vitamin A')}")
        self.VitaminB1.SetLabel(f"Vitamin B1: {result.get('Vitamin B1')}")
        self.Magnesium.SetLabel(f'Magnesium: {result.get("Magnesium")}')

        self.VitaminB12.SetLabel(f"Vitamin B12: {result.get('Vitamin B12')}")
        self.VitaminB2.SetLabel(f"Vitamin B2: {result.get('Vitamin B2')}")
        self.Manganese.SetLabel(f"Manganese: {result.get('Manganese')}")

        self.VitaminB3.SetLabel(f"Vitamin B3: {result.get('Vitamin B3')}")
        self.VitaminB5.SetLabel(f"Vitamin B5: {result.get('Vitamin B5')}")
        self.Phosphorus.SetLabel(f"Phosphorus: {result.get('Phosphorus')}")

        self.VitaminB6.SetLabel(f"Vitamin B6: {result.get('Vitamin B6')}")
        self.VitaminC.SetLabel(f"Vitamin C: {result.get('Vitamin C')}")
        self.Potassium.SetLabel(f"Potassium: {result.get('Potassium')}")


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

    def create_pie_chart(self, event):
        nutritional_info = self.get_nutritional_info(self)
        if not nutritional_info:
            wx.MessageBox("Food item not found or has no nutritional information.", "Error", wx.OK | wx.ICON_ERROR)
            return
        categories = list(nutritional_info.keys())
        sizes = list(nutritional_info.values())

        # Create the pie chart
        fig, ax = plt.subplots(1, 1, figsize=(4, 4))

        # Create explode list with same length as categories
        explode = [0.1] + [0.0] * (len(categories) - 1)

        # Ensure explode list length matches number of slices
        if len(explode) != len(categories):
            explode = [0.0] * len(categories)  # No explosion if lengths mismatch

        ax.pie(sizes, labels=categories, autopct="%1.1f%%", shadow=True, explode=explode)
        ax.set_title("Nutritional Information Pie Chart")

        # Adjust figure size based on panel size
        h, w = self.m_panelFoodInfo.GetSize()
        fig.set_size_inches(h / fig.get_dpi(), w / fig.get_dpi())
        canvas = FigureCanvasWxAgg(self.m_panelFoodInfo, -1, fig)
        canvas.SetSize((h, w))
        self.Layout()



if __name__ == "__main__":
    app = wx.App()
    frame = MyMainFrame()
    app.MainLoop()

