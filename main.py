##########

import logging
import webapp2
from webapp2 import Route

from base_handler import BaseHandler

##########

config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'my-super-secret-key',
}

##########

class FrontPage(BaseHandler):
    
    def get(self):
        self.render('index.html')
        
    def post(self):
        pass


class PeoplePage(BaseHandler):
    
    def get(self):
        self.render('people.html')
        
    def post(self):
        pass
        
        
class AboutPage(BaseHandler):

    def get(self):
        self.render('about.html')
        
    def post(self):
        pass
        
##########

app = webapp2.WSGIApplication([
      ('/', FrontPage),
      ('/people', PeoplePage),
      ('/about', AboutPage)],
      config = config, debug = True)

if __name__ == '__main__':
    app.run()
    
