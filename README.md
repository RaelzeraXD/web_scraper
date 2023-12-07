# web_scraper
a simple web scraper in python using selenium and inserting it into a xlsx file ( Excel | LibreOffice Calc ) or send to mysql

## how to use (python w/excel)
* cd web_scraper
* pip3 install -r requirements.txt
* ./main.py

## how to use (python w/mysql)
* cd web_scraper
* pip3 install -r requirements.txt
* ./database.py
* ./main_db.py

## Problems
if you get some problems to connect with mysql try this:
* sudo  mysql
* USE mysql;
* UPDATE user SET plugin='mysql_native_password' WHERE User='root';
* FLUSH PRIVILEGES;
* exit;
* sudo systemctl restart mysql.service