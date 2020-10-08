#fix in nginx
command => 'sed -i -e "s/15/2000/" /etc/default/nginx;service nginx restart',
