docker pull mysql:8.0.23
mkdir -p /opt/mysql/{data,logs,conf,mysql-files}

sudo cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

docker run -p 3306:3306 --name communication -v /opt/mysql/conf:/etc/mysql \
      -v /opt/mysql/data:/var/lib/mysql \
      -v /opt/mysql/mysql-files:/var/lib/mysql-files/ \
      -v /opt/mysql/logs:/var/log/mysql \
      -v /etc/localtime:/etc/localtime:ro \
      -e MYSQL_ROOT_PASSWORD=123456 -d mysql

docker exec -it $(docker ps -a |grep communication|awk '{print $1}') /bin/bash

# Create database and user
MYCMD="mysql -u root -p123456"

$MYCMD -e "create database communication CHARACTER SET utf8 COLLATE utf8_general_ci;"
$MYCMD -e "CREATE USER 'communication'@'%' IDENTIFIED BY 'JSA238ksdfs35';"
$MYCMD -e "grant all on communication.* to communication@'%' WITH GRANT OPTION;"
$MYCMD -e "flush privileges;"