import wx

from app.controllers.user_controller import UserController
from app.mixins.has_errors import has_errors
from app.mixins.form_layout import FormLayout

class RegisterFrame(wx.Frame, FormLayout):
    def __init__(self, parent, on_login_callback):
        super().__init__(parent, title="Registro", size=(800, 600))
        self.on_login_callback = on_login_callback
        self.SetBackgroundColour(wx.Colour(255, 255, 255))

        sizer = wx.BoxSizer(wx.VERTICAL)

        # Nombre
        sizer.Add(wx.StaticText(self, label="Nombre"), 0, wx.ALL, 5)
        self.name_input = wx.TextCtrl(self)
        self.name_error = wx.StaticText(self, label="")
        self.name_error.SetForegroundColour(wx.Colour(255, 0, 0))
        sizer.Add(self.name_input, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.name_error, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM, 5)

        # Apellido
        sizer.Add(wx.StaticText(self, label="Apellido"), 0, wx.ALL, 5)
        self.last_name_input = wx.TextCtrl(self)
        self.last_name_error = wx.StaticText(self, label="")
        self.last_name_error.SetForegroundColour(wx.Colour(255, 0, 0))
        sizer.Add(self.last_name_input, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.last_name_error, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM, 5)

        # Correo electrónico
        sizer.Add(wx.StaticText(self, label="Correo electrónico"), 0, wx.ALL, 5)
        self.email_input = wx.TextCtrl(self)
        self.email_error = wx.StaticText(self, label="")
        self.email_error.SetForegroundColour(wx.Colour(255, 0, 0))
        sizer.Add(self.email_input, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.email_error, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM, 5)

        # Teléfono
        sizer.Add(wx.StaticText(self, label="Teléfono"), 0, wx.ALL, 5)
        self.phone_input = wx.TextCtrl(self)
        self.phone_error = wx.StaticText(self, label="")
        self.phone_error.SetForegroundColour(wx.Colour(255, 0, 0))
        sizer.Add(self.phone_input, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.phone_error, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM, 5)

        # Usuario
        sizer.Add(wx.StaticText(self, label="Usuario"), 0, wx.ALL, 5)
        self.username_input = wx.TextCtrl(self)
        self.username_error = wx.StaticText(self, label="")
        self.username_error.SetForegroundColour(wx.Colour(255, 0, 0))
        sizer.Add(self.username_input, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.username_error, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM, 5)

        # Contraseña
        sizer.Add(wx.StaticText(self, label="Contraseña"), 0, wx.ALL, 5)
        self.password_input = wx.TextCtrl(self, style=wx.TE_PASSWORD)
        self.password_error = wx.StaticText(self, label="")
        self.password_error.SetForegroundColour(wx.Colour(255, 0, 0))
        sizer.Add(self.password_input, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.password_error, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM, 5)

        # Botones
        self.register_btn = wx.Button(self, label="Registrar")
        self.login_btn = wx.Button(self, label="Inicio de Sesión")
        sizer.Add(self.register_btn, 0, wx.ALL | wx.CENTER, 10)
        sizer.Add(self.login_btn, 0, wx.ALL | wx.CENTER, 5)

        self.SetSizer(sizer)

        # Eventos
        self.login_btn.Bind(wx.EVT_BUTTON, self.on_login)
        self.register_btn.Bind(wx.EVT_BUTTON, self.register)

    def on_login(self, event):
        self.Hide()
        self.on_login_callback()

    def register(self, event):
        user_controller = UserController()
        data = user_controller.register(
            name=self.name_input.GetValue(),
            last_name=self.last_name_input.GetValue(),
            email=self.email_input.GetValue(),
            phone=self.phone_input.GetValue(),
            username=self.username_input.GetValue(),
            password=self.password_input.GetValue()
        )
        
        if has_errors(data):
            self.invalid(data)
        else:
            self.valid(data)

    def valid(self, data):
            self.show_message("Usuario registrado con éxito", title="Éxito")
            self.all_clear_inputs()
            self.on_login_callback()

