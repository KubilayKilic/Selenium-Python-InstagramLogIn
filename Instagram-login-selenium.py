#@author: kaan

# ==============================================================
# ****** kısımlarına kullanıcı adınızı ve şifrenizi giriniz.
# timesleep süreleri rastgele belirlenmiştir, browser kendine
# gelsin diye beklenecek afaki saniyelerdir (değiştirilebilir.)
# ==============================================================

from selenium import webdriver
import time

browser = webdriver.Chrome() #Chrome'u açar.

browser.get("https://www.instagram.com") #belirtilen adrese gider.

time.sleep(4) #4saniye bekler, istenilen bir süre olabilir.

username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")

#kullanıcı adı ve şifre kısımlarını nametaglerine göre bulur.

time.sleep(2) #bir süre bekler.

username.send_keys("******") #kullanıcı adı girilecek kısım.
password.send_keys("******") #şifre girilecek kısım.

#verilen kullanıcı adı ve şifre değerlerini girer.

time.sleep(4)

#giriş yap tuşunun xpath id'sine göre üstüne gelir.
login = browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[4]/button/div")
login.click()#giriş yap tuşuna tıklar.

time.sleep(2)

#giriş yaptıktan sonra şifre hatırlama bildiriminde şimdi değil'in üzerine gelir ve ona tıklar.

simdi_degil = browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button")
simdi_degil.click()

time.sleep(4)

#bildirim açma pop-up'ında şimdi değilin üzerine gelir ve ona tıklar.
no = browser.find_element_by_css_selector(".aOOlW.HoLwm")#xpath'e göre değil css selector'a göre yapılır.
no.click()

time.sleep(4) #bir süre bekledikten sonra

browser.close() #pencere kapatılır.
