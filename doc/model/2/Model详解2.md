#### ORM  ####
* 对象关系映射（Object relational mapping）
* 实现实体（数据模型）和数据库的解耦
* 将sql语句的操作转换成对对象的操作
#### 切换mysql数据库 ####
* 先创建数据库

		create database models charset=utf8
* 在settings中

			DATABASES = {
			    'default': {
			        'ENGINE': 'django.db.backends.mysql',
			        'NAME': "models",
			        'USER':'root',
			        'PASSWORD':'admin',
			        'HOST':'127.0.0.1',
			        'PORT':3306
			    }
			}
#### 查看执行的sql语句 ####
* connection.queries 指的是执行过的所有的语句，最后一条也就是我们刚刚执行的语句

			
			def showsql():
				from django.db import connection
				queries = connection.queries
				print queries[-1]['sql']

#### 根据已有的数据库生成model（数据模型） ####
			python manage.py inspectdb > 模块/models.py
#### Django的ORM类库很有可能会有惰性加载或者懒加载 ####



#### CURD ####
* retrieve（检索）
 *   Movie.objects.all()获得所有的数据
 
			SELECT `movie`.`mid`, `movie`.`mname`, `movie`.`mdesc`, `movie`.`mimg`, `movie`.`mlink` FROM `movie` LIMIT 21
 * get()方法
  * Movie.objects.get(mid = 1000)
	
		 	SELECT `movie`.`mid`, `movie`.`mname`, `movie`.`mdesc`, `movie`.`mimg`, `movie`.`mlink` FROM `movie` WHERE `movie`.`mid` = 1000
  * Movie.objects.get(mid__exact =1000 )
  * 没有数据（DoesNotExist）或者大于1个数据都会出错（MultipleObjectsReturned）
* filter（）过滤条件
 
	* Movie.objects.filter(mid__gt=1000)
	
		SELECT `movie`.`mid`, `movie`.`mname`, `movie`.`mdesc`, `movie`.`mimg`, `movie`.`mlink` FROM `movie` WHERE `movie`.`mid` > 1000 LIMIT 21


  * Movie.objects.filter(mid__lt=1000)

				SELECT `movie`.`mid`, `movie`.`mname`, `movie`.`mdesc`, `movie`.`mimg`, `movie`.`mlink` FROM `movie` WHERE `movie`.`mid` < 1000 LIMIT 21

  * Movie.objects.filter(mid__lte=1000)
  * Movie.objects.filter(mid__gte=1000)
  * Movie.objects.filter(mid__range=(1,1000))

			SELECT `movie`.`mid`, `movie`.`mname`, `movie`.`mdesc`, `movie`.`mimg`, `movie`.`mlink` FROM `movie` WHERE `movie`.`mid` BETWEEN 1 AND 1000 LIMIT 21
 * Movie.objects.filter(mname__contains='爱情')
	
			SELECT `movie`.`mid`, `movie`.`mname`, `movie`.`mdesc`, `movie`.`mimg`, `movie`.`mlink` FROM `movie` WHERE `movie`.`mname` = '%爱情%' LIMIT 21
 * Movie.objects.filter(mname__startswith='爱情')
 
			SELECT `movie`.`mid`, `movie`.`mname`, `movie`.`mdesc`, `movie`.`mimg`, `movie`.`mlink` FROM `movie` WHERE `movie`.`mname` LIKE BINARY '爱情%' LIMIT 21
 * 遇到了脏数据（数据清洗）
   * name多行文本，有很多空格，换行符
  

				for m in Movie.objects.all():
					m.mname=m.mname.strip()
					m.save()
 	
* 查询（爱情开头，了结尾）
 	* Movie.objects.filter(mname__startswith='爱情',mname__endswith='了')
 	* Movie.objects.filter(mname__startswith='爱情').filter(mname__endswith='了')


			SELECT `movie`.`mid`, `movie`.`mname`, `movie`.`mdesc`, `movie`.`mimg`, `movie`.`mlink` FROM `movie` WHERE (`movie`.`mname` LIKE BINARY '爱情%' AND `movie`.`mname` LIKE BINARY '%了') LIMIT 21


 * 时间相关的
 	* User.objects.filter(birthday__in=('2000-11-20','2017-11-11'))
 	
       		SELECT `movie_user`.`id`, `movie_user`.`name`, `movie_user`.`birthday` FROM `movie_user` WHERE `movie_user`.`birthday` IN ('2017-11-11', '2000-11-20') LIMIT 21

  * 查询最近活跃的用户（F(函数)）
