# update_ssh_config.pp

package { 'augeas-tools':
  ensure => installed,
}

$ssh_config_path = '/root/alx-system_engineering-devops/0x0B-ssh/3-ssh_config'

file_line { 'update_ssh_config':
  path    => $ssh_config_path,
  line    => '    StrictHostKeyChecking ask',
  match   => '^#   StrictHostKeyChecking ask',
  ensure  => present,
}
