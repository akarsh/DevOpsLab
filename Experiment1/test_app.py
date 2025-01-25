import unittest
from app import app

class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_register_get(self):
        response = self.app.get('/register')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Register', response.data)

    def test_register_post(self):
        response = self.app.post('/register', data=dict(
            name='Test User',
            email='test@example.com',
            password='password'
        ))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Success', response.data)

if __name__ == '__main__':
    unittest.main()
