import wx
from app.views.components.pages.login_frame import LoginFrame
from app.views.components.pages.register_frame import RegisterFrame
from app.views.components.pages.home import HomeFrame
from app.controllers.session_controler import SessionController
from app.mixins.has_errors import has_errors

class MyApp(wx.App):
    def OnInit(self):
        self.login_frame = LoginFrame(None, self.show_register, self.show_home)
        self.register_frame = RegisterFrame(None, self.show_login)
        self.check_session_and_redirect()
        return True

    def show_register(self):
        self.login_frame.Hide()
        self.register_frame.Show()

    def show_login(self):
        self.register_frame.Hide()
        self.login_frame.Show()
    
    def show_home(self):
        self.login_frame.Hide()
        home = HomeFrame(None, "Ventana Principal")
        home.Show()
        
    def check_session_and_redirect(self):
        result = SessionController().validate_activate_session()
        if has_errors(result):
            self.show_login()
        else:
            self.show_home()





