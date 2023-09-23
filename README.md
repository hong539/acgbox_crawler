# acgbox_crawler

An Python bot for doing ETL(extract, transform, load) personal favorite lists from gamer.com.tw/acgbox.

## Prerequisites

* Setup all on My Arch Linux VM
    * Python version ==3.8 and all dependencies will be managed via pyenv+pipenv
        * [Usage with pyenv+pipenv](https://github.com/hong539/setup_dev_environment/blob/main/programming_languages/python/python.md#usage-with-pyenvpipenv)
    * PostgreSQL 15

## to_do_list

* ~~Migration from MySQL to PostgreSQL~~
* Find Last Updated Date of a Web Page
* [TritonHo/RDBMS course](https://github.com/TritonHo/slides/blob/master/Taipei%202019-04%20course/lesson0.pdf)
* ~~pandas to_sql method if_exists='append' implementation function update method for only update new ACG collects?~~
* implementation function finding method for find last pages?
* research or implementation function for html tags div to table
* check which files will be stored via podman when not executing MySQL container
* implementation function CRUD API/query method for MySQL
* implementation function load_data
* implementation function modfy_data with advanced string replace in pandas.DataFrame
* refactor some parts codes to class acgbox_crawler(object)

## quick start

### setup on Arch Linux

```shell
#setup on Arch Linux
#update package databases
sudo pacman -Syy

#install podman
sudo pacman -S podman
#podman-docker
sudo pacman -S podman-docker
#podman-compose
sudo pacman -S podman-compose
#fuse-overlayfs
sudo pacman -S fuse-overlayfs

#podman: /usr/lib/libc.so.6: version `GLIBC_2.38' not found (required by podman)
#upgrading packages
sudo pacman -Syu

#check podman
podman --version

#create a MySQL container with podman-compose
cd db_settingup/

#check out the db_settingup.md
```

### start this project and do development

```shell
#After Setting UP with Usage with your python projects
#Spawns a shell within the virtualenv.
pipenv shell

#if no packages installed
pipenv install

#add some Packages
pipenv install diagrams
pipenv install "psycopg[binary,pool]"
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

## misc(miscellaneous)

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