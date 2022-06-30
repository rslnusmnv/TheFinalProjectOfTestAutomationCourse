from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PROCEED_TO_CHECKOUT_BUTTON), "Basket is not empty"

    def is_message_basket_empty_present(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET_EMPTY), "Message 'Your basket is empty' is not found"
