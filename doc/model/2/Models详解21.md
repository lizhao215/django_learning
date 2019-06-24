### QuerySet ###

 * 惰性加载（延迟加载）
 *  缓存（查询）
  * posts = Post.objects.all();post = Post.objects.first()
  * 一定要有post持有，一定不要切割。redis（内存）
  * 所有的切割[0][:]（其实涉及到了计算）都不会缓存，剩下的fillter，all,first,等都会缓存
### 事务 ###
* 事务是一个原子操作。 （多表操作，添加修改删除）
*  from django.db import transcation(事务)
* 将事务以装饰器方式，添加到方法中。标示者这个方法是原子的

			from django.db import transaction
			
			@transaction.atomic
			def add(name ,num):
				Category.objects.create(name = name)
				1/num
				Post.objects.create(....)
			#标示着add方法是原子性的，要么成功添加数据库，要么失败回滚
### 扩展模型功能 ###
* 定义model类的一些处理方法
* 获得年龄
* 登录等逻辑
###  objects（管理器） ###
* Manager是所有的数据模型至少都有一个manager（如果不写的话，默认就是objects,写了就是你自己的）
* objects是默认的管理器，管理器作用（CRUD）
* 多对多添加（需要数据中先有post）

		 "<Post: Post object>" needs to have a value for field "id" before this many-to-many relationship can be used.

 
* 自定义PostManager，添加一对多

			class PostManager(models.Manager):
			    def createAddTags(self,title,cate,tags):
			       post = self.create(title = title,category = cate)
			       #self当前的管理器
			       post.tags.add(*tags)
			       post.save()

				class Post(models.Model):
				    title = models.CharField(max_length=100)
				    category = models.ForeignKey(Category)
				    tags= models.ManyToManyField(Tag,null=True)
				    objects = PostManager()

* 多个管理器

			class Post(models.Model):
			    title = models.CharField(max_length=100)
			    category = models.ForeignKey(Category)
			    tags= models.ManyToManyField(Tag,null=True)
			    #多个管理器
			    abc = PostManager()
			    objects = models.Manager()

* 何时自定义管理器
 * 默认的管理器没有需要功能 （添加1对多，还可以封装一些很长的方法，让代码简洁）
 * 重写 manager已有的方法修改排序


			
				class PostManager(models.Manager):
				    def createAddTags(self,title,cate,tags,created):
				       post = self.create(title = title,category = cate,created = created)
				       #self当前的管理器
				       post.tags.add(*tags)
				       post.save()
				    def queryPostByKeyWords(self,keyword):
				        return self.filter(title__contains=keyword).order_by('-title')
				    def all(self):
				        return super(models.Manager,self).all().order_by('-created')
## 字段 ##
* 这些字段会有一些最基本的验证
* CharField 标示字符串的，长度有限 
* DateField 标示日期
* DatetimeField 标示日期+时间
* TextField 标示大段文本，不知长度的文本
* ImageField  标示图片
* FileField  标示文件
* EmailEield 标示邮箱
* DecimalField 标示小数   max_digits 最大标示几位数  decimal_places几位小数
* BooleanField 标示是否
	* NullBooleanField ，是否，null 
* UUIDField 唯一标示
* PositiveIntegerField  正数
* BinaryField 二进制文件
* AutoField 自增
### 属性 ###

* unique=True 标示字段唯一，作用于数据库
* default  标示默认值，作用于表单，和数据库
* 针对时间
 * auto_now_add 自动添加时间（首次创建的时候添加时间）， 都不会在表单显示
 * modifed = models.DateTimeField(null=True,blank=True)
 * auto_now 保存的时候字段更新当前时间 都不会在表单显示
* null=True是数据库层次的，blank=True（空） 表单概念的
*  MEDIA_ROOT=os.path.join(BASE_DIR,'tupian') 针对于文件类 
*  PRIMARY_TRUE主键
### 自定义admin ###
* list_display=[]  在post界面显示什么字段
* list_editable 那些字段可以编辑
* list_display_links 哪些字段点击进入详情	
* list_filter  根据什么分类	
* filter_horizontal 用于多对多	
* list_per_page 一个显示多少数据
* search_fields搜索框

		class PostModelAdmin(admin.ModelAdmin):
		    list_display = ['title','content','created','modifed','category']
		    list_editable =['category','title']
		    list_display_links = ['created']
		    list_filter = ['category','created']
		    filter_horizontal = ['tags']
		    list_per_page = 1
		    search_fields = ['tags__name']
* inlines装饰
 * StackedInline（列表）
 * TabularInline（表格） 
* 修改后台（github，django后台模板）
* CMS（内容管理系统）
* 十几年（模块都是他自己的）