import unittest
from bs4 import BeautifulSoup
from app.helpers import embrapa as helper
from mock import mocks

class TestJsonFunctions(unittest.TestCase):

    def setUp(self):
        # HTML simulado para testes
        self.html_mock1 = mocks.mock_html1()

        self.html_mock2 = mocks.mock_html2()


    def test_get_json(self):
        soup = BeautifulSoup(self.html_mock1, 'html.parser')
        result = helper.get_json(soup)
        print(result)
        expected = mocks.expected_html1()
        self.assertEqual(result, expected)

    def test_get_json2(self):
        soup = BeautifulSoup(self.html_mock2, 'html.parser')
        result = helper.get_json2(soup)
        print(result)
        expected = mocks.expected_html2()
        print(expected)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
