---
title: sed
---


* 包含空格

使用\s*

sed -i 's/PASS_MAX_DAYS\s*99999/PASS_MAX_DAYS 90/' /etc/login.defs