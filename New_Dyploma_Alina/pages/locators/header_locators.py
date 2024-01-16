from selenium.webdriver.common.by import By

catalog_button = (By.XPATH,'(//a[@class="ogg-menu__link  ogg-menu__link_with-categories  "])[1]')
brands_button = (By.XPATH,'(//a[@class="ogg-menu__link   "])[1]')
novelty_button = (By.XPATH,'(//a[@class="ogg-menu__link   "])[2]')
stock_button = (By.XPATH,'(//a[@class="ogg-menu__link   "])[3]')
clients_days_button = (By.XPATH,'(//a[@class="ogg-menu__link   "])[4]')
stores_button = (By.XPATH,'(//a[@class="ogg-menu__link   "])[5]')
gift_certificates_button = (By.XPATH,'//a[@class="ogg-menu__link   ogg-menu__link_with-category-icon"]')
gift_ideas_button = (By.XPATH,'(//a[@class="ogg-menu__link  ogg-menu__link_with-categories  ' \
                    'ogg-menu__link_with-category-icon"])[2]')
discount_40_percent = (By.XPATH,'(//a[@class="ogg-menu__link  ogg-menu__link_with-categories ' \
                      ' ogg-menu__link_with-category-icon"])[3]')
choose_city_button = (By.XPATH,'(//div[@class="header-city"])[1]')
search_button = (By.XPATH,'//button[@class="header-tab-button header-tab-button_search"]')
text_area = (By.XPATH, '//textarea[@id="search_multiline"]') #ввод в поле поиска
liked_button = (By.XPATH,'//button[@class="header-tab-button header-tab-button_wishlist"]')
profile_button = (By.XPATH,'//button[@class="header-tab-button header-tab-button_customer"]')
basket_button = (By.XPATH,'class="header-tab-button header-tab-button_minicart"')
