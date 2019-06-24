### ajax和http请求类库 ###
* 大前端（前端/ios/android）
* http类库发起请求，如果响应码（HttpResponse）是200，就会调用http请求类库成功的方法。
 * 但是很有可能是服务器将异常处理了。
 * 依据数据有没有修改成功?
 
			{'errorcode':200,'errormsg':'',[{},{},{}]} 
			{'errorcode':-100.'errormsg':'出错信息'}
			对于大前端开发者来说，很容易使用第三方json解析类库解析	
 * ajax，success（HttpResponse）是200），name有没有真正的添加成功呢？还得看errorcode
 
### form ###
* 在向数据库添加数据之前，先清洗数据，
* 数据清洗步骤（from表单验证）
 * 原因，在插入数据库的时候，一定要对数据验证（清洗）
 * data = request.POST.dict()  
 * 定义form类(django默认清洗判断，简单。自定义)

			class MyForm(forms):
				  	goodsid = forms.IntegerField()
				    colorid = forms.IntegerField()
				    sizeid  = forms.IntegerField()
				    count = forms.IntegerField()	
					def clean(self):
						super(MyForm,self).clean()#让父类先完成简单的清洗
						data = self.cleaned_data
       					 count = data['count']
        				if count<0:
           					 self.errors['count']=['商品的数量不能小于0']
						还以可以做其他判断
  * myfrom = MyFrom(data)
  * myfrom.isvalid() 数据是否有效
  * myfrom.clean_data 获得格式正确的数据
 ### 多继承 ###

* 树		
 * 树的遍历
 * 深度遍历
 * 广度遍历

### redis ### 				
* 相比原生的session（占用的是自己的内存），redis可以存储更多的东西（redis是非关系型数据库）（除了内存存储，还会存储到数据库）

### 实际开发中 ###
* 前后端分离
 * 后端写的程序
 * 后端发给前端（大前端）一般都是json 
 
			{'errorcode':200,'errormsg':'',[{'marks':[{},{},{}]},{},{},{}]}		* 
 * {} jsonobject
 * [] jsonarray
 * json  包
 * serialize 专门序列化数据模型 （CartItem） 都是继承自models.Model （不能序列化普通对象），不能序列化单个对象（serialize('json',[c,])[1:-1]）
 
				from cart.models import CartItem
				from django.core.serilizes import serialize
				arr = []
				arr=[CartItem(goodsid=1,colorid=1,sizeid=1,count=10),CartItem(goodsid=1,colorid=1,sizeid=1,count=10)]
				serialize('json',arr)  获得了json字符串
 * 序列化：将对象转换成字符串
 * 反序列化：将字符串转换成对象（deserialize）
					
				str = u'[{"model": "cart.cartitem", "pk": null, "fields": {"goodsid": 1, "colorid": 1, "sizeid": 1, "count": 10}}]'
					for obj in deserialize('json',str):
   						 print obj.object
 * json
 
			dumps是将dict转化成str格式，loads是将str转化成dict格式。
 * 普通对象，__dict__

			




			"[{'age': 10, 'name': '\\xe5\\xbc\\xa0\\xe4\\xb8\\x89'}, {'age': 20, 'name': '\\xe6\\x9d\\x8e\\xe5\\x9b\\x9b'}]"
 * 对于普通对象
 * object.__dict__  获得了这个对象的属性
 *  arr = [Person(),Person()] 			


           							
				

 *  写的服务器，就和前端一点关系都没有了。
 *  一套服务器可以让前端，ios，android共同使用