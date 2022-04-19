# Instalo un paquete mas no si sirve.

package { 'flask':
    ensure   => '2.1.0',
    provider => pip3,
}
