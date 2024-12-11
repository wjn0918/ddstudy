---
title: vagrant
---


config.vm.network "public_network", ip: "192.168.3.90"

config.vm.provider "virtualbox" do |v|
  v.memory = 8000
  v.cpus = 2
end