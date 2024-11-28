from selenium import webdriver
from POM.AdminPage import AdminLoginPage
from Libary.BaseFile import BaseClass
import pytest
from Testdata.Excel import read_data,read_headers


headers= read_headers("test_adminpage","Smoke")
data = read_data("test_adminpage","Smoke")

@pytest.mark.parametrize(headers,data)
def test_adminpage(_driver,username,password):
    b = BaseClass(_driver)
    a =AdminLoginPage(_driver)
    a.admin_login(username,password)
