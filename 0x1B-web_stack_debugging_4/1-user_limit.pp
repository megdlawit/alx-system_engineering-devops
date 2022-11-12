# OS configuration user limit
exec { 'Correct hard':
  command  => 'sudo sed -i \'s/nofile 5/nofile 3000/\' /etc/security/limits.conf',
  provider => shell,
}
exec { 'Correct soft':
  command  => 'sudo sed -i \'s/nofile 4/nofile 1000/\' /etc/security/limits.conf',
  provider => shell,
}
