kadm5.acl

控制哪些用户是管理员

主体规则定义了哪些主体（用户）可以拥有管理员权限。在规则中，使用 principal@realm 的格式指定主体。例如，*/admin@HADOOP.COM 表示任何拥有 admin 实例的主体在 HADOOP.COM 域中具有管理员权限。
权限规则指定了允许的操作。通常，使用通配符 * 表示允许执行所有操作