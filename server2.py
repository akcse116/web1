import urllib.request
import requests
import json
import bottle
import launches
import input_handling
from hitCounter import count
from bottle import route, post, run, static_file, request, redirect, error

# *****************************************************
# ***********************VARIABLES*********************

url1 = "https://api.spacexdata.com/v3/launches/upcoming?limit=10"
url2 = "https://api.spacexdata.com/v3/launches/past"
url3 = "https://api.spacexdata.com/v3/launches/past?limit=10"
url4 = "https://api.spacexdata.com/v3/launches/latest"


# *********************** INDEXES *********************


@route('/')
def get_index():
    count()
    return static_file("indexHome.html", root='')


@route('/about')
def get_indexAbout():
    return static_file("indexAbout.html", root='')


@route('/LH')
def get_indexLH():
    return static_file("indexLH.html", root='')


@route('/failed_page')
def get_indexFail():
    return static_file("indexFail.html", root='')


@route('/info')
def get_indexInfo():
    return static_file("indexInfo.html", root='')


@route('/robots.txt')
def get_permission():
    return static_file("robots.txt", root='')


@route('/sitemap')
def get_sitemap():
    return static_file("sitemap.xml", root='')


@error(404)
def error404(error):
    return '404 Nothing here. Have you seen this page?'


# ********** END INDEXES **********


# ********** SUPPORT FILES **********


@route('/LHlogo')
def logo():
    return static_file("LHlogo.png", root='')


@route('/tabimg')
def favicon():
    return static_file("LH favicon.png", root='')


@route('/charts')
def graphes():
    return static_file("charts.js", root='')

# ********** END SUPPORT FILES **********

# ********** SORTED LAUNCH FILES **********


@route('/upcoming')
def get_upcoming_launches():
    return launches.get_launch_data(url1)


@route('/past')
def get_past10_launches():
    return launches.get_launch_data_past_sort(url2)


@route('/allPast')
def get_all_past_launches():
    return launches.get_launch_data(url2)


@route('/latest')
def get_latest_launches():
    return launches.get_latest_launch_data(url4)


@route('/failed')
def get_failed_launches_data():
    return launches.get_failed_launches(url2)


@route('/site_count')
def get_site_count():
    return launches.launch_locations(url2)


# ********** POST **********


@post('/about')
def do_submit():
    content = request.forms.get('email')
    input_handling.add_email(content)
    redirect('/about')
    return "Confirmed"

# ********** BOTTLE RUN **********


bottle.run(host='0.0.0.0', port=8080, debug=True)