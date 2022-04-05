# API docs



## Log in

1. 发送给后端用户名和密码
2. 需要从后端接收传user ID



## Register

1. 发送给后端用户名和密码
2. 需要从后端接收true/false



## Project

1. 初始化页面
   1. 前端发送给后端一个request信息（user ID）
   2. 后端传project list (ID, project_name, time)
   3. 前端完成初始化页面

2. 搜索
   1. 前端发送用户输入的搜索关键字 (user id+project_name)
   2. 后端根据关键字返回合法的project list (ID, project_name, time)
   3. 前端重新加载
3. 删除
   1. 前端发送用户选择 (user id+project_name)
   2. 后端根据关键字返回合法的project list (ID, project_name, time)
   3. 前端重新加载
4. 新建
   1. 前端发送 (user id+project_name, time)
   2. 后端返回合法的project list (ID, project_name, time) + bool
   3. 前端重新加载
5. 上传
   1. 前端传json文件+(user id+project_name, time)
   2. 后端返回合法的project list (ID, project_name, time)+ bool
   3. 前端重新加载
6. 下载
   1. 前端传ID+user id
   2. 后端传json文件
   3. 下载



## Profile

1. 初始化页面

   1. 前端发送给后端一个request信息（用户ID）

   2. 后端传user list

   3. 前端完成初始化页面



## Canvas

1. 初始化页面

   1. 前端发送给后端一个request信息
   2. 后端传json + python

   3. 前端完成初始化页面

2. Compile
   1. 前端传给后端json
   2. 后端返回bool
3. 下载
   1. 前端传ID
   2. 后端传json文件
   3. 下载



## Canvas/Train

1. 初始化页面

   1. 前端发送给后端一个request信息（session模型信息ID）

   2. 后端传json（参数信息） + txt（训练信息）

   3. 前端完成初始化页面

2. apply
   1. 前端发送给后端参数信息
   2. 后端返回bool
3. 润
   1. 前端发送要润的信息
   2. 定时调用init
4. 传数据集
   1. 前端传csv
   2. 后端返回bool





## Template

1. 初始化页面

   1. 前端发送给后端一个request信息

   2. 后端传project list (ID, project_name, author, stars)【分享区】
   3. 后端传project list (ID, project_name, author, stars)【推荐区】
   4. 后端传star list

   3. 前端完成初始化页面

2. 搜索
   1. 前端发送用户输入的搜索关键字 (根据project_name搜索)
   2. 后端根据关键字返回合法的project list (ID, project_name, time)
   3. 前端重新加载
3. Star
   1. 前端发送ID
   2. 初始化页面
