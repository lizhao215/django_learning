### 先把项目放到centos ###
* 创建一个虚拟机环境
* 数据库 centos （账号：密码）
* redis centos
* 让项目通过 xftp传到centos
* 切换到项目目录  python manage.py runserver 0.0.0.0：8000
* nginx （菜鸟教程）make & makeinstall,启动 

### nginx部署django ###
* xftp 传输项目到centos
* 创建env环境
 *  pip install virtualenv 安装工具
 *  virtualenv TEST --python=python2.7 创建2.7的环境
 *  virtualenv TEST --python=python3.6 ENV3.6的环境
 *  前提是centos上有2.7和3.6的环境
 *  source ./bin/activate 激活环境
 * 之后安装django项目需要的工具
 
		django
		pillow 
		MySQL-python
		django-redis
		pycrypto 加签环境(可以下载tar.gz  之后pip install pycrypto.tar.gz包)
 * 切换到项目目录 修改数据库（给liunx配置数据库） redis相关配置 
 * 运行python manage.py runserver 0.0.0.0:8000检测能否使用
* supervisor 管理多进程
 * pip install supervisor
 * echo_supervisord_conf > supervisord.conf 输出默认的conf文件
 *  修改 supervisord.conf文件
 

			；[include]
			；files = relative/directory/*.ini	
			为
			[include]
			files = /etc/supervisor/*.conf	 
 * 拷贝
 
			cp supervisord.conf /etc/
 * 在etc下创建目录supervisor，并创建文件django.conf

	
			[group:djangos]
			programs=django-8000,django-8001,django-8002,django-8003
			
			[program:django-8000]
			command=/root/TEST/bin/python2.7 /root/jiukuaijiy/manage.py runserver 0.0.0.0:8000
			directory=/root/jiukuaijiy
			user=root
			autorestart=true
			redirect_stderr=true
			stdout_logfile=/root/jiukuaijiy/django.log
			loglevel=info
			
			[program:django-8001]
			command=/root/TEST/bin/python2.7 /root/jiukuaijiy/manage.py runserver 0.0.0.0:8001
			directory=/root/jiukuaijiy
			user=root
			autorestart=true
			redirect_stderr=true
			stdout_logfile=/root/jiukuaijiy/django.log
			loglevel=info
			
			
			[program:django-8002]
			command=/root/TEST/bin/python2.7 /root/jiukuaijiy/manage.py runserver 0.0.0.0:8002
			directory=/root/jiukuaijiy
			user=root
			autorestart=true
			redirect_stderr=true
			stdout_logfile=/root/jiukuaijiy/django.log
			loglevel=info
			
			
			[program:django-8003]
			command=/root/TEST/bin/python2.7 /root/jiukuaijiy/manage.py runserver 0.0.0.0:8003
			directory=/root/jiukuaijiy
			user=root
			autorestart=true
			redirect_stderr=true
			stdout_logfile=/root/jiukuaijiy/django.log
			loglevel=info
			
					
			

 * 启动 查看进程

			supervisord -c /etc/supervisord.conf
			ps aux | grep supervisord #查看进程是否存在
			kill 杀死进程
 * supervisorctl 客户端使用


			status    # 查看程序状态
			stop djangos:*   # 关闭 djangos组 程序
		    start djangos:*  # 启动 djangos组 程序
			restart djangos:*    # 重启 djangos组 程序
			update    ＃ 重启配置文件修改过的程序
 * 检测 是否正常（windows检测）

* nginx
 * nginx功能  （负载均衡，反向代理，缓存static文件等）
 * 放在整个web服务的最前面
	
		
		![](https://i.imgur.com/el5wfDb.png)

 * 安装 编译 参照 菜鸟教程
 * 安装的路径
 				# centos的nginx配置文件
				/usr/local/webserver/nginx/conf/nginx.config
 *  修改nginx配置文件


			

				#user  nobody;
				worker_processes  1;
				
				#error_log  logs/error.log;
				#error_log  logs/error.log  notice;
				#error_log  logs/error.log  info;
				
				#pid        logs/nginx.pid;
				
				
				events {
				    worker_connections  1024;
				}
				
				
				http {
				    include       mime.types;
				    default_type  application/octet-stream;
				
				    #log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
				    #                  '$status $body_bytes_sent "$http_referer" '
				    #                  '"$http_user_agent" "$http_x_forwarded_for"';
				
				    #access_log  logs/access.log  main;
				
				    sendfile        on;
				    #tcp_nopush     on;
				
				    #keepalive_timeout  0;
				    keepalive_timeout  65;
				
				    #gzip  on;
				    upstream djangos {
				    server 0.0.0.0:8000;
				    server 0.0.0.0:8001;
				    server 0.0.0.0:8002;
				    server 0.0.0.0:8003;
				    }
				
				    server {
				        listen       80;
				        server_name  localhost;
				
				        #charset koi8-r;
				
				        #access_log  logs/host.access.log  main;
				
				        location / {
				        proxy_pass_header Server;
				        proxy_set_header Host $http_host;
				        proxy_redirect off;
				        proxy_set_header X-Real-IP $remote_addr;
				        proxy_set_header X-Scheme $scheme;
				        proxy_pass http://djangos;
				        }
				        location /static {
					autoindex on;
				        alias  /var/www/static/;
				        }
					location /media
					{
					autoindex on;
					alias /var/www/media/;
					}
				
				        #error_page  404              /404.html;
				
				        # redirect server error pages to the static page /50x.html
				        #
				        error_page   500 502 503 504  /50x.html;
				        location = /50x.html {
				            root   html;
				        }
				
				        # proxy the PHP scripts to Apache listening on 127.0.0.1:80
				        #
				        #location ~ \.php$ {
				        #    proxy_pass   http://127.0.0.1;
				        #}
				
				        # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
				        #
				        #location ~ \.php$ {
				        #    root           html;
				        #    fastcgi_pass   127.0.0.1:9000;
				        #    fastcgi_index  index.php;
				        #    fastcgi_param  SCRIPT_FILENAME  /scripts$fastcgi_script_name;
				        #    include        fastcgi_params;
				        #}
				
				        # deny access to .htaccess files, if Apache's document root
				        # concurs with nginx's one
				        #
				        #location ~ /\.ht {
				        #    deny  all;
				        #}
				    }
				
				
				    # another virtual host using mix of IP-, name-, and port-based configuration
				    #
				    #server {
				    #    listen       8000;
				    #    listen       somename:8080;
				    #    server_name  somename  alias  another.alias;
				
				    #    location / {
				    #        root   html;
				    #        index  index.html index.htm;
				    #    }
				    #}
				
				
				    # HTTPS server
				    #
				    #server {
				    #    listen       443 ssl;
				    #    server_name  localhost;
				
				    #    ssl_certificate      cert.pem;
				    #    ssl_certificate_key  cert.key;
				
				    #    ssl_session_cache    shared:SSL:1m;
				    #    ssl_session_timeout  5m;
				
				    #    ssl_ciphers  HIGH:!aNULL:!MD5;
				    #    ssl_prefer_server_ciphers  on;
				
				    #    location / {
				    #        root   html;
				    #        index  index.html index.htm;
				    #    }
				    #}
				
				}
				
				
				
* 收集static文件到/var/www目录
		
		python manage.py collectstatic
* 收集media文件到/var/www目录 
		
* 修改debug 为false
* 修改setting中的meida的路径，
* 后台添加
							
				
							

						

