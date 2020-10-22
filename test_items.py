import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_wishlist_button_is_present(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_element_by_css_selector("button.btn.btn-wishlist"), f'Кнопка "Добавление в корзину не найдена"'
    assert len(button) > 0, f"Кнопка не найдена"
