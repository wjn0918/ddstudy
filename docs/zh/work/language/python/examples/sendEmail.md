---
title: 发送email
---


```
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


def send_email_via_163_to_qq():
    # 配置信息
    smtp_server = "smtp.163.com"  # 163 SMTP服务器地址
    smtp_port = 25  # 非SSL端口(25)或SSL端口(465/994)
    sender_email = ""  # 你的163邮箱地址
    password = ""  # 163邮箱授权码(不是密码)
    receiver_email = ""  # 接收方QQ邮箱

    # 创建邮件内容
    message = MIMEMultipart()
    message["From"] = Header(f"{sender_email}")  # 发件人显示名称
    message["To"] = Header(f"{receiver_email}")  # 收件人显示名称
    message["Subject"] = Header("Python邮件测试", "utf-8")  # 邮件主题

    # 邮件正文内容 (支持HTML)
    body = """
    <h1>这是一封测试邮件</h1>
    <p>来自Python脚本通过163邮箱发送到QQ邮箱的测试内容</p>
    <p>当前时间：{}</p>
    """.format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    message.attach(MIMEText(body, "html", "utf-8"))

    try:
        # 连接SMTP服务器 (三种连接方式选其一)

        # 方式1: 普通非加密连接 (不推荐)
        # server = smtplib.SMTP(smtp_server, smtp_port)

        # 方式2: SSL加密连接 (推荐)
        server = smtplib.SMTP_SSL(smtp_server, 465)

        # 方式3: STARTTLS加密 (先建立普通连接再升级)
        # server = smtplib.SMTP(smtp_server, smtp_port)
        # server.starttls()

        # 登录服务器
        server.login(sender_email, password)

        # 发送邮件
        server.sendmail(sender_email, [receiver_email], message.as_string())
        print("邮件发送成功！")

    except smtplib.SMTPException as e:
        print(f"邮件发送失败: {str(e)}")
    finally:
        server.quit()  # 关闭连接


if __name__ == "__main__":
    from datetime import datetime

    send_email_via_163_to_qq()

```