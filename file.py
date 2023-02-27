import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(autouse=True)
def testing():
    pytest_driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
    pytest_driver.get('https://petfriends.skillfactory.ru/login')
    pytest_driver.implicitly_wait(2)
    yield pytest_driver
    pytest_driver.quit()

def test_my_account(testing):
    pytest_driver = testing
    pytest_driver.find_element(By.ID, 'email').send_keys('mail@mail.ru')
    pytest_driver.find_element(By.ID, 'pass').send_keys('12345qwerty')
    pytest_driver.find_element(By.CSS_SELECTOR, "button[type=\"submit\"]").click()
    assert pytest_driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    images = WebDriverWait(pytest_driver, 5).until(EC.presence_of_all_elements_located(By.CSS_SELECTOR, '.card-deck.card-img-top'))
    names = WebDriverWait(pytest_driver, 5).until(EC.presence_of_all_elements_located(By.CSS_SELECTOR, '.card-deck.card-title'))
    descriptions = WebDriverWait(pytest_driver, 5).until(EC.presence_of_all_elements_located(By.CSS_SELECTOR, '.card-deck.card-text'))

    for i in range(len(names)):
        assert images[i].get_attribute('src') != ""
        assert names[i].text != ""
        assert descriptions[i].text != ""
        assert ',' in descriptions[i]
        parts = descriptions[i].text.split(",")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0
    print("Everything is Good")


def test_show_all_pets(testing):
    # Finding cards of all pets
    pytest_driver = testing
   pytest_driver.find_element(By.ID, 'email').send_keys('mail@mail.ru')
    pytest_driver.find_element(By.ID, 'pass').send_keys('12345qwerty')
    pytest_driver.find_element(By.CSS_SELECTOR, "button[type=\"submit\"]").click()
    assert pytest_driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    pytest_driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul[1]/li[1]/a[1]').click()
    pytest_driver.find_element(By.CSS_SELECTOR, "html > body > div > div > div > h2")
    assert pytest_driver.find_element(By.TAG_NAME, 'h2').text == "Kati"
    print("Everything is Good")


def test_count_pet_cards(testing):
    pytest_driver = testing
    pytest_driver.find_element(By.ID, 'email').send_keys('mail@mail.ru')
    pytest_driver.find_element(By.ID, 'pass').send_keys('12345qwerty')
    pytest_driver.find_element(By.CSS_SELECTOR, "button[type=\"submit\"]").click()
    cards = pytest_driver.find_elements(By.CLASS_NAME, 'card-title')

    pet_names = []
    for pet in cards:
        pet_names.append(pet.text)
        print(pet_names)
    print(len(pet_names))
    assert len(pet_names) == len(cards)
    print("Everything is Good")
