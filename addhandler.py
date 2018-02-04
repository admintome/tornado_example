import tornado.web
import book
import json


class AddHandler(tornado.web.RequestHandler):
    def initialize(self, books):
        self.books = books
        
    def get(self):
        title = self.get_argument('title')
        author = self.get_argument('author')
        result = self.books.add_book(title, author)
        self.write(result)
