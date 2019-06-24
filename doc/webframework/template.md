### Template ###
* tornado模板的渲染流程

		
			from tornado.template import Template
			t = Template('hello:{{name}}')
			t.generate(name='张三')

 * 自定义渲染1


			class IndexHandler(tornado.web.RequestHandler):
			    def get(self, *args, **kwargs):
			        from tornado.template import  Template
			        # 读取模板
			        with open('index.html') as fr:
			            content = fr.read()
			        # 创建模板对象
			        t = Template(content)
			        # 渲染
			        response = t.generate(name='张三')
			        self.write(response)
 * 自定义渲染2
 

			  def get(self, *args, **kwargs):
			        from tornado.template import Loader
			        import os
			        TEMPLATE_PATH = os.path.dirname(__file__)
			        loader = Loader(TEMPLATE_PATH)
			        t = loader.load('index.html')
			        response = t.generate(name='李四')
			        self.write(response)
 * 系统提供的


				class RenderHandler(tornado.web.RequestHandler):
				    def get(self, *args, **kwargs):
				        self.render('index.html',name='王五')

				BASE_DIR = os.path.dirname(__file__)
				app = tornado.web.Application([
				    (r'/',IndexHandler),
				    (r'/loader',LoaderHandler),
				    (r'/render',RenderHandler),
				]
				    ,template_path=os.path.join(BASE_DIR,'templates')
				)
### 语法 ###
* 表达式{{}} （tornado的模板渲染完全的支持python语法）
 *  支持任何的python语句，函数，对象
 *  reverse_url
 *  {{static_url('a.jpg') }}  self.static_url
* 表达式{%%}
 * for循环
 * if判断
 *  {%raw %}  富文本编辑器
 *  支持任何的python语法  如果你使用了{%%} 一定要记得{%end%}

### 模板 ###
* 模板继承 extends
* 包含 include
* 占位 block 
