# killing a process

exec { 'killmenow_process':
  command => 'pkill -f killmenow',
  path    => ['/bin', '/usr/bin'],
  onlyif  => 'pgrep -f killmenow',
}
