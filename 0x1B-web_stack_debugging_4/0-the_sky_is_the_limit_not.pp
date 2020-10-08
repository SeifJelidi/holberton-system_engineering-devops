#fix in nginx
exec { 'fixing':
echo "fixing"
command => 'sed -i' "s/15/2000/" '/etc/default/nginx',
path    => ['/bin/']
}

exec { 'restart_server':
echo "restart"
command  => 'service nginx restart',
}

