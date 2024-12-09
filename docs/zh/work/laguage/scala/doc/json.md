```
import net.liftweb.json._
import net.liftweb.json.JsonDSL._

object LiftJsonExample {
  implicit val formats = DefaultFormats

  def main(args: Array[String]): Unit = {
    val jsonData =
      """
        |{
        | "age": [
        |   {
        |   "age": "111"
        |   }
        | ],
        | "sex": 1
        |}
      """.stripMargin

    val json = parse(jsonData)
    val ga = json.extract[GA]
    println(ga)
  }

  case class GA(age: List[GB], sex: Int)
  case class GB(age: String)
}

```



*  A needed class was not found. This could be due to an error in your runpath. Missing class: scala/tools/scalap/scalax/rules/scalasig/Type

检查case class 的数据类型和json 不匹配



# 更改内容


```
    var body =
      """
        |{
        |    "status": 1,
        |    "pageNo": 1,
        |    "pageSize": 2
        |}
        |""".stripMargin

    implicit val customFormats: Formats = DefaultFormats
    val value: json.JValue = parse(body)
    val value1 = value transformField {
      case JField("pageNo", JInt(x)) => JField("pageNo", JInt(x+1))
      case other => other
    }
    val str = compactRender(value1)
    print(str)
```
