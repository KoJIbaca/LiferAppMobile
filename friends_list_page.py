import csv
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.list import (MDListItem, MDListItemHeadlineText, MDListItemLeadingAvatar, MDListItemSupportingText,
                             MDListItemTertiaryText, MDList)


Builder.load_file('kv/friends_list_page.kv')


class FriendsListPage(Screen):

    def back_to_profile_page(self):
        self.manager.current = 'profile_page'
        self.manager.transition.direction = 'right'

    def on_enter(self):
        if not self.ids.lists:
            self.ids.scroll.add_widget(MDList(id='lists'))

        with open("server/friends.csv", encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter=";")
            self.ids.lists.clear_widgets()
            for row in file_reader:
                self.ids.lists.add_widget(MDListItem(
                        MDListItemLeadingAvatar(source=f'{(row[3]).strip()}'),
                        MDListItemHeadlineText(text=f"{row[0]}", theme_text_color='Custom', text_color='black'),
                        MDListItemSupportingText(text=f'{row[1]}', theme_text_color='Custom', text_color='grey'),
                        MDListItemTertiaryText(text=f'{row[2]}', theme_text_color='Custom', text_color='black'),
                    )
                )

