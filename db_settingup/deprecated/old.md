# old

## This is a old and deprecated setup for running MySQL(5.7) with podman-compose

```shell
#Reminder!!!
#Please replace this to your own password for MySQL root user
vim docker-compose.yml
MYSQL_ROOT_PASSWORD

#Error: kernel does not support overlay fs: 'overlay' is not supported over extfs at "/home/hong/.local/share/containers/storage/overlay": backing file system is unsupported for this graph driver
sudo podman info --format '{{.Store.Driver}}'
sudo podman info --format '{{.Store.GraphDriverName}}'
#check kernel version
uname -r
#Enable native rootless overlays
podman system reset

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