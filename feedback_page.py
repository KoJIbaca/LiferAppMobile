from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen

Builder.load_file('kv/feedback_page.kv')


class FeedbackPage(Screen):

    def back_to_login_page(self):
        self.manager.current = 'login_page'
        self.manager.transition.direction = 'left'

    def send_report_button(self):
        name = self.ids.reporter_name.text or ''
        email = self.ids.feedback_email.text or ''
        theme = self.ids.feedback_theme.text or ''
        report = self.ids.feedback_text.text or ''

        '''Появление и исчезновение Popup'а о подтверждении фидбека'''
        popup_content = Label(text='Ваша заявка принята!\nОжидайте ответа на указанный Вами адрес')
        popup = Popup(title='Подтверждение', content=popup_content, size_hint=(None, None), size=(340, 180))
        popup.open()
        Clock.schedule_once(lambda x: popup.dismiss(), 2)

        """Создание основного тела заявки"""
        report_body = {}
        report_names = ['name', 'email', 'theme', 'report']
        report_values = [name, email, theme, report]
        list(map((lambda key, val: report_body.update({f'{key}': val})), report_names, report_values))
        print(report_body)

        """Очистка полей формы"""
        self.ids.reporter_name.text = ''
        self.ids.feedback_email.text = ''
        self.ids.feedback_theme.text = ''
        self.ids.feedback_text.text = ''

        self.back_to_login_page()
