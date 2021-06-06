-- create databases
CREATE DATABASE IF NOT EXISTS sennderdb;
CREATE DATABASE IF NOT EXISTS test_sennderdb;

-- create user
CREATE USER 'sennder'@'%' IDENTIFIED WITH mysql_native_password BY 'sennder';

-- grant priviliges
GRANT ALL ON sennderdb.* TO 'sennder'@'%';
GRANT ALL ON test_sennderdb.* TO 'sennder'@'%';
FLUSH PRIVILEGES;
