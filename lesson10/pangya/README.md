## 作业10

```
1. 用form的action方式实现资产添加的功能；


实现：
1，当点击“添加”按钮，跳转链接/assets/addpage，匹配调用addPageAssetsView函数
2，addPageAssetsView函数使用render函数渲染assets_add_page.html页面
3，在assets_add_page.html页面填写相关资产信息后，点击提交按钮，表单动作为跳转到/assets/add/，匹配调用addAssetsView函数
4，addAssetsView函数用request.GET.get前端的资产信息，通过ORM操作添加到数据库，将添加成功的信息返回给前端

```
 
