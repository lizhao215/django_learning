### 模板的渲染过程 ###
* MVC(MVT,MTV)
* Template
 * 模板类 


			t = Template('<h1>{{name}}:欢迎</h1>')
* Context 上下文（）
	
			 c =Context({'name':'张三'})
* 渲染

			string = t.render(c)	
			print string 
* http 1


			def index_view(request):
		    t = Template('<h1>{{name}}:欢迎</h1>')
		    c = Context({'name':'张三'})
		    render_string = t.render(c)
		    return HttpResponse(render_string) 
* http 2
 * 在项目根目录下新建index.txt 
 
			 <h1 style='color:red'>{{name}}:欢迎</h1>
 * 代码

				def index_view(request):
				    with open('index.txt') as fr:
				        template_string = fr.read()
				    t = Template(template_string)
				    c = Context({'name':'李四'})
				    render_string = t.render(c)
				    return HttpResponse(render_string)
 * 发现模板字符串想写在哪里就写在哪里
* http 3


			
		 def index_view(request):
		        with open('templates/index.html') as fr:
		            template_string = fr.read()
		        t = Template(template_string)#创建模板
		        c = Context({'name':'李四'})# 上下文，dict
		        render_string = t.render(c)# 根据上下文把模板里面的未知渲染成已知，这个时候render_string全都是确定的东西
		        return HttpResponse(render_string)
* render_context

			
				from  django.template import Template
				from  django.template import Context
				from  django.http.response import  HttpResponse
				def render_context(request,template_name,context):
				    with open('templates/'+template_name) as fr:
				        template_string = fr.read()
				    t = Template(template_string)
				    c = Context(context)
				    render_string = t.render(c)
				    return  HttpResponse(render_string)
* render

### TEMPLATES settings ###

	

			TEMPLATES = [
			    {
			        'BACKEND': 'django.template.backends.django.DjangoTemplates',
			        'DIRS': [os.path.join(BASE_DIR, 'templates')]
			        ,
			        'APP_DIRS': True,
			        'OPTIONS': {
			            'context_processors': [
			                'django.template.context_processors.debug',
			                'django.template.context_processors.request',
			                'django.contrib.auth.context_processors.auth',
			                'django.contrib.messages.context_processors.messages',
			            ],
			        },
			    },
			]
* BACKEND 渲染的引擎
* DIRS 模板存放目录
* APP_DIRS:True
 * 如果DIRS里面没有找到 ，去自己模块中的templates目录下找。找不到就出错（TemplateDoesNotExist）
* context_processors 处理全局上下文（下午讲）						 
 
### DTL ###
* {{name}} 获得变量的值，如果变量不存在显示空白字符串。
* .的作用
 * 先按照字典的key来查  {'dict':{'name':'张三'}}
 * 按照对象的属性来查找  date  date.year
 * 按照对象的方法来查找  'asd'.upper 这个方法一定是无参方法，注意自定义方法的异常问题。  silent_variable_failure = True
 * 按照索引来找   list.0 支持正索引
 * 默认显示空白  
* if标签
 * <,>,==,!= >=,<= 都支持，但是要有空格
 * not and or
 *  支持多if elif else嵌套，但是，复杂逻辑在views中处理好
 *  ifequals 和 ifnotequals 需要接收两个参数判断
* for 
 * 只要是可迭代的全都可以
 * reversed 倒叙遍历
 * 配合 empty使用，显示空界面（empty） 
 * forloop count (循环的次数)一般会if配合使用
 * forloop.parentloop获得是外层循环的forloop
* 注释
 * 单行 {#{% for pageouter in page_range %}#} 
 * {% comment %} 多行注释
* csrf_token 针对post
 * form 隐藏字段 
 * cookie csrf_token值
 *  上面两个值同时服务器，服务器匹配，是否是正常渠道
 * 没有绝对安全的
* 转义
 * 将html标签转成字符串 
 * 为什么django默认转义所有的变量呢？为了防止跨站脚本攻击
 * on 默认也是打开
 * off  如果要关闭自动转义，一定要确认文本是安全的（js读取cookies）
 * 试用于代码
### url逆向解析 ###
* 更大程度解耦，模块与模块之jian的关系
* 代码中的
 *   url(r'^newdata/$',views.newdata_view,name='new') 就是给newdata起个名字。
 *    url(r'^filter/',include('fillter.urls',namespace='filter')),给模块起个名字 
 * reverse这个方法 
 * url = reverse('filter:new')  在代码中reverse('命名空间:view的名字')
 * 如果传递捕获试用的是args=[1007,800]
* 模板中
 * {% url 'filter:new' 2007 10 %}    
 * {% url 'filter:new' 2007 10 %}?name=李四
 * include 导入其他的html使用的，一般来说是复用代码
 * base.html抽象所有界面共同的部分 （挖坑占个位置）
 * extends 必须是第一标签
 * 填坑的时候，只需要填充部分（按需求）

![](https://i.imgur.com/zH4TPug.png)
### RequestContext ###
* 很多界面使用相同的数据
* request中包含了很多有用的信息，比如说购物车，session 
* c = RequestContext(request,context,processors=[custom_pro])
* processor 是给context字典包装新的数据的

				def custom_pro(request):#request是httprequest
    				return {'right':"我是右面的菜单"}
### 全局的RequestContext ###
* 在settings中添加即可
* 写法一波一样，只是配置到templates的settings中了，context_processors里面


### 自定义过滤器 ###
* 现在INSTALL_APP里面建一个包，templatetags

		#coding=UTF-8
		from  django import template
		#创建一个Libray对象
		register = template.Library()
		
		@register.filter
		def strip(value):#value接受的值
		    return  value.strip()



		@register.filter
		def strip(value,position):
		    return  value[position:]
* 模板中{%load 标签文件名%}
