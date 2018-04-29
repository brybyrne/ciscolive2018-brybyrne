# -*- mode: ruby -*-
# vi: set ft=ruby :


Vagrant.configure("2") do |config|
  config.vm.box = "iosxe/16.08.01"

  # IOS XE 16.7+ requires virtio for the network adapters.
  config.vm.network :private_network, virtualbox__intnet: "link1", auto_config: false, nic_type: "virtio"
  config.vm.network :private_network, virtualbox__intnet: "link2", auto_config: false, nic_type: "virtio"

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  # config.vm.provision "shell", inline: <<-SHELL
  #   apt-get update
  #   apt-get install -y apache2
  # SHELL
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "ansible/cl_startup_playbook.yml"
    ansible.inventory_path = "ansible/hosts.ini"
  end

end
