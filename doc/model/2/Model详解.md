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
* timedelta (专门时间+-操作)
 * Post.objects.update(created = F('created')+timedelta(days = -1)) 更新当前帖子的时间
 *  F('created')获得当前帖子的时间
 * Post.objects.filter(id = 2).update(created = F('created')+timedelta(days = -100))
 * Post.objects.filter(created__gte=date.today()+timedelta(days= -200))

				SELECT `post_post`.`id`, `post_post`.`title`, `post_post`.`category_id`, `post_post`.`created` FROM `post_post` WHERE `post_post`.`created` >= '2017-04-08' LIMIT 21
 * 热帖
 * Post.objects.filter(remark__gte=F('read')/2).filter(remark__gte=50)

				SELECT `post_post`.`id`, `post_post`.`title`, `post_post`.`category_id`, `post_post`.`created`, `post_post`.`remark`, `post_post`.`read` FROM `post_post` WHERE (`post_post`.`remark` >= ((`post_post`.`read` / 2)) AND `post_post`.`remark` >= 50) LIMIT 21
	
	


 


  
 
  
