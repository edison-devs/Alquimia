import wx

class PopupDialog:
    def show_message(self, text, title="Mensaje", duration=2000):
        popup = wx.Frame(self, title=title, style=wx.STAY_ON_TOP | wx.FRAME_NO_TASKBAR | wx.BORDER_SIMPLE)
        popup.SetBackgroundColour(wx.Colour(255, 255, 255))
        popup.SetSize((300, 100))
        popup.CenterOnParent()

        sizer = wx.BoxSizer(wx.VERTICAL)
        label = wx.StaticText(popup, label=text)
        label.Wrap(280)
        sizer.Add(label, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 15)
        popup.SetSizer(sizer)

        popup.Show()
        wx.CallLater(duration, popup.Destroy)
