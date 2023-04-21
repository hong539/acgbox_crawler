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


* [Usage with your python projects](https://github.com/hong539/setup_dev_environment/tree/main/programing_languages/python#usage-with-your-python-projects)

## Test

```shell
#After Setting UP with Usage with your python projects
#Spawns a shell within the virtualenv.
pipenv shell

pipenv install requests
pipenv install beautifulsoup4
pipenv install pandas
pipenv install lxml
pipenv install SQLAlchemy
pipenv install PyYAML

#Generate a requirements.txt from Pipfile.lock. to requirements.txt
pipenv requirements > requirements.txt

#Becareful your execute PATH! XD 
python src/main.py
```

## others

* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
    * [searching-by-css-class](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-by-css-class)
* [requests](https://github.com/psf/requests)
* [pandas](https://pandas.pydata.org/)
* [lxml](https://lxml.de/)
* [PyYAML](https://pyyaml.org/)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [selenium](https://pypi.org/project/selenium/)
    * [Selenium Documentation](https://www.selenium.dev/selenium/docs/api/py/api.html)
* [Scrapy](https://scrapy.org/)
* [MechanicalSoup](https://mechanicalsoup.readthedocs.io/en/stable/)
