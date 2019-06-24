### MVC        V ###
### django和tornado区别 ###
* 性能
 * 多线程或者多进程
 *  django使用的是（ 多线程或者多进程）
 *  tornado使用的是协程（微线程），协程性能非常高（没有线程这种上下文创建，切换的开销）yield
* 功能
 * django 大而全（什么都有）（定制太困难了）
 
			后台(admin) 
			orm(对象关系映射类库)
			session
 * tornado 小而精 （轻量级）什么也没有 
 * tornado 单线程异步分阻塞（node.js）
 * tornado适用场景


			高并发，长连接
### http协议版本 ###
* http 1.0
 * 连接->请求->响应->关闭
 *  Connection:keep-alive(告诉服务器要做长连接)
* http1.1
 *   连接->请求->响应->请求->响应->关闭
### web服务器c10k ###
*  如果是软件的话，用的人越多，公司成本越低（越容易盈利）
*  360云盘
 * 用的人越多，涉及到硬盘（硬件），成本越高， 360云盘夭折了  
* 同时连接当达到1万的并发的时候，我们就需要加服务器了（成本）
* nginx
  *  缓存static文件（static文件全部交给nginx处理）
  *  逆向解析（127.0.0.0:80）-->8081
  *  负载均衡
  
		![](https://i.imgur.com/lmlc2Nx.png) 
* tornado 性能比高3倍左右
### 新互联公司 ###
* python，---》web，爬虫，大数据，--》人工智能

### tornado单线程异步分阻塞 ###
* 代码

			# 处理网络请求的	
			class IndexHandler(tornado.web.RequestHandler):
				# get请求
			    def get(self):
					# 输出响应体
			        self.write('hello world')

				#Application 其实是一个设置的容器
				app = tornado.web.Application([
					    (r'/',IndexHandler)
					])
				# 绑定端口（调用了HttpServer）
				app.listen(8000)
				# 死循环（从epoll中获得需要操作的socket）
				tornado.ioloop.IOLoop.instance().start()
* epoll
 * 客户端socket的储存的容器 

* 原理图
 * epoll
 * 单线程异步非阻塞
 

![](https://i.imgur.com/rjbAH5F.png)

### 步骤 ###
* 清理类（RequestHandler）
* Application对象 （很多设置）
* app.listen(8000) 绑定端口，创建服务器
* ioLoop.start（不断的从epoll中读取要处理的客户端socket）

### 为什么tornado能处理高并发，长连接 ###
* 长连接（epoll容器存储起来了）	
* 高并发（使用的是协程，没有线程创建和线程上下文切换开销）		



					def printa():
						while True:
						yield 'a'
						
					
					def printb():
						while True:
						yield 'b'
					while True:
						pirnta()
						printb()

					abababababab

### tornado特性 ###
* 单线程
* 异步（协程）
* 非阻塞

							
###  查询参数 ###
* get/post
 * get  get_query_argument  get_query_arguments 
 * post get_body_argument get_body_arguments
 * 缩写 get_argument  get_arguments(通用的)
 * 捕获  
 
			 (r'/time/(\d+)/(\d+)/(\d+)',TimeHandler) 
			  def get(self,year,month,day):
			 可以具名捕获
			(r'/time/(?P<month>\d+)/(?P<year>\d+)/(?P<day>\d+)'
					
 * self.write(响应体)
			
* file，大文件
				

### 查询I(Input) ###
* get_argument 获得get/post参数
* 捕获/具名捕获
* self.request.files 上传多个文件
* self.request.headers 请求头
* self.request.remote_ip 获得客户端ip

###  输出O(Output) ###
* write () 响应体
* add_header()添加响应头
* set_status 设置状态码
* 自定义重定向

		class RedirctHandler(tornado.web.RequestHandler):
		    def get(self, *args, **kwargs):
		        # self.set_status(404,'照比到了')
		        self.set_status(302,'FOUND')
		        self.add_header('LOCATION','http://www.bjsxt.com')
 * 重定向（302,301）self.redirct(地址)
 * 301 永久重定向，
 

				(r'/hello',tornado.web.RedirectHandler,{"url": "http://www.bjsxt.com"}  			
 * set_cookie 
  

			        self.set_cookie('sessionid',uuid.uuid4().get_hex(),expires=datetime.datetime.utcnow()+ datetime.timedelta(minutes=30),path='/asd')
 * get_cookie

### 生命周期 ###	
* initialize--》prepare-->get/post-->on_finish	
* initialize和on_finish是一对，如果说initialize初始化工作,on_finish是清理功能。
* url中 (r'/',Handler,字典，name)    #字典是给Handler中的initialize方法的
* write_error 出错之后，会自动调用
* set_default_headers
 *  write_error和set_default_headers 一般写在父类中，设置通用的响应头

### url路由 ###
* 元组
* URLSpec
 * 正则,处理类，初始化参数，名字(self.reverse_url('名字')) 



###  手写一个注册登录的逻辑 ###
* db （pymysql,mysqldb）
 * User account,password (unique) (uuid)
 * 