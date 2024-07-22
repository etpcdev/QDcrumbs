"""
#######################################################################
#######################################################################
                       Quick & Dirty Breadcrumbs
                                QDCrumbs        

This package provides a simple way to add dynamic breadcrumbs to a
Flask application. The breadcrumbs can easily be used in a jinja2
template (see example.html and the below example).

QDcrumbs work in both the main Flask application and in Flask 
Blueprints, and currently support a single variable page, simply import
qdcrumb from qdcrumbs and follow the examples below.

Get started:
Getting started with qdcrumbs is easy! Import the qdcrumb object 
(from qdcrumbs import qdcrumb) and follow the example below.

The following examples work both in the main Flask app and Blueprints!
Standard Usage:
    @app.route('/')
    def my_page():
        x = qdcrumb.get_crumbs()
        return render_template('/my_page.html', breadcrumbs=x)

With a variable name: 
    @app.route('/path/to/<var>')
    def my_page(var):
        x = qdcrumb.get_crumbs(var)
        return render_template(f'/path/to/{var}.html', breadcrumbs=x)

IMPORTANT!
qdcrumb.get_crumbs() must be called from within a function that points
to a resource's route.
    I.E. a function with the route decorator 
    (@app.route | @blueprint.route)
This is because the url is resolved via Flask itself, using url_for()
which takes the name of the function that was decorated.

Breadcrumbs are provided as a list of the Breadcrumb class and have the
following attributes:
    url     -->     Path to the current page/resource & preceding
                    pages.
    text    -->     Name of the current page/resource.

The breadcrumbs do not provide the site's root directory, this can be
added manually trivially (see example.html).

For usage in jinja2 refer to example.html

#######################################################################
#######################################################################
"""
from .qdcrumb import QDCrumbs

qdcrumb = QDCrumbs()
