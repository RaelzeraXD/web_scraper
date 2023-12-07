#!/bin/python3
#
#Author: israel silva de freitas
#------------------------------
#          CHANGELOG
# v1.0 12/07/2023
#   -first release with mysql support
#------------------------------
from selenium import webdriver
from selenium.webdriver.common.by import By
import mysql.connector

driver = webdriver.Chrome()
driver.get('https://www.kabum.com.br/promocao/MENU_PCGAMER')
title = driver.find_elements(By.XPATH,"//span[@class='sc-d79c9c3f-0 nlmfp sc-cdc9b13f-16 eHyEuD nameCard']")
price = driver.find_elements(By.XPATH,"//span[@class='sc-620f2d27-2 bMHwXA priceCard']")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="products"
)
mycursor = mydb.cursor()

# Create the table if it doesn't exist
mycursor.execute("CREATE TABLE IF NOT EXISTS products (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), price VARCHAR(15));")

for a,b in zip(title,price):
  sql = "INSERT INTO products (title, price) VALUES (%s, %s)"
  val = (a.text, b.text) 
  mycursor.execute(sql, val)
  mydb.commit()
mycursor.close()
mydb.close()