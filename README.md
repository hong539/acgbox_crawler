# acgbox_crawler
An acgbox_crawler for gamer.com.tw/acgbox

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
pipenv install SQLAlchemy

#pipenv requirements > requirements.txt

python src/main.py
```

# others

* [selenium](https://pypi.org/project/selenium/)