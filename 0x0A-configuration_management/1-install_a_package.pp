# Install flask from pip3

package { 'python3-pip3':
  ensure => 'installed',
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install flask=2.1.0',
  unless  => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',
}
