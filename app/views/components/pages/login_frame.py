import wx

from app.controllers.session_controler import SessionController
from app.mixins.has_errors import has_errors
from app.mixins.form_layout import FormLayout
from app.views.components.pages.home import HomeFrame

class LoginFrame(wx.Frame, FormLayout):
    def __init__(self, parent, on_register_callback, on_home_callback):
        super().__init__(parent, title="Inicio de Sesión", size=(800, 500))
        self.on_register_callback = on_register_callback
        self.on_home_callback = on_home_callback
        self.SetBackgroundColour(wx.Colour(255, 255, 255))

        sizer = wx.BoxSizer(wx.VERTICAL)

        sizer.Add(wx.StaticText(self, label="Usuario"), 0, wx.ALL, 5)
        self.user_input = wx.TextCtrl(self)
        self.username_error = wx.StaticText(self, label="")
        self.username_error.SetForegroundColour(wx.Colour(255, 0, 0))
        sizer.Add(self.user_input, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.username_error, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM, 5)

        sizer.Add(wx.StaticText(self, label="Contraseña"), 0, wx.ALL, 5)
        self.password_input = wx.TextCtrl(self, style=wx.TE_PASSWORD)
        self.password_error = wx.StaticText(self, label="")
        self.password_error.SetForegroundColour(wx.Colour(255, 0, 0))
        sizer.Add(self.password_input, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.password_error, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM, 5)

        self.login_btn = wx.Button(self, label="Ingresar")
        self.register_btn = wx.Button(self, label="Registrarse")
        sizer.Add(self.login_btn, 0, wx.ALL | wx.CENTER, 10)
        sizer.Add(self.register_btn, 0, wx.ALL | wx.CENTER, 5)

        self.SetSizer(sizer)

        self.register_btn.Bind(wx.EVT_BUTTON, self.on_register)
        self.login_btn.Bind(wx.EVT_BUTTON, self.verify_login)

    def on_register(self, event):
        self.Hide()
        self.on_register_callback()

    def verify_login(self, event):
        session = SessionController()
        data = session.login(
            username=self.user_input.GetValue(),
            password=self.password_input.GetValue()
        )
        if has_errors(data):
            print(data)
            self.invalid(data)
        else:
            self.valid(data)
    
    def valid(self, data):
        self.Hide()
        home = HomeFrame(None, "Ventana Principal")
        home.Show()
