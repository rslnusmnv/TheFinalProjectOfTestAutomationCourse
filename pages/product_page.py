from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_on_add_to_basket_button(self):
        self.click_on_the_button(*ProductPageLocators.ADD_TO_BASKET_BUTTON)

    def should_be_product_added_in_basket(self):
        self.should_be_toaster_with_product_name()
        self.should_be_toaster_with_basket_cost()

    def should_be_toaster_with_product_name(self):
        #toaster_text = self.browser.extract_element_text(*ProductPageLocators.TOASTER_WITH_PRODUCT_NAME)
        #product_name_text = self.browser.extract_element_text(*ProductPageLocators.PRODUCT_NAME)
        toaster_text = self.extract_element_text(*ProductPageLocators.TOASTER_WITH_PRODUCT_NAME)
        product_name_text = self.extract_element_text(*ProductPageLocators.PRODUCT_NAME)
        assert toaster_text == product_name_text, f"Product name:{product_name_text} Toaster contain product name:{toaster_text}"

    def should_be_toaster_with_basket_cost(self):
        toaster_text = self.extract_element_text(*ProductPageLocators.TOASTER_WITH_BASKET_COST)
        product_cost_text = self.extract_element_text(*ProductPageLocators.PRODUCT_COST)
        assert toaster_text == product_cost_text, f"Product cost:{product_cost_text} Toaster contain basket cost:{toaster_text}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_of_success_message(self):
        assert not self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"


