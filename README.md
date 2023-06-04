# acgbox_crawler
An web_crawler for gamer.com.tw/acgbox

## to_do_list

* implementation function method for find last pages?
* research or implementation function for html tags div to table
* check which files will be stored via podman when not executing MySQL container
* implementation function CRUD API/query method for MySQL
* implementation function load_data
* implementation function modfy_data with advanced string replace in pandas.DataFrame
* refactor some parts codes to class acgbox_crawler(object)


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
pipenv install user_agent
pipenv install tornado

#Generate a requirements.txt from Pipfile.lock. to requirements.txt
pipenv requirements > requirements.txt

#Becareful your execute PATH! XD 
#Test
pipenv shell
cd src
python main.py
#time a simple command or give resource usage
time python main.py
# real    2m55.699s
# user    0m3.973s
# sys     0m0.858s
```

## others

* html generator    
    * [htmlgenerator](https://pypi.org/project/htmlgenerator/)
    * [Yattag/ a generator for html/xml/pythonic ](https://www.yattag.org/)
    * [HTML div/table tag TABLE GENERATOR](https://divtable.com/generator/)

* html parser
    * [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
        * [searching-by-css-class](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-by-css-class)
    * [requests](https://github.com/psf/requests)
    * [pandas](https://pandas.pydata.org/)
    * [lxml](https://lxml.de/)
* [PyYAML](https://pyyaml.org/)
* Automation test
    * [selenium](https://pypi.org/project/selenium/)
        * [Selenium Documentation](https://www.selenium.dev/selenium/docs/api/py/api.html)
    * [Scrapy](https://scrapy.org/)
    * [Playwright/python](https://playwright.dev/python/)
        * enables reliable end-to-end testing for modern web apps.
    * [MechanicalSoup](https://mechanicalsoup.readthedocs.io/en/stable/)

## Important!!!

== We're Using GitHub Under Protest ==

This project is currently hosted on GitHub.  This is not ideal; GitHub is a
proprietary, trade-secret system that is not Free and Open Souce Software
(FOSS).  We are deeply concerned about using a proprietary system like GitHub
to develop our FOSS project.  We have an
[open {bug ticket, mailing list thread, etc.} ](INSERT_LINK) where the
project contributors are actively discussing how we can move away from GitHub
in the long term.  We urge you to read about the
[Give up GitHub](https://GiveUpGitHub.org) campaign from
[the Software Freedom Conservancy](https://sfconservancy.org) to understand
some of the reasons why GitHub is not a good place to host FOSS projects.

If you are a contributor who personally has already quit using GitHub, please
[check this resource](INSERT_LINK) for how to send us contributions without
using GitHub directly.

Any use of this project's code by GitHub Copilot, past or present, is done
without our permission.  We do not consent to GitHub's use of this project's
code in Copilot.

![Logo of the GiveUpGitHub campaign](https://sfconservancy.org/img/GiveUpGitHub.png)