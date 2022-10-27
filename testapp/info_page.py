from src.button.button_data import ButtonData, ButtonCallback
from src.page.page import Page


class InfoPage(Page):

    async def _respond_to_input(self, user, text):
        await self.send_message(user, f"Нет, ты {text}")

    async def make_page_content(self, user):
        back_button = ButtonData("Back", ButtonCallback(self.nav.get_back))
        self.markup.add_row([
            back_button
        ])
        await self.send_keyboard_message(user, self.markup, 'Ну ты можешь вернуться...')
