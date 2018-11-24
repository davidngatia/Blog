import unittest

from app.models import Comment,User,Blog
from app import db

class BlogModelTest(unittest.TestCase):

    def setUp(self):
        self.user_david = User(username = 'david',password = '1234', email = 'machngatia@gmail.com')
        self.new_blog = Blog(title="car"blog='best means',user = self.user_david )

    def tearDown(self):
        Blog.query.delete()
        User.query.delete()
    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.title,'car')

        self.assertEquals(self.new_blog.blog,'best means')
        self.assertEquals(self.new_blog.user,self.user_david)

    def test_save_blog(self):
        self.new_blog.save_blog()
        self.assertTrue(len(Blog.query.all())>0)