* 查询的电影不包含爱情的
 * Movie.objects.exclude(mname__contains='爱情')

				SELECT `movie`.`mid`, `movie`.`mname`, `movie`.`mdesc`, `movie`.`mimg`, `movie`.`mlink` FROM `movie` WHERE NOT (`movie`.`mname` LIKE BINARY '%爱情%') LIMIT 21
* 获得第一条数据
 * Movie.objects.first()


		  SELECT `movie`.`mid`, `movie`.`mname`, `movie`.`mdesc`, `movie`.`mimg`, `movie`.`mlink` FROM `movie` ORDER BY `movie`.`mid` ASC LIMIT 1
* 获得最后一条语句
 * Movie.objects.last()

		SELECT `movie`.`mid`, `movie`.`mname`, `movie`.`mdesc`, `movie`.`mimg`, `movie`.`mlink` FROM `movie` ORDER BY `movie`.`mid` DESC LIMIT 1
* 惰性查询
 * **再查询多条数据的时候，什么时候用什么时候查**  
 * movies = Movie.objects.all()
 * 这时候，有没有查询数据，没有
 * 什么时候用什么时候查询
 *  print movies
 * <font color='red'>多余超过一个数据，会惰性查询</font>
 * <font color='red'>一个数据get,first,last都不会</font>
 * **再查询多条数据的时候，不用全部查询过来，而是查询有限的个数（21）**  1.11.6
* 切割 [1,2,3][1:2]
 * Movie.objects.all()[:5]
 * Movie.objects.all()[10:20]

				SELECT `movie`.`mid`, `movie`.`mname`, `movie`.`mdesc`, `movie`.`mimg`, `movie`.`mlink` FROM `movie` LIMIT 10 OFFSET 10
	

 * 用途   分页 
  * Pagnitor 

* 排序
	* Movie.objects.order_by('-mid').all()降序
 
	* Movie.objects.order_by('mid').all()
	* Movie.objects.order_by('mname','-mid')多个字段排序
* 使用values查询 部分属性

* QuerySet 结果集
 * 惰性，什么时候使用什么时候查询
 * 缓存  
* 聚合函数
 * 针对一系列记录的
 *  count,max,min,avg,sum
 

			from django.db.models import Count
				Movie.objects.aggregate(Count('*'))

				SELECT COUNT(*) AS `count` FROM `movie`
 
* 分组
 * group_by (分组)，聚合一旦和分组使用
 *  聚合函数，就会统计同一组下面的记录
 *  统计类别下面有多少篇文章
 * Post.objects.values('category__name').annotate(count= Count('*'))
		 
			SELECT `post_category`.`name`, COUNT(*) AS `count` FROM `post_post` INNER JOIN `post_category` ON (`post_post`.`category_id` = `post_category`.`id`) GROUP BY `post_category`.`name` ORDER BY NULL LIMIT 21
* 修改字段

