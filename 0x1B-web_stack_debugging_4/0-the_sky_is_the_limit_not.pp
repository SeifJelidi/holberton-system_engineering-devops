#fix in nginx
exec { 'fix':
  command => 'sed -i s/15/2000/ /etc/default/nginx',
   path    => ['/bin/']
}
