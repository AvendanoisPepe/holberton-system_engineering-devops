# Instalo un paquete mas no si sirve.

package { 'puppet-lint':
    ensure   => '2.5.0',
    provider => 'gem',
    source   =>  'https://rubygems.org/gems/puppet-lint/versions/2.5.0'
}
