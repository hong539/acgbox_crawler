#!/bin/bash

# src: https://dev.mysql.com/doc/refman/5.7/en/mysqldump-definition-data-dumps.html

# mysqldump --no-data --routines --events test > dump-defs.sql
mysqldump --no-data test > dump-defs.sql