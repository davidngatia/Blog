import unittest

from app.models import Comment,User
from app import db

class CommentModelTest(unittest.TestCase):

    def setUp(self):
        self.user_david = User(username = 'david',password = '1234', email = 'machngatia@gmail.com')
        self.new_comment = Comment(comment='best',user = self.user_david )

    def tearDown(self):
        Comment.query.delete()
        User.query.delete()
    def test_check_instance_variables(self):

        self.assertEquals(self.new_comment.comment,'best')
        self.assertEquals(self.new_comment.user,self.user_david)

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)
