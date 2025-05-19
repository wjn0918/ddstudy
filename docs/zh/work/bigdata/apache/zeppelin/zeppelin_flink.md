


# 调用hik

```

%flink

import scala.collection.JavaConverters._
import com.hikvision.artemis.sdk.ArtemisHttpUtil
import com.hikvision.artemis.sdk.config.ArtemisConfig

ArtemisConfig.host="192.168.3.214:443"
ArtemisConfig.appKey="24902513"
ArtemisConfig.appSecret="kiSd4eZ34DfR4EP7cOND"


var contentType = "application/json"
var header: Map[String, String] = _
val path = Map("https://" -> "/artemis/api/resource/v2/person/advance/personList")
val body = """
{"pageNo": 1, "pageSize": 1000}
"""

val result = ArtemisHttpUtil.doPostStringArtemis(path.asJava, body, null, null,
                    contentType, header.asJava)

print(result)
```



