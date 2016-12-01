# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|

  FileUtils.cp("#{Dir.home}/.ssh/id_rsa.pub", "key.pub")

  config.vm.provider "docker" do |d|
    d.build_dir = "."
    d.force_host_vm = false
    d.name    = "vagrant-docker-kolibri"
    # d.has_ssh = true
  end

  config.ssh.guest_port = 22
  config.ssh.username = "root"
  config.ssh.private_key_path = "#{Dir.home}/.ssh/id_rsa"

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  config.vm.network "forwarded_port", guest: 8080, host: 9080
  config.vm.network "forwarded_port", guest: 8000, host: 9000
  config.vm.network "forwarded_port", guest: 8010, host: 8010
  config.vm.network "forwarded_port", guest: 22, host: 2122

  config.vm.synced_folder ".", "/app"

end
