---
title: alertManager
---


## [alertmanager](https://github.com/prometheus/alertmanager/releases)


## 测试

```
curl -X POST http://localhost:9093/api/v2/alerts \
  -H "Content-Type: application/json" \
  -d '[{
    "labels": {
      "alertname": "HighCPU",
      "instance": "server1:9100",
      "severity": "critical"
    },
    "annotations": {
      "description": "CPU usage超过95%"
    },
    "startsAt": "2023-07-20T12:00:00Z"
  }]'
```


```
route:
  receiver: 'webhook'
  
receivers:
- name: 'webhook'
  webhook_configs:
  - url: 'http://localhost:5000/alert'  # 自定义Webhook接收地址
    send_resolved: true                   # 发送恢复通知
    # http_config:
    #   bearer_token: 'your-auth-token'     # 可选认证
    max_alerts: 10                        # 单次请求最大告警数
```

Alertmanager 会将相同标签的告警合并为一个通知组，默认 group_wait: 30s（首次等待）和 group_interval: 5m（重复间隔）

```
route:
  receiver: 'webhook'
  group_by: ['alertname']  # 按告警名称分组
  group_wait: 1s          # 立即发送首次告警
  group_interval: 1s      # 每组告警间隔1秒
  repeat_interval: 1s     # 相同告警重复间隔

receivers:
- name: 'webhook'
  webhook_configs:
  - url: 'http://localhost:5000/alert'
    send_resolved: true
    max_alerts: 10
```


## email 告警通知

```
{{ define "custom.email.html" }}
<!DOCTYPE html>

    <h1>hello world</h1>
</html>

{{ end }}
```


```
global:
  resolve_timeout: 5m
  smtp_from: ''
  smtp_smarthost: 'smtp.qq.com:465'
  smtp_auth_username: ''
  smtp_auth_password: ''  # 邮箱授权码（非登录密码）
  smtp_require_tls: false               # SSL，此处设为false
  smtp_hello: '163.com'

templates:
  - './hello.html'

route:
  receiver: 'email-notice'

receivers:
- name: 'email-notice'
  email_configs:
  - to: 'wangjn@shingi.cn'
    send_resolved: true                 # 发送问题解决通知
    headers:
      Subject: '【报警】{{ .CommonLabels.alertname }}'
    html: '{{ template "custom.email.html" . }}'
```