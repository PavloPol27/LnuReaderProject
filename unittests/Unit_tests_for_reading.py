import unittest
from fitz import Document
from read_books import read_book, show_page

class Read_books_tests(unittest.TestCase):
    def test_reading_books_test1(self):
        test_file = "c++_trofumenko.pdf"
        actual_result = read_book(test_file).page_count
        expected_result = Document(test_file).page_count
        self.assertEqual(actual_result, expected_result)

    def test_reading_books_test2(self):
        test_file = "lala.doc"
        with self.assertRaises(Exception) as context:
            read_book(test_file)
        self.assertTrue("Wrong file format" in str(context.exception))

    def test_reading_books_test3(self):
        test_file = "c++_trofumenko.pdf"
        with self.assertRaises(Exception) as context:
            show_page(read_book(test_file), -1)
        self.assertTrue("Wrong page" in str(context.exception))

    def test_reading_books_test4(self):
        test_file = "c++_trofumenko.pdf"
        page = show_page(read_book(test_file), 24)
        self.assertTrue("ЕОМ" in page)



if __name__ == '__main__':
    unittest.main()