import unittest
from app import app

class BasicTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_feedback_submission(self):
        response = self.app.post('/submit', data={
            'name': 'Alice',
            'email': 'alice@example.com',
            'service_id': 1,
            'feedback_type': '긍정적',
            'feedback_content': 'Great service!'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after submission

if __name__ == '__main__':
    unittest.main()
