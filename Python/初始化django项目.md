### 一、初始化项目：`django-admin startproject [项目名称]`
项目结构： 
    ```
        mysite/                     # 项目容器，名称任意
            manage.py               # 用来跟django项目对接的命令行工具
            mysite/                 # Python包
                __init__.py         # 有这个文件目录才能称做包
                settings.py         # 设置django项目
                urls.py             # 路由，进行请求转发  重点
                wsgi.py             # web服务器
    ```


### 二、运行测试项目：`python3 manage.py runserver [ip]:[port]`

### 三、创建应用程序目录结构：`python3 manage.py startapp [应用程序名]`
应用程序结构：
    ```
        polls/
            __init__.py                # 有这个文件目录才能称做包
            admin.py                   # 注册模型
            apps.py                    
            migrations/                # 子包
                __init__.py            # 有这个文件目录才能称做包
            models.py                  # 创造模型，通过该模型创建对应的数据库表
            tests.py                   # 测试函数
            views.py                   # 视图
    ```

### 五、创建后台管理人员账户： `python3 manage.py createsuperuser`

### 六、MVT结构
1. 请求访问路由，通过路由映射到对应应用程序的视图
2. 视图（T）调用模型(M)对请求进行处理，并通过模板（T）进行渲染
3. 最后返回相应给浏览器

### 七、项目启动应用：
1. 配置`INSTALLED_APPS = [应用程序、应用程序...]` *<font size=2>放在这里的应用程序进行数据库迁移</font>*
