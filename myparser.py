from selenium import webdriver
import time

url = 'https://www.worldometers.info/coronavirus/'

def get_info_kz(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(0.5)
    input_field = driver.find_element_by_class_name('form-control')
    input_field.send_keys('Kazakhstan')

    ths = ['Страна', 'Всего случаев', 'Новые случаи', 'Всего смертей', 'Новые случаи смертей', 'Всего вылечилось', 'Активные случаи', 'Критические случаи', 'Всего случаев на 1М населения']
    tds = driver.find_elements_by_tag_name('td')[:9]

    dict = {}
    for th, td in zip(ths, tds):
        td_text = td.text
        if td_text != '':
            dict[th] = 'недостаточно данных' if td_text == '' else td_text
    del dict['Страна']
    driver.close()
    return dict

