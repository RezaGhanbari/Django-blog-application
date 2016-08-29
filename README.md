# Django blog application
This is a Django/ReactJs blog application


## Features
#####• Comment system
#####• Sharing posts by e-mail
#####• Search engine (Solr and Haystack)
#####• Custom template tags and filters
#####• Pagination
#####• Simple Admin page
#####• Sending E-mail
#####• Handling forms in views
#####• Tag system for posts
#####• Retrieving posts by similarity
#####• Integrating third-party applications
#####• Complex QuerySets
#####• Sitemap
#####• Blog posts feeds


## Demo


## How to use
##### 1- Clone into your workspace: git clone
##### 2- create a virtualenv
##### 3- install project requirements (pip install -r requirements.txt)
##### 4- python manage.py migrate (inside root directory)
##### 5- python manage.py runserver ( see 127.0.0.1:8000/blog/)


## Solr setup
##### 1- Download latest version of [solr](http://www.oracle.com/technetwork/java/
javase/downloads/index.html)
##### 2- Unzip downloaded file go to the example directory within the Solr installation directory (that is, cd solr-4.10.4/example/)
##### 3- From this directory, run Solr with the built-in Jetty web server using the command: java -jar start.jar
##### 4- Open your browser and enter the URL http://127.0.0.1:8983/solr/
##### 5- Create a new core
##### 6- Inside the example directory within the solr-4.10.4/ directory, create a new directory and name it blog . Then put solr files of project inside that
##### 7- Put content of solr directory inside the resources directory of solr-4.10.4/example .