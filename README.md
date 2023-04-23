# acgbox_crawler
An web_crawler for gamer.com.tw/acgbox

## Setting UP

* [Installing Podman](https://podman.io/getting-started/#installing-podman)
* create a test MySQL DB with podman

```shell
#create a MySQL container with podman-compose
cd db_settingup/

#Reminder!!!
#Please replace this to your own password for MySQL root user
vim docker-compose.yml
MYSQL_ROOT_PASSWORD

#Run a MySQL:5.7 with podman-compose
podman-compose up -d

#Go to containter and test mysql
podman exec -it db_settingup_db_1 bash
mysql -u root -p
show databases;

#Stop
podman-compose stop

#Force removal of a running or unusable container
podman rm -f

#Other commands
podman stop -l
podman rm -l
podman ps
```

* [SQLAlchemy](https://www.sqlalchemy.org/)
    * [DBAPI Support](https://docs.sqlalchemy.org/en/20/dialects/mysql.html#dialect-mysql)
* [Using MySQL with SQLAlchemy: Hands-on examples](https://planetscale.com/blog/using-mysql-with-sql-alchemy-hands-on-examples)
* database driver
    * mysql-connector-python
    * PyMySQL
    * MySQLdb
* ModuleNotFoundError: No module named 'MySQLdb'
* sqlalchemy engine_url password duplicate@ cause str passe_error
    * 請問程式設計中，對於密碼之字元/字串的特殊符號(例如在MySQL的密碼中有使用到符號@)解析錯誤是不是常常出現?
        * 在程式設計中，特殊符號造成的解析錯誤是常常出現的問題之一，尤其是在處理密碼或其他機密資訊時。特殊符號（如 @、$、&、#、*等）在不同的程式語言和環境中可能有不同的含義，如果沒有正確地處理，就可能導致解析錯誤。尤其是在SQL語句中使用特殊符號時，如果沒有進行適當的轉義，就可能導致SQL注入攻擊等安全問題。因此，在處理密碼和其他機密資訊時，應該適當地處理特殊符號，以確保程式的安全性和正確性。

```python
mysql+<drivername>://<username>:<password>@<server>:<port>/dbname
```

* [Usage with your python projects](https://github.com/hong539/setup_dev_environment/tree/main/programing_languages/python#usage-with-your-python-projects)

## Test

```shell
#After Setting UP with Usage with your python projects
#Spawns a shell within the virtualenv.
pipenv shell

#Packages
pipenv install requests
pipenv install beautifulsoup4
pipenv install pandas
pipenv install lxml
pipenv install SQLAlchemy
pipenv install PyYAML
pipenv install pymysql
pipenv install fake-useragent

#Generate a requirements.txt from Pipfile.lock. to requirements.txt
pipenv requirements > requirements.txt

#Becareful your execute PATH! XD 
python src/main.py

#Test
cd src
python main.py
#time a simple command or give resource usage
time python main.py
# real    2m55.699s
# user    0m3.973s
# sys     0m0.858s
```

## others

* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
    * [searching-by-css-class](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-by-css-class)
* [requests](https://github.com/psf/requests)
* [pandas](https://pandas.pydata.org/)
* [lxml](https://lxml.de/)
* [PyYAML](https://pyyaml.org/)
* [selenium](https://pypi.org/project/selenium/)
    * [Selenium Documentation](https://www.selenium.dev/selenium/docs/api/py/api.html)
* [Scrapy](https://scrapy.org/)
* [MechanicalSoup](https://mechanicalsoup.readthedocs.io/en/stable/)
