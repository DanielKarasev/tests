import pytest, allure, javaproperties
from pages.foop_list_page import FOOPListPage
#from pages.foop_page import FOOPPage
from pages.login_page import LoginPage
#from pages.foop_site_page import FOOPSitePage

with open('data.properties', 'r', encoding='utf-8') as data:
    props = javaproperties.load(data)

link = props['foop_list_link']
site_link = props['foop_link']