# mesos-school
Experiments with Mesos

## Install dependencies
`sudo ansible-galaxy install -r requirements.yml`

## List of submodules:
`git submodule add git@github.com:AnsibleShipyard/ansible-zookeeper.git roles/ansible-zookeeper`

`git submodule add git@github.com:AnsibleShipyard/ansible-mesos.git roles/ansible-mesos`


### Hack for networking???
http://www.jamesbaltar.com/blog/set-default-network-interface-ubuntu
```
sudo ip route change to default dev usb0 via [gateway ip]

"ansible_eth1": {
            "active": true, 
            "device": "eth1", 
            "ipv4": {
                "address": "192.168.56.10", 
                "netmask": "255.255.255.0", 
                "network": "192.168.56.0"
            }, 
            "macaddress": "08:00:27:79:b7:5e", 
            "module": "e1000", 
            "mtu": 1500, 
            "promisc": false, 
            "type": "ether"
        }, 
        
        
        
default via 10.0.2.2 dev eth0 
10.0.2.0/24 dev eth0  proto kernel  scope link  src 10.0.2.15 
        
"ansible_eth0": {
            "active": true, 
            "device": "eth0", 
            "ipv4": {
                "address": "10.0.2.15", 
                "netmask": "255.255.255.0", 
                "network": "10.0.2.0"
            }, 
            "macaddress": "08:00:27:84:06:a3", 
            "module": "e1000", 
            "mtu": 1500, 
            "promisc": false, 
            "type": "ether"
        }, 
                
====
sudo ip route change to default dev eth1 via 192.168.56.0     

```