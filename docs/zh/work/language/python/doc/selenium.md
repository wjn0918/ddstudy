---
title: selenium
---

官网：https://googlechromelabs.github.io/chrome-for-testing/#stable
国内镜像:https://registry.npmmirror.com/binary.html?path=chrome-for-testing/



# element not interactable  元素不可交互

使用脚本执行

```
resp = requests.get(r'https://cdn.bootcdn.net/ajax/libs/jquery/3.5.1/jquery.min.js')
# 直接执行jquery源码
self.driver.execute_script(resp.content.decode())
time.sleep(2)

self.driver.execute_script("$(arguments[0]).click()",xpath)

```



# 操作打开的浏览器

```
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import subprocess

# 打开浏览器
subprocess.Popen("C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9527")


option = Options()
option.add_experimental_option("debuggerAddress", "localhost:9527")
driver = Chrome(executable_path=r"chromedriver.exe", options=option)

```


## 2

```
# Licensed to the Software Freedom Conservancy (SFC) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The SFC licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import base64
from selenium.webdriver.remote.command import Command
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.remote_connection import ChromeRemoteConnection
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import InvalidElementStateException

class MyWebDriver(RemoteWebDriver):
    """
    Controls the ChromeDriver and allows you to drive the browser.

    You will need to download the ChromeDriver executable from
    http://chromedriver.storage.googleapis.com/index.html
    """

    def __init__(self, command_executor, session_id):
        self.r_session_id = session_id
        RemoteWebDriver.__init__(self, command_executor=command_executor, desired_capabilities={})

    def start_session(self, capabilities, browser_profile=None):
        """
        重写start_session方法
        """
        if not isinstance(capabilities, dict):
            raise InvalidElementStateException("Capabilities must be a dictionary")
        if browser_profile:
            if "moz:firefoxOptions" in capabilities:
                capabilities["moz:firefoxOptions"]["profile"] = browser_profile.encoded
            else:
                capabilities.update({'firefox_profile': browser_profile.encoded})

        self.capabilities = Options().to_capabilities()
        self.session_id = self.r_session_id
        self.w3c = False

    def launch_app(self, id):
        """Launches Chrome app specified by id."""
        return self.execute("launchApp", {'id': id})

    def quit(self):
        """
        Closes the browser and shuts down the ChromeDriver executable
        that is started when starting the ChromeDriver
        """
        try:
            RemoteWebDriver.quit(self)
        except:
            # We don't care about the message because something probably has gone wrong
            pass
        finally:
            self.service.stop()

    def create_options(self):
        return Options()

```

```
import time

from selenium import webdriver

from my_remote_chrome import MyWebDriver


driver = webdriver.Chrome(executable_path='./chromedriver.exe')
executor_url = driver.command_executor._url
session_id = driver.session_id
driver.get("http://www.spiderpy.cn/")


print(session_id)
print(executor_url)


driver2 = MyWebDriver(command_executor=executor_url, session_id=session_id)

print(111111)
print(driver2.current_url)
driver2.get("https://www.baidu.com")

time.sleep(10)
```