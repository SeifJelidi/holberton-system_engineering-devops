#fix in nginx
command => 'sed -i -e "$aULIMIT=\"-n 4096\" /etc/default/nginx;service nginx restart',
