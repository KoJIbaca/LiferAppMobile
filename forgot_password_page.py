from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen


Builder.load_file('kv/forgot_password_page.kv')


class ForgotPasswordPage(Screen):

    def back_to_login_page(self):
        self.manager.current = 'login_page'
        self.manager.transition.direction = 'right'
        self.manager.get_screen('login_page').ids.registration_widget.opacity = 1
        self.manager.get_screen('login_page').ids.mail.opacity = 1
        self.manager.get_screen('login_page').ids.reg_login.opacity = 1
        self.manager.get_screen('login_page').ids.reg_password.opacity = 1
        self.manager.get_screen('login_page').ids.registration_button.opacity = 1
        self.ids.warning_label.opacity = 0

    def recover_button_click(self):
        telephone = self.ids.telephone_number.text
        email = self.ids.email.text
        data_list = {'telephone': telephone, 'email': email}
        if telephone.strip() == "" and email.strip() == '':
            self.ids.warning_label.opacity = 1
        else:
            for elem in list(data_list.keys()):
                if data_list[elem] == '':
                    del data_list[elem]

            popup_content = Label(text='Вам высланы инструкции\nна электронную почту!')
            popup = Popup(title='Успешно', content=popup_content, size_hint=(None, None), size=(340, 180))
            popup.open()
            Clock.schedule_once(lambda x: popup.dismiss(), 2)
            self.ids.email.text = ''
            self.ids.telephone_number.text = ''
            self.back_to_login_page()

