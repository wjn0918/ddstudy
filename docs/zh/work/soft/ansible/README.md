---
title: Ansible
---



ansible --version 
查看配置文件是否配置成功
- 运行shell

```
ansible all -i hosts.yml -m shell -a "ls /"
```


```
yum install sshpass
```

## [inventories](https://docs.ansible.com/ansible/latest/inventory_guide/index.html)


```
<!-- @include: hosts.yml -->
```

