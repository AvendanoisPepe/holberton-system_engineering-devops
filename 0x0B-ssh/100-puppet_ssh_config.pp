# PPFile that config ssh_config file.
include stdlib

file_line { 'Esta mierda no funcuina':
  path =>  '/etc/ssh/ssh_config',
  line =>  'PasswordAuthentication no',
}

file_line {  'modo sad':
  path =>  '/etc/ssh/ssh_config',
  line =>  'IdentityFile ~/.ssh/school',
}
