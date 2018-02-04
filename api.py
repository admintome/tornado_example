import tornado.ioloop
import tornado.web
from book import Book
from addhandler import AddHandler
from delhandler import DelHandler
from gethandler import GetHandler

books = Book()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Book Microservice v1")

def make_app():
    return tornado.web.Application([
        (r"/v1", MainHandler),
        (r"/v1/addbook", AddHandler, dict(books = books)),
        (r"/v1/delbook", DelHandler, dict(books = books)),
        (r"/v1/getbooks", GetHandler, dict(books = books)),
        ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