![](https://i.imgur.com/jPntDRt.png)

* 时间分组聚合
 * Post.objects.values('created').annotate(count = Count('*'))

			SELECT `post_post`.`created`, COUNT(*) AS `count` FROM `post_post` GROUP BY `post_post`.`created` ORDER BY NULL
* 原生的操作
 *  Post.objects.raw('select * from post_post ') 查询语句
 *  connection （默认的数据连接对象）
 		
				from django.db import connection
				cursor = connection.cursor()
				cursor.execute('crud   sql')
				cursor.close()	 

* F类的功能
 * timedelta (专门时间+-操作)
 * Post.objects.update(created = F('created')+timedelta(days = -1)) 更新当前帖子的时间
 *  F('created')获得当前帖子的时间
 * Post.objects.filter(id = 2).update(created = F('created')+timedelta(days = -100))
 * Post.objects.filter(created__gte=date.today()+timedelta(days= -200))

				SELECT `post_post`.`id`, `post_post`.`title`, `post_post`.`category_id`, `post_post`.`created` FROM `post_post` WHERE `post_post`.`created` >= '2017-04-08' LIMIT 21
 * 热帖
 * Post.objects.filter(remark__gte=F('read')/2).filter(remark__gte=50)

				SELECT `post_post`.`id`, `post_post`.`title`, `post_post`.`category_id`, `post_post`.`created`, `post_post`.`remark`, `post_post`.`read` FROM `post_post` WHERE (`post_post`.`remark` >= ((`post_post`.`read` / 2)) AND `post_post`.`remark` >= 50) LIMIT 21
 * F 可以操作的运算符+-*/% 
* Q类功能，主要作用在filter（其实就是过滤条件）
 * 与或非 and  or ~ 
 * 想查询电影中名字包含爱情或者包含犯罪关键字的电影 
	  Movie.objects.filter(Q(mname__contains='爱情')|Q(mname__contains='犯罪'))


				SELECT `movie`.`mid`, `movie`.`mname`, `movie`.`mdesc`, `movie`.`mimg`, `movie`.`mlink` FROM `movie` WHERE (`movie`.`mname` LIKE BINARY '%爱情%' OR `movie`.`mname` LIKE BINARY '%犯罪%') LIMIT 21

	
 * 想查询电影中名字包含爱情或者包含犯罪关键字的电影 
 
		Movie.objects.filter(Q(mname__contains='爱情')&Q(mname__contains='犯罪'))


				SELECT `movie`.`mid`, `movie`.`mname`, `movie`.`mdesc`, `movie`.`mimg`, `movie`.`mlink` FROM `movie` WHERE (`movie`.`mname` LIKE BINARY '%爱情%' AND `movie`.`mname` LIKE BINARY '%犯罪%') LIMIT 21


 * 想查询电影中名字不包含爱情

		Movie.objects.filter(~Q(mname__contains='爱情'))
### create ###
 * 第一种

			cate = Category(name='大数据')
			cate.save()保存
 * 第二种使用objects（Manager）(针对于每一张表都有一个管理器)

  			Category.objects.create(name= '大数据')
### delete ###
* 第一种
			cate = Category.objects.get(id = 1)
			cate.delete()
* 第二种使用objects（Manager）(针对于每一张表都有一个管理器)
			Category.objects.get(name = '前端').delete()
			Category.objects.filter(name ='张三').delete()
			
### 更新 ###
* 通过对象更新
	
			post = Post.objects.get(title = 'HTML详解')
			post.title='HTML基础教程'
			post.save()
			虽然我只是修改了标题，但是所有的字段都会更新（就是对象的主键）
			UPDATE `post_post` SET `title` = 'HTML基础', `category_id` = 17, `created` = '2017-10-25', `remark` = 0, `read` = 0 WHERE `post_post`.`id` = 4
* 第二种使用objects（Manager）(针对于每一张表都有一个管理器)
  
	* Post.objects.filter(title = 'HTML基础').update(title= 'HTML详解',read=10)


				UPDATE `post_post` SET `read` = 10, `title` = 'HTML详解' WHERE `post_post`.`title` = 'HTML基础'

## 关系 ##
* 1对1   身份证：征信记录
* 1对n   博客：帖子，教室：学生  消费者：商品
* n对n   老师：学生。学生：选课，博客：标签

## 1对多查找 ##
* 正向
		获得1的类的实例
		实例.多的类_set.all()
		cate = Category.objects.first()
		cate.post_set.all()
* 反向
		获得多的类的实例
		实例.字段
		post = Post.objects.first()
		post.category 类别
## 多对多 ##
* 正向
		获得多的类的实例
		实例.多的类_set.all()
		tag = Tag.objects.all()
		tag.post_set.all()
* 反向
		获得多的类的实例
		实例.多的类_set.all()
		post = Post.objects.first()
		post.tags.all()

## 结论 ##

* 只要获得任何一个实例（对象），和这个实例相关的都能查到。			


### migrate迁移之后缺失字段或者缺失表 ###
* 删除模块migrations目录下的所有迁移文件
* DELETE from django_migrations where app = 'post'
* 如果**表已经存在（只能删除模块下的表）
* python manage.py migrate
### 添加1对多对象 ###
* 从数据库获得外键对象/创建一个对象保存到数据库中
### 如果已有数据库  ###
python manage.py inspectdb > 模块/models.py