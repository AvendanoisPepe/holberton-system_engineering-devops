# Instalo un paquete mas no si sirve.

package { 'puppet-lint':
    ensure   => '2.5.2',
    provider => 'gem',
}
