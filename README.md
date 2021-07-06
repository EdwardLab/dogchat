# DogChat
Fast, lightweight chat software🌈🌈
## introduce
Fast and lightweight open source chat framework dogchat, support server deployment and operation, based on python3, django development   
Powered By:Microtech Group
## Deploy Dogchat on your server🚀🚀
Whether you're a Windows, Linux, or other system server, Python and Django support enables rapid deployment and installation  
### Installation QuickServer method
#### Ubuntu or Debian (Series) Linux
1.Open Server Terminal  
2.Enter ```apt update && apt install python3 git mysql-server && pip install django && cd ~ && mkdir dogchat && cd dogchat && git clone https://github.com/xingyujie/dogchat.git```  
3.Configuring the MySQL server:  
DogChat needs Mysql server support, we can go to dogchat/setting.py to configure the default database.  
#### Other Linux, like centos
1.Install python3(like yum),mysql,pip,django(pip) and Clone Code  
2.Configuring the MySQL server:  
DogChat needs Mysql server support, we can go to dogchat/setting.py to configure the default database.  
#### Windows
1.Download and install the Python standard exe package, and check pip for custom installation.  
2.Clone the repository source code and place it in any folder.  
3. Build Mysql Server, configure the database according to the database configuration prompt below.  
4. Check out the Running QuickServer chapter Quick Boot Server  
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
}
```
## Tips for database deploy
You need to configure a standard mysql server, and fill in the server information in dogchat/setting.py (like the configuration format above), NAME fill in your database name, USER is your database user name, HOST is your database IP address (if you build locally, it is usually 127.0.0.1), PORT is your database port (usually 3306), and PASSWORD is your database password. If you are buying a cloud host, the cloud host provider usually provides this information. If you don't know this information, you can consult. If you want to use your own equipment to build a mysql database, then you can go to Google chat for more information on the mysql database
## Running QuickServer
1.Configure environment variables (python 3.x defaults to python variables)
2. Go to the dogchat root folder, open cmd or terminal, and enter the code ```python manage.py runserver 0.0.0.0:8000```You can also change to another port.






 
