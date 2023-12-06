#!/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

driver = webdriver.Chrome()
driver.get('https://www.kabum.com.br/promocao/MENU_PCGAMER')
title = driver.find_elements(By.XPATH,"//span[@class='sc-d79c9c3f-0 nlmfp sc-cdc9b13f-16 eHyEuD nameCard']")
price = driver.find_elements(By.XPATH,"//span[@class='sc-620f2d27-2 bMHwXA priceCard']")

workbook = openpyxl.Workbook()

#creating the sheet
workbook.create_sheet('computers')
pag = workbook['computers']

#inserting the titles
pag['A1'].value = 'products'
pag['B1'].value = 'prices'

#inserting each title and price into the workbook
for a,b in zip(title,price):
    pag.append([a.text,b.text])

workbook.save("computers.xlsx")