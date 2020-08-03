# Tanjil's Website  
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)  

[![Website lbesson.bitbucket.org](https://img.shields.io/website-up-down-green-red/http/lbesson.bitbucket.org.svg)](https://flask-tanjil.herokuapp.com/)
[![Codefresh build status]( https://g.codefresh.io/api/badges/pipeline/tanjil/default%2Fkhansite?key=eyJhbGciOiJIUzI1NiJ9.NWU5OWYxMzQ3ZjczZDcyZmQ1NGU4Yjgx.5yP5JcVolgL_vWAyde5tk32fbZhvo5N6mvjqILjqR6Q&type=cf-1)]( https%3A%2F%2Fg.codefresh.io%2Fpipelines%2Fkhansite%2Fbuilds%3Ffilter%3Dtrigger%3Abuild~Build%3Bpipeline%3A5eb450ec7641237f6f2c08ca~khansite)
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Khantanjil/tanjil-s-website/blob/master/LICENSE)
[![GitHub version](https://badge.fury.io/gh/Naereen%2FStrapDown.js.svg)](https://github.com/Naereen/StrapDown.js)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)  
The website was made with python via Flask  
My website deployed with Heroku CLI and was created with the micro web framework called flask in python script and is a simple blog programming to practice and do my hobby's program skills  
  
### Usages

This was builded with
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Mini Framework Based in Python
* [Python](https://www.python.org/) -  general-purpose programming language
* [HTML](https://devdocs.io/html/) - Hypertext Markup Language, sandard markup language for documents designed to be displayed in a web browser
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) - Cascading Style Sheets, style sheet language used for describing the presentation of a document written in a markup language like HTML.
* [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/) - Jinja is a web template engine for the Python programming language 
* [Folium](https://python-visualization.github.io/folium/) - Python data, leaflet.js maps
* [Pandas](https://pandas.pydata.org/) - Python Data Analysis Library
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Python package for parsing HTML and XML documents. It creates a parse tree for parsed pages that can be used to extract data from HTML
* [Requests](https://requests.readthedocs.io/en/master/)- Requests is a Python HTTP library, released under the Apache License 2.0. The goal of the project is to make HTTP requests simpler and more human-friendly

### Installation (Updated)
Activate the virtual environment with these steps:
```sh
cd virtualEnv
source bin/activate
cd ..
```

## Running the server
Start the application with 
```sh
python app.py
```
Verify the deployment by navigating to your server address in your preferred browser.

```sh
127.0.0.1:5000
```

## Optional
If you d'like to change the port, you can edit the file with your preferred editor, so i choose nano:
```sh
nano app.py 
```
After, you can edit on the next line
```py
if __name__ == '__main__':
    app.run(debug=True)
```
To
```py
if __name__ == '__main__':
    # Changes the nº port
    app.run(debug=True, port=8080) 
```
[![thank you!](https://img.shields.io/badge/say-thanks-ff69b4.svg)](https://saythanks.io/to/kennethreitz)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://github.com/Khantanjil/tanjil-s-website/issues/1)

## Live website deployed with heroku
* [Website](https://flask-tanjil.herokuapp.com/tanjil) - Main page
* [Website](https://flask-tanjil.herokuapp.com/about) - About page
* [Website](https://flask-tanjil.herokuapp.com/) - Home page

## MetPort
MetPort is a webmap, can view which are they the actual max temperatures on various cities on portugal.
Was builded too with folium. The webmap can be accessed with this link.
* [Website](https://flask-tanjil.herokuapp.com/met) - MetPort

## Images
![](https://media.discordapp.net/attachments/688091927085580312/700321580034818078/Screenshot_from_2020-04-16_13-26-47.png?width=549&height=309)

License
----

MIT
