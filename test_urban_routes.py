from data import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service

from data.data import phone_number, card_code, card_number, message_for_driver
from pages import urban_routes_page as urp





class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        chrome_options = webdriver.ChromeOptions()
        chrome_options.set_capability('goog:loggingPrefs',{'performance': 'ALL'})
        cls.driver = webdriver.Chrome(service=Service(), options=chrome_options)
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = urp.UrbanRoutesPage(cls.driver)

    def test_set_route(self):
        #self.driver.get(data.urban_routes_url)
       # routes_page = urp.UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to

    def test_select_confort_rate(self):
        #routes_page = urp.UrbanRoutesPage(self.driver)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_rate_icon()


    def test_type_phone_number(self):
        self.routes_page.click_phone_number_button()
        self.routes_page.set_phone_number(phone_number)
        self.routes_page.click_next_button()

        # Aquí obtenemos el código interceptado
        code = self.routes_page.get_sms_code()
        print(f"Código recibido: {code}")

        # Lo ingresamos en el campo de código
        self.routes_page.set_code_field(code)

        self.routes_page.click_confirm_button()

    def test_payment_method(self):
        self.routes_page.click_payment_button()
        self.routes_page.click_add_card_button()
        self.routes_page.set_card_number_field(data.card_number)
        assert self.routes_page.get_card_number_value() == card_number
        print ('El numero de la tarjeta es correcto')

        self.routes_page.set_card_code_field(data.card_code)
        assert self.routes_page.get_card_code_value() == card_code
        print ('El codigo de la tarjeta es correcto')

        self.routes_page.click_confirm_card_button()
        self.routes_page.click_payment_close_button()

    def test_message_for_driver(self):
        self.routes_page.click_message_field()
        self.routes_page.set_message_field(data.message_for_driver)
        assert self.routes_page.get_message_value() == message_for_driver
        print ('El mensaje coincide')

    def test_slider_for_blanket(self):
        self.routes_page.click_slider_blanket()

    def test_counter_for_ice_cream(self):
        self.routes_page.click_counter_plus_ice_cream()

    def test_order_taxi_button(self):
        self.routes_page.click_order_taxi_button()

    def test_order_button(self):
        self.routes_page.click_order_button()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
