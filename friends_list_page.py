import csv
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivymd.uix.behaviors import RotateBehavior
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.dialog import MDDialog, MDDialogHeadlineText, MDDialogSupportingText, MDDialogContentContainer, \
    MDDialogButtonContainer
from kivymd.uix.list import (MDListItem, MDListItemHeadlineText, MDListItemLeadingAvatar, MDListItemSupportingText,
                             MDListItemTertiaryText, MDListItemTrailingIcon)
from kivymd.uix.textfield import MDTextField, MDTextFieldLeadingIcon, MDTextFieldHelperText

Builder.load_file('kv/friends_list_page.kv')


class TrailingPressedIconButton(ButtonBehavior, RotateBehavior, MDListItemTrailingIcon):
    ...


class FriendsListPage(Screen):

    def on_enter(self):
        self.ids.friends.active = True
        self.ids.favorite_friends.active = False
        self.friends_list()

    def on_touch_move(self, touch):
        if touch.dx > 15:
            self.manager.transition.direction = 'right'
            self.manager.current = 'profile_page'

    def back_to_profile_page(self):
        self.manager.current = 'profile_page'
        self.manager.transition.direction = 'right'

    def favorite_button_click(self):
        with open("server/friends.csv", encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter=";")
            self.ids.lists.clear_widgets()
            for row in file_reader:
                if row[4].strip() == 'f':
                    self.ids.lists.add_widget(MDListItem(
                        MDListItemLeadingAvatar(source=(row[3]).strip()),
                        MDListItemHeadlineText(text=row[0], theme_text_color='Custom', text_color='black'),
                        MDListItemSupportingText(text=row[1], theme_text_color='Custom', text_color='grey'),
                        MDListItemTertiaryText(text=row[2], theme_text_color='Custom', text_color='black'),
                        TrailingPressedIconButton(icon="email",
                                                  on_release=lambda button,
                                                                    friend=row[0]: self.message_dialog_open(button,
                                                                                                            friend))
                    )
                    )

    def friends_list(self):
        with open("server/friends.csv", encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter=";")
            self.ids.lists.clear_widgets()
            for row in file_reader:
                self.ids.lists.add_widget(MDListItem(
                    MDListItemLeadingAvatar(source=row[3].strip()),
                    MDListItemHeadlineText(id='name', text=row[0], theme_text_color='Custom', text_color='black'),
                    MDListItemSupportingText(text=row[1], theme_text_color='Custom', text_color='grey'),
                    MDListItemTertiaryText(text=row[2], theme_text_color='Custom', text_color='black'),
                    TrailingPressedIconButton(icon="email",
                                              on_release=lambda button, friend=row[0]: self.message_dialog_open(button,
                                                                                                                friend))
                )
                )

    def add_friends_dialog_open(self):
        self.mdtf = MDTextField(
            MDTextFieldLeadingIcon(icon='magnify'),
            MDTextFieldHelperText(text="Helper text"),
            mode="outlined")

        self.search_dialog = MDDialog(
            MDDialogHeadlineText(text='Найти участника соцсети'),
            MDDialogSupportingText(text="Введите имя и фамилию человека"),
            MDDialogContentContainer(self.mdtf),
            MDDialogButtonContainer(
                Widget(),
                MDButton(
                    MDButtonText(text="Отмена"),
                    style="text",
                    on_release=lambda *args: self.search_dialog.dismiss()
                ),
                MDButton(
                    MDButtonText(text="Найти"),
                    style="text",
                    on_release=lambda *args: self.dialog_search_button_click()
                ),
                spacing="8dp",
            ),
        )
        self.search_dialog.open()

    def dialog_search_button_click(self):
        self.search_dialog.dismiss()
        name_value = self.mdtf.text
        with open('server/peoples.csv', encoding='utf-8') as peoples:
            file_reader = csv.reader(peoples, delimiter=";")
            self.ids.lists.clear_widgets()
            for name in file_reader:
                if name_value in name[0]:
                    self.trash_icon = TrailingPressedIconButton(icon="account-plus",
                                                                on_release=lambda button, friend=name[0]:
                                                                self.add_people(button, friend))
                    self.ids.lists.add_widget(MDListItem(
                        MDListItemLeadingAvatar(source=name[3].strip()),
                        MDListItemHeadlineText(text=name[0], theme_text_color='Custom', text_color='black'),
                        MDListItemSupportingText(text=name[1], theme_text_color='Custom', text_color='grey'),
                        MDListItemTertiaryText(text=name[2], theme_text_color='Custom', text_color='black'),
                        self.trash_icon
                    )
                    )



    def find_friends_button_click(self):
        self.friend_name_input = MDTextField(
            MDTextFieldLeadingIcon(icon='magnify'),
            MDTextFieldHelperText(text="Helper text"),
            mode="outlined")

        self.friend_search_dialog = MDDialog(
            MDDialogHeadlineText(text='Найти среди друзей'),
            MDDialogSupportingText(text="Введите имя и фамилию друга"),
            MDDialogContentContainer(self.friend_name_input),
            MDDialogButtonContainer(
                Widget(),
                MDButton(
                    MDButtonText(text="Отмена"),
                    style="text",
                    on_release=lambda *args: self.friend_search_dialog.dismiss()
                ),
                MDButton(
                    MDButtonText(text="Найти"),
                    style="text",
                    on_release=lambda *args: self.friend_search_button_click()
                ),
                spacing="8dp",
            ),
        )
        self.friend_search_dialog.open()

    def friend_search_button_click(self):
        name_value = self.friend_name_input.text
        with open('server/friends.csv', encoding='utf-8') as peoples:
            file_reader = csv.reader(peoples, delimiter=";")
            self.ids.lists.clear_widgets()
            for name in file_reader:
                if name_value in name[0]:
                    self.ids.lists.add_widget(MDListItem(
                        MDListItemLeadingAvatar(source=name[3].strip()),
                        MDListItemHeadlineText(text=name[0], theme_text_color='Custom', text_color='black'),
                        MDListItemSupportingText(text=name[1], theme_text_color='Custom', text_color='grey'),
                        MDListItemTertiaryText(text=name[2], theme_text_color='Custom', text_color='black'),
                        TrailingPressedIconButton(icon="email",
                                                  on_release=lambda button, friend=name[0]:
                                                  self.message_dialog_open(button, friend),
                                                  )
                    )
                    )
        self.friend_search_dialog.dismiss()

    def message_dialog_open(self, button, friend_name):
        self.message_input_field = MDTextField(mode="filled", height="100dp", multiline=True)

        self.message_dialog = MDDialog(
            MDDialogHeadlineText(text=f'Сообщение {friend_name}'),
            MDDialogContentContainer(self.message_input_field),
            MDDialogButtonContainer(
                Widget(),
                MDButton(
                    MDButtonText(text="Отмена"),
                    style="text",
                    on_release=lambda *args: self.message_dialog.dismiss()
                ),
                MDButton(
                    MDButtonText(text="Отправить"),
                    style="text",
                    on_release=lambda *args: self.message_send_button_click()
                ),
                spacing="8dp",
            ),
        )
        self.message_dialog.open()

    def message_send_button_click(self):
        popup_content = Label(text='Сообщение успешно отправлено!')
        popup = Popup(title='Успешно', content=popup_content, size_hint=(None, None), size=(340, 180))
        popup.open()
        Clock.schedule_once(lambda x: popup.dismiss(), 2)
        print(self.message_input_field.text)
        self.message_dialog.dismiss()

    def add_people(self, button, people_name):
        print(f'People {people_name} is add to your friend list')
        with open('server/peoples.csv', encoding='utf-8') as peoples:
            file_peoples_reader = csv.reader(peoples, delimiter=";")
            for row in file_peoples_reader:
                if people_name in row[0]:
                    string_row = ';'.join(str(elem) for elem in row)
                    with open('server/friends.csv', 'a', encoding='utf-8') as friends:
                        friends.write(string_row)
                        friends.write('\n')
        with open('server/peoples.csv', 'r+', encoding='utf-8') as peoples:
            peoples_list = peoples.readlines()
        with open('server/peoples.csv', 'w', encoding='utf-8') as file:
            for line in peoples_list:
                if people_name not in line:
                    file.write(line)
        button.icon = 'check'
        button.disabled = True

        add_friend_dialog = MDDialog(
            MDDialogSupportingText(
                text=f"{people_name} добавлен в друзья!",
            ),
        )
        add_friend_dialog.open()
        Clock.schedule_once(lambda x: add_friend_dialog.dismiss(), 2)
