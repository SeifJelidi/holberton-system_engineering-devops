#fix in nginx
exec { 'fixing':
command => 'sed -i' "s/15/2000/" '/etc/default/nginx',
path    => ['/bin/']
}

exec { 'restart_server':
command  => 'service nginx restart',
}

