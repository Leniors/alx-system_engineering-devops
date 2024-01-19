# Install flask from pip3

package { 'python3-pip':
  ensure => 'installed',
}

exec { 'install_flask':
  command => 'pip3 install flask=2.1.0',
  path    => ['/bin', '/usr/bin']
  unless  => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',
}
