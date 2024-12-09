# 设置别名

Set-Alias name command

Get-Alias



$ENV:path -split ":"

# 注册function

```

# PowerShell 配置文件
notepad $PROFILE

# 添加您的函数定义

function ssh-copy-id([string]$userAtMachine, $args){   
    $publicKey = "$ENV:USERPROFILE" + "/.ssh/id_rsa.pub"
    if (!(Test-Path "$publicKey")){
        Write-Error "ERROR: failed to open ID file '$publicKey': No such file"            
    }
    else {
        & cat "$publicKey" | ssh $args $userAtMachine "umask 077; test -d .ssh || mkdir .ssh ; cat >> .ssh/authorized_keys || exit 1"      
    }
}


# 重新加载配置文件中的更改

. $PROFILE
```