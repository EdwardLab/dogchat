# DogChat
Fast, lightweight chat software

## Tips
Unfinished project, please do not use will be removed after the completion of this field
## introduce
Fast and lightweight open source chat framework dogchat, support server deployment and operation, based on python3, django development   
Powered By:Microtech Group
## Deploy Dogchat on your server🚀🚀
Whether you're a Windows, Linux, or other system server, Python and Django support enables rapid deployment and installation  
### Installation QuickServer method
#### Ubuntu Linux
1.Open Server Terminal  
2.Enter ```apt update && apt install python3 git mysql-server && pip install django && cd ~ && mkdir dogchat && cd dogchat && git clone https://github.com/xingyujie/dogchat.git```
3.Configuring the MySQL server:  
DogChat needs Mysql server support, we can go to dogchat/setting.py to configure the default database.  
Line 79 of dogchat/setting.py:  
```DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dogchat',
        'USER': 'dogchat',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'PASSWORD': '@dogchat?963_default!321_?password@!'
    }
}```
You need to configure a standard mysql server, and fill in the server information in dogchat/setting.py (like the configuration format above), NAME fill in your database name, USER is your database user name, HOST is your database IP address (if you build locally, it is usually 127.0.0.1), PORT is your database port (usually 3306), and PASSWORD is your database password. If you are buying a cloud host, the cloud host provider usually provides this information. If you don't know this information, you can consult. If you want to use your own equipment to build a mysql database, then you can go to Google chat for more information on the mysql database







 
