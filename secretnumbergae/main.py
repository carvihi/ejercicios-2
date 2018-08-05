#!/usr/bin/env python
import os
import jinja2
import webapp2
import random


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))

secret = random.randint(1, 10)
class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("hello.html")

    def post(self):

        guess = int(self.request.get("guess"))
        result = None

        if guess == secret:
            result = "Congratulations!!! The secret number is " + str(secret)

        elif guess < secret:
            result= "Sorry, try again with a higher number"

        elif guess > secret:
            result= "Sorry, try again with a smaller number"

        params={"result":result}

        return self.render_template("result.html", params=params)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)
