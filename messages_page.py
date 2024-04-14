from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file('kv/messages_page.kv')


class MessagesPage(Screen):

    def on_touch_move(self, touch):
        if touch.dx > 15:
            self.manager.transition.direction = 'right'
            self.manager.current = 'profile_page'

    # def on_enter(self):
    #     self.messages_list()

    def messages_list(self):
        # with open("server/friends.csv", encoding='utf-8') as r_file:
        #     file_reader = csv.reader(r_file, delimiter=";")
        #     self.ids.lists.clear_widgets()
        #     for row in file_reader:
        #         self.ids.messages_list.add_widget(MDListItem(
        #             MDListItemLeadingAvatar(source=row[3].strip()),
        #             MDListItemHeadlineText(text=row[0], theme_text_color='Custom', text_color='black'),
        #             MDListItemSupportingText(text=row[1], theme_text_color='Custom', text_color='grey'),
        #             MDListItemTertiaryText(text=row[2], theme_text_color='Custom', text_color='black'),
        #             )
        #         )
        pass

