import time
import unittest
import HtmlTestRunner
from selenium import webdriver

class myTestWeb(unittest.TestCase):
    def testCase(self):
        self.driver = webdriver.Chrome(executable_path='../Pantalla_Login/chromedriver.exe')
        self.driver.get('http://129.159.102.93/#/pages/login')
        time.sleep(2)
        # Ubicando objetos para ingreso de usuario y contraseña en el sistema
        usuario = self.driver.find_element_by_id('mat-input-0')
        usuario.clear()
        usuario.send_keys('cristian_parada@TESTLAB')
        time.sleep(2)
        contrasena = self.driver.find_element_by_id('mat-input-1')

        contrasena.clear()
        contrasena.send_keys('Unicomer21')
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '/html/body/div/app-root/app-login/div[1]/div/mat-card/mat-card-content/form/div[2]/div[2]/div/div/button/span[1]').click()
        time.sleep(2)
        self.driver.stop_client()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r'C:\Users\cristian_parada\Desktop\Practica_Automatizacion\Reportes_Casos_Pruebas'))
