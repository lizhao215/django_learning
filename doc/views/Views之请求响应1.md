### get和post区别 ###
* get在url中 ，url长度不能超过2k

		127.0.0.1:8000/user/register/?username=admin&paswword=admin
* post在请求体

			请求行
			请求头
			请求空行
			请求体	（username=admin&paswword=admin）
* request.GET和request.POST都是QueryDict的实例
### *agrs和**kwargs ###
* 位置参数
* 关键字参数

### 注册 ###
* UNIQUE constraint failed: User_user.username
* 异常转换
 * 数据中报的是唯一性约束异常
 * 转换成UserExistException
### 重定向 ###
* 302 让浏览器重新发起请求，在响应头中会有location告诉浏览器在服务器找谁？
 * /user/register/
 * 响应头是
			
				HTTP/1.0 302 Found
				Date: Mon, 30 Oct 2017 02:02:09 GMT
				Server: WSGIServer/0.1 Python/2.7.13
				X-Frame-Options: SAMEORIGIN
				Content-Type: text/html; charset=utf-8
				Location: /user/
				Content-Length: 0  
 * 发现响应头中的location字段，name浏览器就知道接着去找谁了
 * 浏览器刷新意味着再一次执行浏览器上一次操作
### 文件上传 ###
* enctype="multipart/form-data"
* 加上时间戳去重
* request.FILES    InMemoryUploadedFile


				  username =   request.POST.get('username')
				    file = request.FILES.get('headimg')
				    # InMemoryUploadedFile()
				    name = file.name[:file.name.index(r'.')]+str(time.time()*1000)+file.name[file.name.index(r'.'):]
				    fw = open(os.path.join(BASE_DIR,name),'wb')
				    fw.write(file.read())
				    fw.close()
				    return  HttpResponse('上传成功')
* .chunks() 片段（读一部分，写一部分）


					  username =   request.POST.get('username')
					    file = request.FILES.get('headimg')
					    # InMemoryUploadedFile()
					    name = file.name[:file.name.index(r'.')]+str(time.time()*1000)+file.name[file.name.index(r'.'):]
					    fw = open(os.path.join(BASE_DIR,name),'wb')
					    for part in file.chunks():
					        fw.write(part)
					    fw.close()
					    return  HttpResponse('上传成功')

* with as

			  username =   request.POST.get('username')
			    file = request.FILES.get('headimg')
			    name = file.name[:file.name.index(r'.')]+str(time.time()*1000)+file.name[file.name.index(r'.'):]
			    with open(os.path.join(BASE_DIR,name),'wb') as fw:
			        for part in file.chunks():
			            fw.write(part)
			    return  HttpResponse('上传成功')
### request ###
* get数据
* post数据
* 文件数据
### cookie ###
* 客户端存储技术
 *  cookie是存在浏览器的
 *  广告
 *  获得cookies  COOKIES 【字典】
 *  所有的字典的操作get,items,['']
* 如何写一个cookies
 * response.set_cookie() 写cookie 
 * key,value
 * 过期时间 （expires）如果过期就自动删除，不过期的话访问服务器的时候并且在同一路径下会自动携带cookie的值
 * 回话结束 浏览器关了 
 * max_age = 60*10  10分钟
 * path  路径 路径相同会自动携带 （path） path='/user/'
 * 当你访问127.0.0.1:8000/user/***  子路径也算
 * 域名要相同
* 什么时候会携带cookie
 * cookie没有过期
 * 相同path
 * 相同域名
* 悬浮广告 
* cookies的第一应用
 * 保存商品的浏览记录（调整顺序和去重）
* cookies小结
 * cookies 所有对字典的操作都可以对cookie
 * cookie的五个属性 key,value,expries,path,domain
 * 从request.COOKIES获得cookie
  * cookie的过期时间None（会话结束就删除。（浏览器关闭）），正数（多少时间过期）
 * 从response.set_cookie存储cookie 
 * 能不能使用cookie保存用户的账号和密码？不行。（cookie不能存储敏感信息，而且存储大小和存储数量邮箱）
* session（会话）
 *  服务器的一种存储技术
 *  加入购物车，免登陆
 * 默认session会在数据库中有一张表 
 * request.session获得session
* session详解
 * session   from  django.contrib.sessions.backends.db import SessionStore
 * session是基于cookie的
 * 关键是sessionid 不重复

			![](https://i.imgur.com/4P326bw.png)
 * 将对象转换成字符串（序列化）
  *  {'username':'admin','password':'admin'}
 * session中不能存储自定义对象，如果存储需要转换成json对象
* 对象是有什么组成的
 *  父类的__dict__+本类的__dict__+对象的__dict__
### session中存储字典 ###
* 出问题
* session过期时间
* 清空session
* 删除session没讲
* session购物车


