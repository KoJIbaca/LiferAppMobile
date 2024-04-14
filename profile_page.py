import csv
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

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

    def profile_info(self):
        with open("profile/info.csv", encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter=";")
            for row in file_reader:
                name = row[0].strip()
                surname = row[1].strip()
                location = row[2].strip()
                age = row[3].strip()
        profile_info = [name, surname, location, age]
        return profile_info

    def friends_number(self):
        with open("server/friends.csv", encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file)
            friends_num = sum(1 for row in file_reader)
            print(friends_num)
        return friends_num

    def friends_page_open(self):
        self.manager.current = 'friends_list_page'
        self.manager.transition.direction = 'left'

    def messages_page_open(self):
        self.manager.current = 'messages_page'
        self.manager.transition.direction = 'left'
