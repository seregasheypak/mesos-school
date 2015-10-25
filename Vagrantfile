# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  if Vagrant.has_plugin?("vagrant-cachier")
    # Configure cached packages to be shared between instances of the same base box.
    # More info on the "Usage" link above
    config.cache.scope = :box
    config.cache.enable :apt
  end

  config.vm.box = "ubuntu/trusty64"
  config.vm.box_url = "https://atlas.hashicorp.com/ubuntu/boxes/trusty64"

  if Vagrant.has_plugin?("vagrant-cachier")
    config.cache.scope = :box
  end

  config.vm.define "mesosnode01" do |node1|
    node1.vm.box = "ubuntu/trusty64"
    node1.vm.hostname = "mesosnode01"
    node1.vm.network  "private_network", ip: "192.168.56.10"
    config.vm.provider "virtualbox" do |vb|
      vb.customize ["modifyvm", :id, "--memory", "3072"]
    end
  end

  config.vm.define "mesosnode02" do |node2|
    node2.vm.box = "ubuntu/trusty64"
    node2.vm.hostname = "mesosnode02"
    node2.vm.network  "private_network", ip: "192.168.56.11"
    config.vm.provider "virtualbox" do |vb|
      vb.customize ["modifyvm", :id, "--memory", "3072"]
    end
  end

  config.vm.define "mesosnode03" do |node3|
    node3.vm.box = "ubuntu/trusty64A"
    node3.vm.hostname = "mesosnode03"
    node3.vm.network  "private_network", ip: "192.168.56.12"
    config.vm.provider "virtualbox" do |vb|
      vb.customize ["modifyvm", :id, "--memory", "3072"]
    end
  end

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "playbook.yml"
    ansible.inventory_path = "hosts"
  end

  # config.vm.provision "ansible" do |ansible|
  #   ansible.playbook = "playbook.yml"
  #   ansible.groups = {
  #     "dse" => ["dsenode01","dsenode02","dsenode03"],
  #     "opscenter" => ["dsenode04"],
  #     "sparkmasters" => ["dsenode01"],
  #     "sparkworkers" => ["dsenode01","dsenode02","dsenode03"],
  #     "sparkjobserver" => ["dsenode02"],
  #     "sparkhistory" => ["dsenode02"],
  #     "graphite" => ["dsenode03"],
  #     "grafana" => ["dsenode03"],
  #   }
  # end

end
