import unittest
from models import Sources
Source = source.Source

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources("abc-news","ABC News","Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.","https://abcnews.go.com")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))


if __name__ == '__main__':
    unittest.main()