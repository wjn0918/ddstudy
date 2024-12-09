https://editor.swagger.io/?spm=ding_open_doc.document.0.0.2b2b6534XEe5of


```
openapi: 3.0.1
info:
  title: 测试接口
  description: 测试openapi
  version: 1.0.0
servers:
  - url: http://120.26.77.177:8012
paths:
  /api/ai/receive_answer:
    get:
      description: 测试openapi
      summary: 测试openapi
      operationId: openapiCS
      parameters:
        - name: location
          in: query
          description: 地区
          required: false
          schema: 
            type: string
        - name: date
          in: query
          description: 日期
          required: false
          schema: 
            type: string
      responses:
        200:
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/openapiCSResponse'
components:
  schemas:
    openapiCSResponse:
      type: object
      properties:
        status:
          type: string
          description: 状态

```