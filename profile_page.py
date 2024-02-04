from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.effects.scroll import ScrollEffect
from kivy.uix.scrollview import ScrollView

Builder.load_file('kv/profile_page.kv')


class ProfilePage(Screen):

    def back_to_login_page(self):
        self.manager.current = 'login_page'
        self.manager.transition.direction = 'right'
        self.manager.get_screen('login_page').ids.registration_widget.opacity = 1
        self.manager.get_screen('login_page').ids.mail.opacity = 1
        self.manager.get_screen('login_page').ids.reg_login.opacity = 1
        self.manager.get_screen('login_page').ids.reg_password.opacity = 1
        self.manager.get_screen('login_page').ids.registration_button.opacity = 1
        self.manager.get_screen('forgot_password_page').ids.warning_label.opacity = 0

    def age(self):
        age = '28'
        return age

    def friends_number(self):
        friends_num = '15'
        return friends_num

    def friends_page_open(self):
        self.manager.current = 'friends_list_page'
        self.manager.transition.direction = 'left'

