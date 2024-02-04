from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file('kv/contacts_page.kv')


class ContactsPage(Screen):

    def back_to_login_page(self):
        self.manager.current = 'login_page'
        self.manager.transition.direction = 'left'
