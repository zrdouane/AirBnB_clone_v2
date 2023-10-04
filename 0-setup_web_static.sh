#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static.

apt-get -y update > /dev/null
apt-get install -y nginx > /dev/null

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
touch /data/web_static/releases/test/index.html
echo "Hello World From Morocco" > /data/web_static/releases/test/index.html
if [ -d "/data/web_static/current" ]
then
        sudo rm -rf /data/web_static/current
fi
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -hR ubuntu:ubuntu /data
sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
service nginx restart
