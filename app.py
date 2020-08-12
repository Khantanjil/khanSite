# Import the librarys
#from flask import send_file
from flask import Flask
from flask import render_template
from bokeh.plotting import figure
from bokeh.plotting import show
from bokeh.plotting import output_file
from bokeh.embed import components
from bokeh.resources import CDN
from pandas_datareader import data
import datetime
from flask import request
#from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy.sql import func
#from send_email import send_email
from werkzeug.utils import secure_filename
import run
import folium

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:newpassword@localhost/height_collector'
"""
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgres://orrwejuxdvxcpe:41fe360787ddfc7991e04ed180efe3c2527221aa45ac2461fc88ae8fd5e9e138@ec2-54-152-175-141.compute-1.amazonaws.com:5432/d333bpqpqjrsi4?sslmode=require'

db = SQLAlchemy(app)
class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    email_ = db.Column(db.String(120), unique=True)
    height_ = db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_ = email_
        self.height_ = height_

"""
# Decorator Home Page
@app.route('/')
def home():
    return render_template('main.html')

@app.route('/met')
def met():
    return render_template("meteo.html")

@app.route('/ip')
def ip():
    return render_template("ip.html")

@app.route('/test')
def test():
    return render_template("test.html")

@app.route('/layout')
def layout():
    return render_template("layout.html")


# @app.route('/about')
# def about():
#    return render_template('about.html')

# Tanjil website
@app.route('/tanjil')
def tanjil():
    return render_template("home.html")
    


@app.route('/webmap')
def webmap():
    return render_template('world.html')


@app.route('/webapp')
def webapp():
    return render_template("index.html")


@app.route('/webapp/success', methods=["POST"])
def success():
    if request.method == 'POST':
        file = request.files["file"]



@app.route('/programming')
def about():
    start = datetime.datetime(2019, 11, 10)
    end = datetime.datetime.now()
    df = data.DataReader(name="GOOG", data_source="yahoo", start=start, end=end)

    data_increase = df.index[df.Close > df.Open]
    data_decrease = df.index[df.Close < df.Open]

    df["Status"] = [inc_dec(c, o) for c, o in zip(df.Close, df.Open)]
    df["Middle"] = (df.Open + df.Close) / 2
    df["Height"] = abs(df.Close - df.Open)
    p = figure(x_axis_type="datetime", width=1000, height=300, sizing_mode="scale_width")
    p.title.text = "Candlestick Chart"
    p.grid.grid_line_alpha = 0.3
    hours_12 = 12 * 60 * 60 * 1000
    p.segment(df.index, df.High, df.index, df.Low, color="black")
    p.rect(df.index[df.Status == "Increase"], df.Middle[df.Status == "Increase"], hours_12,
           df.Height[df.Status == "Increase"], fill_color="#CCFFFF", line_color="black")
    p.rect(df.index[df.Status == "Decrease"], df.Middle[df.Status == "Decrease"], hours_12,
           df.Height[df.Status == "Decrease"], fill_color="#FF3333", line_color="black")

    script1, div1 = components(p)
    cdn_js = CDN.js_files[0]

    # Setting the start and the end of the time
    start_2 = datetime.datetime(2019, 11, 10)
    end_2 = datetime.datetime.now()

    # Setting a data frame to Microsoft Stock Market
    df = data.DataReader(name="MSFT", data_source="yahoo", start=start_2, end=end_2)

    # Setting the graph
    plot = figure(width=1000, height=300, x_axis_type="datetime", sizing_mode="scale_width")

    # Setting the title of the graph
    plot.title.text = "Candlestick Chart"
    plot.title.text_color = "Gray"
    plot.title.text_font = "times"
    plot.title.text_color = "orange"
    plot.title.text_font_style = "italic"

    # Setting the label of the graph
    plot.xaxis.axis_label = "Date"
    plot.yaxis.axis_label = "Values"

    # Making a transparent lines
    plot.grid.grid_line_alpha = 0.3

    # Conditional which view if increased the value or decreased.
    def incr_decr(c, o):
        if c > o:
            value = "Increase"
        elif c < o:
            value = "Decrease"
        else:
            value = "Equal"
        return value

    # Creating a new column to view if was increased or decreased
    df["Status"] = [incr_decr(c, o) for c, o in zip(df.Close, df.Open)]

    # Creating a new column middle to put the plot rectangle on the middle
    df["Middle"] = (df.Close + df.Open) / 2

    # Creating a new column to setting up the height of the plot rectangle
    df["Height"] = abs(df.Close - df.Open)

    # Converts the 12 hours to milliseconds
    hours_12 = 12 * 60 * 60 * 1000

    # Setting up the output file
    output_file("Microsoft Stock Market.html")

    # Print out the current data frame
    #print(df)

    # Setting up the segment
    plot.segment(df.index, df.High, df.index, df.Low)

    # Setting up the rectangle which was INCREASED
    # THe first is the x axis, next is the y axis, the third is the width of the rectangles, next is the height.
    plot.rect(df.index[df.Status == "Increase"], df.Middle[df.Status == "Increase"], hours_12,
              df.Height[df.Status == "Increase"], fill_color="#CCFFFF", color="black")

    # Setting pup the rectangle which was DECREASED
    plot.rect(df.index[df.Status == "Decrease"],
              df.Middle[df.Status == "Decrease"],
              hours_12,
              df.Height[df.Status == "Decrease"], fill_color="#FF3333", color="black")

    script2, div2 = components(plot)
    cdn_js2 = CDN.js_files[0]

    return render_template("about.html", script1=script1, div1=div1, cdn_js=cdn_js, script2=script2, div2=div2,
                           cdn_js2=cdn_js2)


def inc_dec(c, o):
    if c > o:
        value = "Increase"
    elif c < o:
        value = "Decrease"
    else:
        value = "Equal"
    return value


if __name__ == '__main__':
    # Loads the website
    app.run(debug=True)
