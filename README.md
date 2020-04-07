# Tanjil's Website  
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)  

[![Website lbesson.bitbucket.org](https://img.shields.io/website-up-down-green-red/http/lbesson.bitbucket.org.svg)](http://lbesson.bitbucket.org/)
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)
[![GitHub version](https://badge.fury.io/gh/Naereen%2FStrapDown.js.svg)](https://github.com/Naereen/StrapDown.js)
[![](https://badge-size.herokuapp.com/Naereen/StrapDown.js/master/strapdown.min.js)](https://github.com/Naereen/StrapDown.js/blob/master/strapdown.min.js)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
The website was made with python via Flask  
My website deployed with Heroku CLI and was created with the micro web framework called flask in python script and is a simple blog programming to practice and do my hobby's program skills  

  - Homepage
  - Mainpage
  - Aboutpage
  
# New Features!

  - Added the Data collector with database postgresql and send the email with smtplib
  - Added the candlestick charts graphs of big companies stock markets
  
 You can also:
  - View my webmap
  - Visit the data collector web application
  - Interactive with the graph
  
### Languages

This was builded with
* [Python](https://www.python.org/) -  general-purpose programming language
* [HTML](https://devdocs.io/html/) - Hypertext Markup Language, sandard markup language for documents designed to be displayed in a web browser
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) - Cascading Style Sheets, style sheet language used for describing the presentation of a document written in a markup language like HTML.
* [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/) - Jinja is a web template engine for the Python programming language 

### Installation
First, create an virtual environment and than install the dependencies and start the server.

```sh
$ cd 'tanjil-s-website'
$ python3 -m venv runServer
$ cd runServer
$ cd bin
$ source activate
```

And then install the requirements using...  
  
  
```sh
$ pip install bokeh
$ pip install flask
$ pip install flask_sqlalchemy
$ pip install pandas
$ pip install pandas_datareader
$ pip install psycopg2
```

Verify the deployment by navigating to your server address in your preferred browser.

```sh
127.0.0.1:8000
```
[![thank you!](https://img.shields.io/badge/say-thanks-ff69b4.svg)](https://saythanks.io/to/kennethreitz)

License
----

MIT
