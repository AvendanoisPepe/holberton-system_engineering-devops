# Se crea un archivo en la ruta de 'file' y no se si sirve.

file { '/tmp/school':
    ensure  => 'present',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet',
}
