```shell
<olcRootPW> can only be set when rootdn is under suffix



change.ldif 需要在/etc/openldap/schema/ 下执行
```


* additional info: modify/add: olcRootPW: no equality matching rule

```
是因为之前已经设置密码了，修改就行
可将rootpwd.ldif文件内容中的add换成replace；
```

* additional info: value of single-valued naming attribute 'dc' conflicts with value present in entry

表明添加条目时出现了命名冲突。


dn: dc=inner,dc=fdstack,dc=com
objectClass: top
objectClass: dcObject
objectclass: organization
o: inner fdstack com
dc: inner  

注意上面dc写最后一个dc