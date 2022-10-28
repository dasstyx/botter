from abc import ABC, abstractmethod

from src.button.button_factory import TgButtonFactory, VkButtonFactory
from src.keyboard.markup_factory import TgKeyboardMarkupFactory, VkKeyboardMarkupFactory
from src.page.page_data import PageData


class PageFactory(ABC):

    def __init__(self, api, navigator, bot_events):
        self.bot_events = bot_events
        self.navigator = navigator
        self.api = api

    @abstractmethod
    def _make_dependencies(self, page_data: PageData):
        pass

    def create(self, data: PageData):
        self._make_dependencies(data)
        return data.page_type(data.path, self.api, self.navigator, self.bot_events, self.markup_factory, data)


class TgPageFactory(PageFactory):
    def _make_dependencies(self, page_data: PageData):
        button_factory = TgButtonFactory(page_data.inline)
        self.markup_factory = TgKeyboardMarkupFactory(button_factory)


class VkPageFactory(PageFactory):
    def _make_dependencies(self, page_data: PageData):
        button_factory = VkButtonFactory(page_data.inline)
        self.markup_factory = VkKeyboardMarkupFactory(button_factory)
