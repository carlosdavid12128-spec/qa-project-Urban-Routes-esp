from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from utils.retrieve_code import retrieve_phone_code



class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    request_taxi_button = (By.CSS_SELECTOR, '.button.round')
    comfort_rate = (By.XPATH, "//div[@class='tcard-title' and text()= 'Comfort']")
    phone_number_button= (By.CSS_SELECTOR,'.np-button')
    phone_number_field = (By.ID, 'phone')
    next_button = (By.CSS_SELECTOR, '.button.full')
    code = (By.ID, 'code')
    confirm_button = (By.XPATH, "//button[contains(text(),'Confirmar')]")
    payment_button = (By.CSS_SELECTOR, ".pp-button.filled")
    add_card_button = (By.CSS_SELECTOR, '.pp-row.disabled')
    card_number_field = (By.ID, 'number')
    card_code_field = (By.XPATH, "//div[@class='card-code-input']//*[@id='code']")
    add_card_confirm_button = (By.XPATH, "//button[contains(text(),'Agregar')]")
    payment_close_button = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/button")
    message_for_driver_field = (By.XPATH, "//*[@id='comment']")
    slider_blanket = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span")
    order_taxi_button = (By.CLASS_NAME, "smart-button-wrapper")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def set_from(self, from_address):
        #self.driver.find_element(*self.from_field).send_keys(from_address)
        self.wait.until(EC.presence_of_element_located(self.from_field)).send_keys(from_address)

    def set_to(self, to_address):
        #self.driver.find_element(*self.to_field).send_keys(to_address)
        self.wait.until(EC.presence_of_element_located(self.to_field)).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, address_from,address_to):
        self.set_from(address_from)
        self.set_to(address_to)


# getter -> busca y devuelve un elemento
    def get_request_taxi_button(self):
        return self.wait.until(EC.presence_of_element_located(self.request_taxi_button))

# clicker -> interactua con el elemento
    def click_request_taxi_button(self):
        self.get_request_taxi_button().click()

# getter -> busca y devuelve un elemento
    def get_comfort_rate_icon(self):
        return self.wait.until(EC.presence_of_element_located(self.comfort_rate))

# clicker -> interactua con el elemento
    def click_comfort_rate_icon(self):
        self.get_comfort_rate_icon().click()

# getter -> busca y devuelve un elemento
    def get_phone_number_button(self):
        return self.wait.until(EC.presence_of_element_located(self.phone_number_button))

# clicker -> interactua con el elemento
    def click_phone_number_button(self):
        self.get_phone_number_button().click()

    def set_phone_number_field(self, phone_field):
        self.wait.until(EC.presence_of_element_located(self.phone_number_field)).send_keys(phone_field)

    def get_phone_number_field(self):
        return self.driver.find_element(*self.phone_number_field).get_property('value')

    def set_phone_number(self, phone_number):
        self.set_phone_number_field(phone_number)

    def get_next_button(self):
        return self.wait.until(element_to_be_clickable(self.next_button))

    def click_next_button(self):
        self.get_next_button().click()

    def set_code_field(self, code_field):
        self.wait.until(EC.presence_of_element_located(self.code)).send_keys(code_field)

    def get_code_field(self):
        return self.driver.find_element(*self.code).get_property('value')

    def set_code(self, card_code):
        self.set_phone_number_field(card_code)

    def get_sms_code(self):
        """Obtiene el código SMS interceptado desde los logs del navegador"""
        return retrieve_phone_code(self.driver)

    def get_phone_code(self):
        return retrieve_phone_code(self.driver)

    def get_confirm_button(self):
        return self.wait.until(EC.presence_of_element_located(self.confirm_button))

    def click_confirm_button(self):
        self.get_confirm_button().click()

    def get_payment_button(self):
        element = self.wait.until(EC.presence_of_element_located(self.payment_button))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return self.wait.until(EC.visibility_of(element))

    def click_payment_button(self):
        self.get_payment_button().click()

    def get_add_card_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.add_card_button))

    def click_add_card_button(self):
        self.get_add_card_button().click()

    def get_card_number_field(self):
        return self.wait.until(EC.presence_of_element_located(self.card_number_field))

    def get_card_number_value(self):
        return self.driver.find_element(*self.card_number_field).get_property('value')

    def click_card_number_field(self):
        self.get_card_number_field().click()

    def set_card_number_field(self, card_number):
        self.wait.until(EC.presence_of_element_located(self.card_number_field)).send_keys(card_number)

    def get_card_code_field(self):
        return self.wait.until(EC.presence_of_element_located(self.card_code_field))

    def get_card_code_value(self):
        return self.driver.find_element(*self.card_code_field).get_property('value')

    def click_card_code_field(self):
        self.get_card_code_field().click()

    def set_card_code_field(self, card_code):
        self.wait.until(EC.presence_of_element_located(self.card_code_field)).send_keys(card_code)
        field = self.wait.until(EC.presence_of_element_located(self.card_code_field))
        field.send_keys(Keys.TAB)

    def get_confirm_card_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.add_card_confirm_button))

    def click_confirm_card_button(self):
        self.get_confirm_card_button().click()

    def get_payment_close_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.payment_close_button))

    def click_payment_close_button(self):
        self.get_payment_close_button().click()

    def get_message_field(self):
        message_element = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[3]/div/label" )))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", message_element)
        return self.wait.until(EC.visibility_of(message_element))

    def get_message_value(self):
        return self.driver.find_element(*self.message_for_driver_field).get_property('value')

    def click_message_field(self):
        self.get_message_field().click()


    def set_message_field(self, message_for_driver):
        self.wait.until(EC.element_to_be_clickable(self.message_for_driver_field)).send_keys(message_for_driver)

    def get_slider_blanket(self):
        return self.wait.until(EC.element_to_be_clickable(self.slider_blanket))

    def click_slider_blanket(self):
        self.get_slider_blanket().click()

    def get_counter_plus_ice_cream(self):
        counter_element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div[3]/div[3]"
                                                  "/div[2]/div[2]/div[4]/div[2]/div[3]"
                                                  "/div/div[2]/div[1]/div/div[2]/div/div[3]")))

        return self.wait.until(EC.visibility_of(counter_element))

    def click_counter_plus_ice_cream(self, times=2):
        for _ in range(times):
            self.get_counter_plus_ice_cream().click()

    def get_order_taxi_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.order_taxi_button))

    def click_order_taxi_button(self):
        self.get_order_taxi_button().click()

    def get_order_timeout(self):
        return self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'order-body')))

    def get_order_button(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/div[5]/div[2]/"
                                                                         "div[2]/div[1]/div[3]/button")))

    def click_order_button(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div[5]"
                                                              "/div[2]/div[2]/div[1]/div[3]/button")))
