#fix in nginx
command => 'sed -i "s/15/2000/" /etc/default/nginx;service nginx restart',
path    => '/bin/',
