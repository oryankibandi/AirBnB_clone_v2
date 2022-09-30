#!/usr/bin/env bash
# sets up web servers for deployment

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/ /data/web_static/shared/ /data/web_static/current/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
sudo echo Holberton School > /data/web_static/releases/test/index.html
sudo ls -s /data/web_static/current /data/web_static/releases/test/
chown -R $USER /data/
chown -R $USER /data/
echo "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }
    location /redirect_me {
        return 301 http://cuberule.com/;
    }
    location /hbnb_static {
        alias /data/web_static/current/;
        autoindex off;
    }
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}"

sudo systemctl restart nginx
