from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def main():
    service=Service()
    First_name=input('First Name?')
    Last_name=input('Last Name?')
    url="https://www.linkedin.com/pub/dir/+/+?trk=guest_homepage-basic_guest_nav_menu_people"
    chromeoptions=webdriver.ChromeOptions()
    # chromeoptions.headless=True
    driver=webdriver.Chrome(service=service)
    driver.get(url)
    first_name="#people-search-panel > form > section:nth-child(1) > input"
    last_name="#people-search-panel > form > section:nth-child(2) > input"
    elem_f=driver.find_element('css selector',first_name)
    elem_l=driver.find_element('css selector', last_name)
    elem_f.clear()
    elem_l.clear()
    elem_f.send_keys(First_name)
    elem_l.send_keys(Last_name)
    button_path='#people-search-panel > form > button'
    elem=driver.find_elementO('css selector',button_path)
    elem.click()
    path="#main-content > section > ul > li:nth-child(1) > a > div.base-search-card__info > h3"
    elems=driver.find_elements('css selector',path)
    for elem in elems:
        print(elem.text)
main()