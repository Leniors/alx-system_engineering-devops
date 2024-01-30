# 2-puppet_custom_http_response_header.pp

$nginx_conf = '/etc/nginx/sites-available/default'

class { 'nginx':
  package_name => 'nginx',
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}

file { '/etc/nginx/sites-enabled/default':
  ensure  => file,
  notify  => Service['nginx'],
}

exec { 'add_custom_header':
  command => "/bin/sed -i '/^[[:space:]]*server {/a\\\\tadd_header X-Served-By \$(hostname);' ${nginx_conf}",
  path    => ['/bin', '/usr/bin'],
  require => Class['nginx'],  # Ensure Nginx is installed before running this exec
}
