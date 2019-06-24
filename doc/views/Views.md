###web的访问流程  ###
* 输入url
* 根据域名找ip
 * 现在hosts文件   c:/windows/system32/drivers/etc/hosts
 * DNS (防止假的域名服务器，wifi)
*  发起http请求
 * 找到主机（ip）
 * 找到监听80端口的程序
	
	![](https://i.imgur.com/EDe9h4X.png)
 * TCP/UDP 传输层协议
 * ip 网络层
 * http属于应用层
 * tcp/ip 网络传输层，协议簇
* 服务器处理
* 服务器返回数据
* 浏览器下载到本地
* 浏览器渲染   
### url  ###
* url uniform resouces location(统一资源定位符)，http
* url格式
 * http://www.baidu.com:80/query/2015/10/9/?keyword=美女&type=图片 
 * 协议:主机:端口/路径?参数
 * 协议：http
 * 主机：www.baidu.com
 * 端口:80
 * 路径:query/2015/10/9/
 * 参数：keyword=美女 
* uri uniform resouces Identifier (统一资源标识符)，uri是url超集：file://文件地址
### Django url解析流程 ###
* 解析的路径，通过<font color='red'>正则</font>匹配<font color='red'>路径</font>找到相应的调用函数
* 先找根urls，根路由（settings里面有一个ROOT_URLCONF）
 * 第一件事是正则匹配，
 * 匹配的顺序 
 * 匹配规则一定要准确

	![](https://i.imgur.com/bUTm8O1.png)


	![](https://i.imgur.com/uttL9gK.png)
### 具名捕获 ###
* page/(\d+)  定义的view函数除了request，还会传递捕获的字符串
 * 所有参数，还有捕获传递的都是字符串 
* 具名：(?P<categoryId>\d+) 关键字传递参数
* 默认参数

			def index(request,num=0):
	    return HttpResponse('我是page'+num+'页面')


			    url(r'^page/(\d+)$',views.index),
   				 url(r'^page/$',views.index),
* url的第三个参数也可以传递值

			url(r'^page/$',views.index,kwargs={'num':'10'}),
### 错误界面 ###
* DEBUG=FALSE
* ALLOW_HOSTS=['127.0.0.1']
 * ALLOWED_HOSTS = [
   '*'
] 
* 在templates里面定义
 * 500.html  服务器出问题了
 * 404 
 * 403 （没有权限） 
 * 400 （HttpBadRequest）
### Fiddler的简单使用 ###
![](https://i.imgur.com/kv6BYH0.png)

### http网络请求 ###
* http协议特点：无状态
 * http一旦请求完成，下次再请求服务器，服务器就不认识client 
 * 头（请求头，响应头）头里面携带了服务器和客户端沟通的信息
* 请求

		#请求头中的信息都是给服务器看的
		GET http://127.0.0.1:8000/ HTTP/1.1  请求行：请求方式 主机  协议
		**Host: 127.0.0.1:8000
		Connection: keep-alive 保持较短时间连接，反复和服务器通讯，给服务器看的
		User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36 客户端信息 给服务器看的 
		Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/ webp,image/apng,*/*;q=0.8 客户端能够显示的信息  给服务器看的
		Accept-Encoding: gzip, deflate, br 压缩的方法
		Accept-Language: zh-CN,zh;q=0.9
		Cookie: name1="2|1:0|10:1508218301|5:name1|8:5byg5LiJ|c9d2e2a9c7618a9f7d9577a0d08465781bc8e88c86cc5652457e0328dfb3d937"; csrftoken=sguSgAQGDpWlhm7wE7N0yaP8t2vSHNKFfmhZxPPkLIQAG72EMvsMa4Ec055j04jB**请求头
		
			请求空行
			请求体（POST）
 	
* 响应


		HTTP/1.0 200 OK 响应行:协议 状态码 状态描述
		Date: Fri, 27 Oct 2017 06:48:23 GMT 
		Server: WSGIServer/0.1 Python/2.7.13 服务器版本
		X-Frame-Options: SAMEORIGIN  网页中能不能显示iframe:SAMEORIGIN(只能显示自己域名下的iframe)
		Content-Type: text/html; charset=utf-8   （文本的类型）
		Content-Length: 12   （响应体长度）
		     响应空行
		我是百度   （响应体）
					
* 行,头，体
* http请求方式
 * get (查找)  好多浏览器会缓存get请求信息。
 * post (修改/添加)
 * delete (删除)
 * put
 * CONNECT
 *  PATCH
 *  HEAD
 *  ....
### request请求 ###
* request对象封装了刚刚请求信息
* request.META 描述信息
* 都有在浏览器（url），超链接都是GET请求方法
* GET 
 * 参数  http://127.0.0.1:8000/?name=%E5%BC%A0%E4%B8%89 放在url后面  
 * request.GET.get('key')
 * request.GET.keys() 获得查询参数中所有key
 * request.GET.values() 获得查询参数中所有的values
 * request.GET.getlist() 多个值
 * 'age' in request.GET
 * QueryDict 查询字典
 * get请求的查询参数放在url里面。url请求参数长度不能超过2k
* POST
 * 查询参数放在请求体 

			POST http://127.0.0.1:8000/search HTTP/1.1
			Host: 127.0.0.1:8000
			Connection: keep-alive
			Content-Length: 67
			Cache-Control: max-age=0
			Origin: http://127.0.0.1:8000
			Upgrade-Insecure-Requests: 1
			Content-Type: application/x-www-form-urlencoded
			User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36
			Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
			Referer: http://127.0.0.1:8000/
			Accept-Encoding: gzip, deflate, br
			Accept-Language: zh-CN,zh;q=0.9
			Cookie: name1="2|1:0|10:1508218301|5:name1|8:5byg5LiJ|c9d2e2a9c7618a9f7d9577a0d08465781bc8e88c86cc5652457e0328dfb3d937"; csrftoken=sguSgAQGDpWlhm7wE7N0yaP8t2vSHNKFfmhZxPPkLIQAG72EMvsMa4Ec055j04jB
			
			keyword=meinv&options=%E5%B9%B4%E8%BD%BB&options=%E6%88%90%E7%86%9F  请求体
![](https://i.imgur.com/njvkmqA.png)
 * QueryDict get请求里面的方法在POST中统统适用


