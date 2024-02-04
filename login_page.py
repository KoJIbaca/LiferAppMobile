from kivy.animation import Animation
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivymd.uix.button import MDButtonText, MDButton
from kivymd.uix.dialog import MDDialog, MDDialogButtonContainer, MDDialogHeadlineText, MDDialogSupportingText
from kivymd.uix.menu import MDDropdownMenu


Builder.load_file('kv/login_page.kv')


class LoginPage(Screen):
    # dialog = None

    def config_button_click(self):
        menu_items = [
            {'text': 'О приложении', 'on_release': lambda x=f"Item_1": self.show_info_dialog()},
            {'text': 'Обратная связь', 'on_release': lambda x=f"Item_2": self.feedback_page_open()},
            {'text': 'Контакты', 'on_release': lambda x=f"Item_3": self.contacts_page_open()},
        ]

        self.cfg_menu = MDDropdownMenu(caller=self.ids.cfg, items=menu_items)
        self.cfg_menu.open()

    def show_info_dialog(self):
        MDDialog(
            MDDialogHeadlineText(text='Информация о приложении'),
            MDDialogSupportingText(text="Название: Моё творчество\n" \
                 "Версия: pre-alpha\n" \
                 "Build: 0.0.01.24\n" \
                 "Автор: Максим Игрок aka Lonsdeilit\n" \
                 "Логотип от logturnal на Freepik"),
            # MDDialogButtonContainer(
            #     Widget(),
            #     MDButton(
            #         MDButtonText(text="Ok"),
            #         style="text",
            #         on_release=MDDialog.dismiss()
            #     ),
            # ),
        ).open()
        self.cfg_menu.dismiss()

    def feedback_page_open(self):
        self.manager.current = 'feedback_page'
        self.manager.transition.direction = 'right'
        self.cfg_menu.dismiss()

    def contacts_page_open(self):
        self.manager.current = 'contacts_page'
        self.manager.transition.direction = 'right'
        self.cfg_menu.dismiss()

    def registration_button(self, instance):
        animation_back = Animation(pos_hint={'center_x': .7, 'center_y': .7}, size=(80, 80), t='out_quint', duration=0.5)
        animation_back.start(instance)

    def authorization_button(self, instance):
        animation_back = Animation(pos_hint={'center_x': .3, 'center_y': .7}, size=(80, 80), t='out_quint', duration=0.5)
        animation_back.start(instance)

    def registration_form_transition(self, widget_list_1: list, widget_list_2: list):
        for (elem_1, elem_2) in zip(widget_list_1, widget_list_2):
            pos_x1, pos_x2 = elem_1.pos_hint['center_x'] - 1.0, elem_2.pos_hint['center_x'] - 1.0
            pos_y1, pos_y2 = elem_1.pos_hint['center_y'], elem_2.pos_hint['center_y']
            anim_1 = Animation(pos_hint={'center_x': pos_x1, 'center_y': pos_y1}, duration=0.5)
            anim_2 = Animation(pos_hint={'center_x': pos_x2, 'center_y': pos_y2}, duration=0.5)
            anim_1.start(elem_1), anim_2.start(elem_2)

    def authorization_form_transition(self, widget_list_1: list, widget_list_2: list):
        for (elem_1, elem_2) in zip(widget_list_1, widget_list_2):
            pos_x1, pos_x2 = elem_1.pos_hint['center_x'] + 1.0, elem_2.pos_hint['center_x'] + 1.0
            pos_y1, pos_y2 = elem_1.pos_hint['center_y'], elem_2.pos_hint['center_y']
            anim_1 = Animation(pos_hint={'center_x': pos_x1, 'center_y': pos_y1}, duration=0.5)
            anim_2 = Animation(pos_hint={'center_x': pos_x2, 'center_y': pos_y2}, duration=0.5)
            anim_1.start(elem_1), anim_2.start(elem_2)

    def login_button_press(self, registration_elements: list):
        for element in registration_elements:
            element.opacity = 0
        self.manager.current = 'profile_page'
        self.manager.transition.direction = 'left'

    def forgot_password_button_click(self, registration_elements: list):
        for element in registration_elements:
            element.opacity = 0
        self.manager.current = 'forgot_password_page'
        self.manager.transition.direction = 'left'
