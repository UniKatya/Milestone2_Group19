import wx.grid
import pandas as pd
import matplotlib

matplotlib.use('WXAgg')

df = pd.read_csv('Food_Nutrition_Dataset.csv')

from template_frame import MyFrame1 as MyFrame

class MyMainFrame(MyFrame):
    def __init__(self,parent=None):
        super().__init__(parent)

        self.Layout()
        self.Show(True)

    def search_food_by_name(self, event):
        food_name = self.m_textCtrlSearch.GetValue()
        food_name = food_name.lower()
        result = df[df['food'] == food_name]
        if result.empty:
            display_text = f"There is no such food called {food_name}."
        else:
            display_text = f"{result}"

        self.m_staticTextData.SetLabel(str(display_text))
        self.Layout()


if __name__ == "__main__":
    app = wx.App()
    frame = MyMainFrame()
    app.MainLoop()
