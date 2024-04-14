from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from login_page import LoginPage
from forgot_password_page import ForgotPasswordPage
from feedback_page import FeedbackPage
from contacts_page import ContactsPage
from profile_page import ProfilePage
from friends_list_page import FriendsListPage
from messages_page import MessagesPage


screen_list = '''
ScreenManager:
    id: sm
    
    LoginPage:
        id: login_page
        name: 'login_page'
    ForgotPasswordPage:
        id: forgot_password_page
        name: 'forgot_password_page'
    FeedbackPage:
        id: feedback_page
        name: 'feedback_page'
    ContactsPage:
        id: contacts_page     
        name: 'contacts_page'
    ProfilePage:
        id: profile_page     
        name: 'profile_page'   
    FriendsListPage:
        id: friends_list_page  
        name: 'friends_list_page'
    MessagesPage:
        id: messages_page
        name: 'messages_page'  
'''


class LiferApp(MDApp):

    def build(self):
        MDApp.title = "Мое творчество"
        MDApp.icon = "Images/main_logo.png"
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Orange"
        Window.size = (393, 851)
        return Builder.load_string(screen_list)


if __name__ == '__main__':
    LiferApp().run()
