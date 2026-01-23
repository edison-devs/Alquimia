from app.seeders.sedeers import seeders, seed_roles, seed_default_user
from app.controllers.user_controller import UserController
from app.controllers.session_controler import SessionController
import wx
from app.views.components.my_app import MyApp

def init():
    app = MyApp(False)
    app.MainLoop()
    
def simple_test():
    session_controller = SessionController()
    result = session_controller.logout(user_id=int(input("Enter user ID to logout: ")))
    print(result)

commands = {
    "test": simple_test,
    "init": init,
    "seeders": seeders,
    "seed_roles": seed_roles,
    "seed_default_user": seed_default_user,
}
