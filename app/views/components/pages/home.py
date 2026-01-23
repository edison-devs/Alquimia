import wx 

class HomeFrame(wx.Frame):
    def __init__(self,parent,title):
        super(HomeFrame, self).__init__(parent, title=title, size=(800, 600))

if __name__ == '__main__':
 app=wx.App(False)
 frame=HomeFrame(None, "Ventana Principal")
 frame.Show()
 app.MainLoop()