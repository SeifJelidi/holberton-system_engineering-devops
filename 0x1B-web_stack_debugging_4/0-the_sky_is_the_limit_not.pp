#fix in nginx
command => 'sed -i -e "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 2000\"/g" /etc/default/nginx;service nginx restart',
