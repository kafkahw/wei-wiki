import webapp2

class Welcome(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write("<h1>Welcome to Wei's wiki!</h1><br><br> Try to post a wiki page.")

app = webapp2.WSGIApplication([('/', Welcome),
                              ],
                              debug=True)
