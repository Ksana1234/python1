import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Search(unittest.TestCase):
    def setUp(self): #операции до запуска теста
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
# 1. Открыть страницу http://google.com/ncr
        self.driver.get('http://google.com/ncr')

    def test_search(self):
        assert 'Google' in self.driver.title
# 2. Выполнить поиск слова “selenide”
        elem = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        elem.send_keys('selenide')
        elem.send_keys(Keys.RETURN)
# 3. Проверить, что первый результат – ссылка на сайт selenide.org.
        fr_link = self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a/div/div/div/cite')
        assert fr_link.text == 'https://selenide.org'
# 4. Перейти в раздел поиска изображений
        image_search = self.driver.find_element(By.XPATH, '//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()
# 5. Проверить, что первое изображение неким образом связано с сайтом selenide.org.
        fr_image = self.driver.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img')
        assert 'Selenide' in fr_image.accessible_name
# 6. Вернуться в раздел поиска Все
        all_search = self.driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[2]/c-wiz/div[1]/div/div[1]/div[1]/div/div/a[1]').click()
# 7. Проверить, что первый результат такой же, как и на шаге 3 (результат не такой же. При первом поиске ссылка - 'https://selenide.org', после перехода в раздел "Все" - 'https://ru.selenide.org'.)
        fr_link2 = self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a/div/div/div/cite')
        assert fr_link2.text == 'https://selenide.org'

    def tearDown(self): #операции после завершения теста
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
