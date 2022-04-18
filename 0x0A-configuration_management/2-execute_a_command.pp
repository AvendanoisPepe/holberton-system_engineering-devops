# Terminamos un proceso mas no se si sirva

exec { 'killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin/',
}
