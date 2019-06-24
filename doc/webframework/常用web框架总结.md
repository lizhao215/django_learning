### HttpRequest ###
* 请求头的方式
 *  remoate,HTTP_REMOATE 
* 请求方式
 *  GET,POST
* 请求参数
 * GET请求参数
 * POST请求参数 
* Cookie
 * 获得cookie
* Session
 * request中有session 

### HttpResponse ###
* 设置响应体  
* 响应头
* 设置Cookie

### HttpServer ###
* 将浏览器请求的字符串转换成HttpRequest对象
* 将HttpResponse对象转换成字符串，传输给浏览器
* 路由匹配
 * 获得HttpRequest中path，然后根据正则[(r'/',index)]，在咱们的路由表中顺序匹配。
* 中间件（自定义装饰器即可）

### setings文件 ###
* 模板的路径
* static_url,staticfile_dirs
* 
### redis,mysqldb ###
* 连接器
* 用的都是封装好的类库（发起TCP链接，向真实服务器发送数据） 
* 在python中使用的redis,mysqldb，相当于客户端。


###  django的核心框架 ###
* 基于正则的url路由匹配
 * 所有的处理函数，都是通过正则匹配
 * 捕获参数是怎么回事？httprequest.PATH  r'/index/(/d+)'
*  处理请求的视图系统
 * 获得请求头，请求参数，cookie，session，method  
 * request.METAS  
 * 因为views中写的处理函数
 * HttpRequest
 * HttpResponse，（HttpRedirtResponse,render,HttpResponse,redirct）,设置响应体，设置cookie，设置响应头   
 * 通用视图，闭包
* 显示给用户的模板系统
 * html（不能是static文件夹下的） 
 * 服务器读取html转换成不确定字符串
 * 根据Context渲染确定的字符串
 * 学会自定义标签（filter，简单标签）{{name|sda}} {%if %} (装饰器，闭包)（不是必须的）
* 面向对象的ORM映射器
 * 以操作对象的方式操作数据库 （反射）
 * 获得对象（类）的字段，拼接成sql语句
 * objects （管理器），（自定义管理器）
 * 分组聚合 （不好理解）
 * 字段，auto_now,auto_now_add,null=True,blank=True,default=True
* django 其他
 * staic文件夹
 * Paginator
 * 中间件
 * form表单 (django中数据清洗的类) Form ，大家需要知道插入数据库的数据都需要清洗（验证）
 * 缓存，（全站缓存，单独view的缓存）
 * 虚拟环境配置 （每个项目使用单独的环境）
 * 富文本编辑器，（文件上传）
 * 全文索引 （做过全文索引）haystack（容器）,whoosh（搜索引擎）,jieba(分词)

 * pythonanywhere很像 nginx（1 虚拟环境，2 指定项目目录，3 static文件夹，media的使用）

