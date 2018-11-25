## 参考

```
https://api.aliyun.com/?spm=a2c1g.8271268.10000.2.1ef2df25sDHCuE
https://help.aliyun.com/document_detail/27566.html?spm=5176.10609282.905295..62e57cbfbQxIm8
https://github.com/aliyun/aliyun-openapi-python-sdk
```


## 注意事项

```python
1. Nginx要手动编译安装 1.14
2. 要设置webapp/settings.py
MEDIA_ROOT = os.path.join(BASE_DIR, "data")
MEDIA_URL = "/data/"
3. 静态文件移动
python manage.py collectstatic
4. nginx配置文件

upstream app_server_port {
    server 127.0.0.1:8000 fail_timeout=0;
}

upstream app_server_sock {
    server unix:/tmp/gunicorn.sock fail_timeout=0;
}

server {
    listen       		9000;
    server_name  		localhost;
    client_max_body_size 	4G;
    keepalive_timeout 		5;

    location / {
        # checks for static file, if not found proxy to app
        try_files $uri @proxy_to_app;
    }

    location @proxy_to_app {
        include uwsgi_params;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header Host $http_host;
        # we don't want nginx trying to do something clever with
        # redirects, we set the Host: header above already.
        proxy_redirect off;
        #proxy_pass http://app_server_port;
        uwsgi_pass 127.0.0.1:8000;
    }


    location /static {
        alias   /home/vagrant/zhengyscn/go/src/github.com/51reboot/actual-19-homework/lesson13/zhengyscn/webapp;
    }

    location = /favicon.ico { 
        access_log off; 
        log_not_found off; 
    }

    error_page 404 /404.html;
        location = /40x.html {
    }

    error_page 500 502 503 504 /50x.html;
        location = /50x.html {
    }
}
```