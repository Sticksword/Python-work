import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'TennisScheduler.settings'

# Force Django to reload its settings.
from django.conf import settings
settings._target = None

from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.api import images
from decimal_property import DecimalProperty
from decimal import *
from datetime import datetime

import webapp2
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

DEFAULT_SCHEDULE = 'default_schedule'

# We set a parent key on the 'Greetings' to ensure that they are all
# in the same entity group. Queries across the single entity group
# will be consistent.  However, the write rate should be limited to
# ~1/second.


def schedule_key(schedule_name=DEFAULT_SCHEDULE):
    """Constructs a Datastore key for a Reservation entity.
    We use schedule_name as the key. As of now, there's only 1 schedule so only need
    """
    return ndb.Key('Schedule', schedule_name)


class Student(ndb.Model):
    """Sub model for representing a user."""
    identity = ndb.StringProperty(indexed=False)
    email = ndb.StringProperty(indexed=False)


class Reservation(ndb.Model):
    user = ndb.StructuredProperty(Student)
    day = ndb.StringProperty()
    picture = ndb.BlobProperty(required=False)
    date = ndb.DateProperty()
    time = ndb.TimeProperty()


class AddReservation(webapp2.RequestHandler):
    def post(self):
        # We set the same parent key on the 'Greeting' to ensure each
        # Greeting is in the same entity group. Queries across the
        # single entity group will be consistent. However, the write
        # rate to a single entity group should be limited to
        # ~1/second.
        if not '' == self.request.get("add"):
            user = users.get_current_user()
            r = Reservation(parent=schedule_key())

            if user:
                r.user = Student(
                    identity=users.get_current_user().user_id(),
                    email=users.get_current_user().email())

            r.day = self.request.get('day')
            r.date = datetime.strptime(self.request.get('date'), "%m-%d-%Y").date()
            r.time = datetime.strptime(self.request.get('time'), '%I:%M%p').time()
            if self.request.get('img'):
                r.picture = images.resize(self.request.get('img'), 64, 64)
            r.put()

        # query_params = {'grocerylist_name': grocerylist_name}
        # self.redirect('/?' + urllib.urlencode(query_params))
        self.redirect('/')

class Home(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        reservations_query = Reservation.query(
            ancestor=schedule_key(DEFAULT_SCHEDULE)).order(-Reservation.date)
        entries = reservations_query.fetch()

        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
            template = JINJA_ENVIRONMENT.get_template('index_after_login.html')
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'
            template = JINJA_ENVIRONMENT.get_template('index.html')

        template_values = {
            'user': user,
            'entries': entries,
            'url': url,
            'url_linktext': url_linktext,
            }
        self.response.write(template.render(template_values))

# We dun need pix at da moment
# class Image(webapp2.RequestHandler):
#     def get(self):
#         entry_id = int(self.request.get('key_id'))
#         item = Reservation.get_by_id(entry_id, parent=schedule_key())
#         if item:
#             self.response.headers['Content-Type'] = 'image/png'
#             self.response.write(item.picture)
#         else:
#             self.error(404)
#             self.response.write('No image')

application = webapp2.WSGIApplication([
    ('/', Home),
    # ('/img', Image),
    ('/addReservation', AddReservation),
], debug=True)
