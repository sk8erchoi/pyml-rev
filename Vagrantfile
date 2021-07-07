# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.box = "bento/ubuntu-20.04"

  config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.network "forwarded_port", guest: 8000, host: 8888

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get install -y apache2 php libapache2-mod-php
    apt-get install -y mysql-server libmysqlclient-dev
    apt-get install -y dos2unix
    apt-get install -y firefox fonts-nanum*
    apt-get install -y python3-pip
    sed 's/tensorflow/tensorflow-cpu/' /vagrant/requirements.txt > /tmp/requirements.txt
    pip install -r /tmp/requirements.txt
    SHELL

end
