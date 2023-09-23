# db_settingup

## tips/guides/etc...

* [PostgreSQL 15 手冊翻譯](https://docs.postgresql.tw/v/15/)
* [Design Tools](https://wiki.postgresql.org/wiki/Design_Tools)
* [FAQ/zh-hant](https://wiki.postgresql.org/wiki/FAQ/zh-hant)

```shell
sudo -iu postgres
createuser --interactive
createdb acgbox_crawler
psql -d acgbox_crawler

psql -U myuser -W -h localhost -d mydb

#SQL part for PostgreSQL
#src: https://wiki.archlinux.org/title/PostgreSQL#Require_password_for_login
#ALTER PASSWORD for USER
ALTER USER acgbox_bot WITH PASSWORD 'new_password';

#edit pg_hba.conf/postgresql.conf
sudo vim /var/lib/postgres/data/pg_hba.conf
sudo vim /var/lib/postgres/data/postgresql.conf

#restart PostergreSQL daemon
sudo systemctl restart postgresql.service

#Test codes with main.py
#psycopg.errors.InsufficientPrivilege: permission denied for schema public
GRANT ALL PRIVILEGES ON DATABASE acgbox_crawler TO acgbox_bot;
GRANT ALL PRIVILEGES ON SCHEMA public TO acgbox_bot;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO acgbox_bot;
```

* [Collation version mismatch](https://dba.stackexchange.com/questions/324649/collation-version-mismatch)

```sql
REINDEX DATABASE postgres;
ALTER DATABASE postgres REFRESH COLLATION VERSION;
```

* [Archwiki/PostgreSQL#Familiarize_with_PostgreSQL](https://wiki.archlinux.org/title/PostgreSQL#Familiarize_with_PostgreSQL)
* rolling release vs Point release
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
    * [install psycopg](https://pypi.org/project/psycopg/)
    * [Psycopg 3](https://www.psycopg.org/psycopg3/)
    * [Support for the PostgreSQL database.](https://docs.sqlalchemy.org/en/20/dialects/postgresql.html)
    * [DBAPI Support](https://docs.sqlalchemy.org/en/20/dialects/mysql.html#dialect-mysql)
    * [Database URLs](https://docs.sqlalchemy.org/en/20/core/engines.html#database-urls)
    * [Using MySQL with SQLAlchemy: Hands-on examples](https://planetscale.com/blog/using-mysql-with-sql-alchemy-hands-on-examples)    
* container part(such as Podman/docker...etc)
    * [Installing Podman](https://podman.io/docs/installation#installing-on-linux)
    * [fuse-overlayfs](https://github.com/containers/fuse-overlayfs)
    * [Podman is gaining rootless overlay support](https://www.redhat.com/sysadmin/podman-rootless-overlay)
    * [Archwiki/Podman](https://wiki.archlinux.org/title/Podman)
    * Enable native rootless overlays
    * [podman-docker](https://archlinux.org/packages/extra/x86_64/podman-docker/)
    * [podman-compose](https://github.com/containers/podman-compose)

* sqlalchemy engine_url password duplicate@ cause str passe_error
    * 請問程式設計中，對於密碼之字元/字串的特殊符號(例如在MySQL的密碼中有使用到符號@)解析錯誤是不是常常出現?
        * 在程式設計中，特殊符號造成的解析錯誤是常常出現的問題之一，尤其是在處理密碼或其他機密資訊時。特殊符號（如 @、$、&、#、*等）在不同的程式語言和環境中可能有不同的含義，如果沒有正確地處理，就可能導致解析錯誤。尤其是在SQL語句中使用特殊符號時，如果沒有進行適當的轉義，就可能導致SQL注入攻擊等安全問題。因此，在處理密碼和其他機密資訊時，應該適當地處理特殊符號，以確保程式的安全性和正確性。

```python
mysql+<drivername>://<username>:<password>@<server>:<port>/dbname
```    