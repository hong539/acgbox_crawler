# db_settingup

## tips/guides/etc...

* [createdb](https://www.postgresql.org/docs/current/app-createdb.html)
* [pg_upgrade](https://www.postgresql.org/docs/current/pgupgrade.html)
* [Look at "pacman directly install PostgreSQL on Arch Linux", if you want to use PostgreSQL instead of MySQL 5.7](https://github.com/hong539/local_library_website#prerequisites)
    * [With the upcoming end-of-life of MySQL Community Version v5.7 in October 2023 (Page 24)](https://aws.amazon.com/blogs/database/introducing-amazon-rds-extended-support-for-mysql-databases-on-amazon-aurora-and-amazon-rds/)
* [docekr postgres](https://hub.docker.com/_/postgres)
* database driver
    * mysql-connector-python
    * PyMySQL
    * MySQLdb
* create a test MySQL DB with podman
* [SQLAlchemy](https://www.sqlalchemy.org/)
    * [DBAPI Support](https://docs.sqlalchemy.org/en/20/dialects/mysql.html#dialect-mysql)
    * [Using MySQL with SQLAlchemy: Hands-on examples](https://planetscale.com/blog/using-mysql-with-sql-alchemy-hands-on-examples)
* container part(such as Podman/docker...etc)
    * [Installing Podman](https://podman.io/docs/installation#installing-on-linux)
    * [fuse-overlayfs](https://github.com/containers/fuse-overlayfs)
    * [Podman is gaining rootless overlay support](https://www.redhat.com/sysadmin/podman-rootless-overlay)
    * [Archwiki/Podman](https://wiki.archlinux.org/title/Podman)
    * Enable native rootless overlays
    * [podman-docker](https://archlinux.org/packages/extra/x86_64/podman-docker/)
    * [podman-compose](https://github.com/containers/podman-compose)