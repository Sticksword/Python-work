import urllib
import os

from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.api import images
from decimal_property import DecimalProperty
from decimal import *

import webapp2
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

DEFAULT_GROCERY_LIST = 'default_grocerylist'

# We set a parent key on the 'Greetings' to ensure that they are all
# in the same entity group. Queries across the single entity group
# will be consistent.  However, the write rate should be limited to
# ~1/second.


def grocerylist_key(username, grocerylist_name=DEFAULT_GROCERY_LIST):
    """Constructs a Datastore key for a Grocerylist entity.

    We use grocerylist_name as the key.
    UPDATE: We now use username as the key so that each Grocerylist entity/datastore is tied with an account.
    """
    return ndb.Key('grocerylist', username)


class Author(ndb.Model):
    """Sub model for representing an author."""
    identity = ndb.StringProperty(indexed=False)
    email = ndb.StringProperty(indexed=False)


class GroceryItem(ndb.Model):
    author = ndb.StructuredProperty(Author)
    name = ndb.StringProperty()
    cost = DecimalProperty()
    number = ndb.IntegerProperty()
    total = DecimalProperty()
    picture = ndb.BlobProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)


class Groceries(webapp2.RequestHandler):
    def post(self):
        # We set the same parent key on the 'Greeting' to ensure each
        # Greeting is in the same entity group. Queries across the
        # single entity group will be consistent. However, the write
        # rate to a single entity group should be limited to
        # ~1/second.
        # grocerylist_name = self.request.get('grocerylist_name',
        #                                   DEFAULT_GROCERY_LIST)
        # item = GroceryItem(parent=grocerylist_key(grocerylist_name))
        if not '' == self.request.get("add"):
            user = users.get_current_user()
            item = GroceryItem(parent=grocerylist_key(user.user_id()))

            if user:
                item.author = Author(
                    identity=users.get_current_user().user_id(),
                    email=users.get_current_user().email())

            item.name = self.request.get('name')
            item.cost = Decimal(self.request.get('cost'))
            item.number = int(self.request.get('number'))
            item.picture = images.resize(self.request.get('img'), 64, 64)
            item.total = item.cost * item.number
            item.put()
        elif not '' == self.request.get("clear"):
            ndb.delete_multi(
                GroceryItem.query().fetch(keys_only=True)
            )

        # query_params = {'grocerylist_name': grocerylist_name}
        # self.redirect('/?' + urllib.urlencode(query_params))
        self.redirect('/')

class GroceriesUI(webapp2.RequestHandler):
    def get(self):
        # grocerylist_name = self.request.get('grocerylist_name',
        #                                   DEFAULT_GROCERY_LIST)
        # groceries_query = GroceryItem.query(
        #     ancestor=grocerylist_key(grocerylist_name)).order(-GroceryItem.date)
        user = users.get_current_user()

        if user:
            groceries_query = GroceryItem.query(
                ancestor=grocerylist_key(user.user_id())).order(-GroceryItem.date)
            items = groceries_query.fetch()
            total = 0
            for item in items:
                total += item.number * item.cost

            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'

            template_values = {
                'user': user,
                'items': items,
                # 'grocerylist_name': urllib.quote_plus(grocerylist_name),
                'url': url,
                'url_linktext': url_linktext,
                'total': total
            }
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'
            template_values = {
                'url': url,
                'url_linktext': url_linktext,
            }

        if user:
            template = JINJA_ENVIRONMENT.get_template('grocerybuddy_UI.html')
        else:
            template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))


class Image(webapp2.RequestHandler):
    def get(self):
        # grocerylist_name = self.request.get('grocerylist_name',
        #                                   DEFAULT_GROCERY_LIST)
        # grocerylist_id = int(self.request.get('key_id'))
        user_id = int(self.request.get('key_id'))
        # item = GroceryItem.get_by_id(grocerylist_id, parent=grocerylist_key(grocerylist_name))
        item = GroceryItem.get_by_id(user_id, parent=grocerylist_key(users.get_current_user().user_id()))
        if item:
            self.response.headers['Content-Type'] = 'image/png'
            self.response.write(item.picture)
        else:
            self.error(404)
            self.response.write('No image')

application = webapp2.WSGIApplication([
    ('/', GroceriesUI),
    ('/img', Image),
    ('/additem', Groceries),
], debug=True)
