import unittest
import sys
import os

# Add parent directory to path to import app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app


class TestApp(unittest.TestCase):
    
    def setUp(self):
        """Set up test client"""
        self.app = app.test_client()
        self.app.testing = True

    def test_health_endpoint(self):
        """Test health check endpoint"""
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['status'], 'ok')

    def test_hello_endpoint(self):
        """Test hello API endpoint"""
        response = self.app.get('/api/hello')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Hello from Flask backend!')

    def test_data_get_endpoint(self):
        """Test data GET endpoint"""
        response = self.app.get('/api/data')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['data'], 'Sample data from backend')

    def test_data_post_endpoint(self):
        """Test data POST endpoint"""
        test_data = {'test': 'value'}
        response = self.app.post('/api/data', 
                                json=test_data,
                                content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['received'], test_data)
        self.assertEqual(response.json['status'], 'success')

    def test_404_endpoint(self):
        """Test non-existent endpoint returns 404"""
        response = self.app.get('/api/nonexistent')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()