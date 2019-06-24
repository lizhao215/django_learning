### session高级 ###
* 用户
* 购物车
* 验证码
* django的session默认存储到数据库。（自定义对象（不能序列化的自定义对象））会出错

			request.session['cart']=[Person(),Person()]
			出错的原因：django默认的是数据库存储
* 让session能支持存储对象？
* 可以的 内存存储
* session放到redis

### md5 ###
				import hashlib
				md = hashlib.md5()
				md.update(原始数据)
				md.hexdigest() #获得16进制的加密数据

### 购物车模块设计 ###
* 商品详情界面 
 * 添加商品（CartView）添加商品，重定向。（有好多界面都会重定向）
 * 重定向到购物车界面（form表单）

				class BaseRedirctView(View):
					redirct_url = None
					def dispatch_request(self):
						# 处理业务（）
						getattr(self,'handle')(request)
						# 显示交给重定向后的页面
						return HttpRedirctRespone(self.redirct_url)	
				class CartView(BaseRedirctView):
						redirct_url = '/cartlistview'
						def handle(request):
							utils = getCartUtils(request)
							utils.save(**request.POST)

* 购物车界面 (CartListView)
 * ajax 
 * 修改的数量（添加+减少） 
 * 查看商品
* 当用户出现
 * session中数据同步到数据库 
* 工厂模式(策略模式)
 * 动态的获得操作的对象（CRUD） 
 				
				type=add&count=1,
				View父类
				type= del & count =1
				getattr(self,request.POST.get('type'))(**reuquest.POST)

				class CartUtils():
					def add(count,goodsid,colorid,sizeid):
					pass
					def delete(goodsid,colorid,sizeid):
					pass
					def get():
					pass
				
				class SessionCartUtils(CartUtils):
					def __init__(self,session):
						self.session= session
				class DBCartUtils(CartUtils):
					def add(count,goodsid,colorid,sizeid):
						CartItem(colorid,sizeiid,goodid,count).save()
				def getCartUtils(request):
					if request.session.get('user',None) !=None:
							return DBCartUtils() 
					else :
						return SesssionCartUtils(request.session)
				
				utils = getCartUtils(request)
				

### 用户 ###
* 实现简单登录
* md5 （前端+后台）
* md5 + 如何在不同的时间登录，发送给服务器的密码（加密之后的密码是随机的）
* 中间件（对未登录用户和已登录用户设置权限）