import wx

from template_frame import MyFrame1 as MyFrame


class MainFrame(MyFrame):
    def __init__(self):
        super().__init__(None)

        self.Layout()
        self.Show(True)

if __name__ == "__main__":
    app = wx.App()
    frame = MainFrame()
    app.MainLoop()