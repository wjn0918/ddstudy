---
title: subprocess
---

## 执行shell命令

```
try:
    result = subprocess.run(['ls', '-l'], capture_output=True, text=True, check=True)
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print(f'Error occurred: {e}')
```


## 执行java

```
cmd = ['java', '-cp /home/soft/schooletl/conf:/home/soft/schooletl/lib/* cn.shingi.schooletl.jobs.batch.SyncFaceJob', jobNo]
cmd = ' '.join(cmd)
print(f"执行：{cmd}")
result = subprocess.run(cmd, capture_output=True, text=True, check=True, shell=True)
```