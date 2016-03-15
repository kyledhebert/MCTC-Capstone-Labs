from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # user browses to homepage of app
        self.browser.get('http://localhost:8000')

        # user notices page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # user is invited to enter a to-do item

        # user types a to-do into a text box

        # user press enter, and the page updates
        # page now shows the to-do as an item on the to-do list

        # textbox asks user to add another item

        # the page updates again and now shows both items

        # the site generates a unique url for the user
        # and explains that it has done so

        # the user visits the unique url and sees that
        # the list is still there

if __name__ == '__main__':
    unittest.main(warnings='ignore')
            
