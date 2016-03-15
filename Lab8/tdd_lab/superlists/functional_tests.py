from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # user browses to homepage of app
        self.browser.get('http://localhost:8000')
        
        # user notices page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # user is invited to enter a to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),
                         'Enter a to-do item')

        # user types a to-do into a text box
        inputbox.send_keys('Buy peacock feathers')
        # user press enter, and the page updates
        inputbox.send_keys(Keys.ENTER)
        # page now shows the to-do as an item on the to-do list
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows))

        # textbox asks user to add another item
        self.fail('Finish the test!')
        # the page updates again and now shows both items

        # the site generates a unique url for the user
        # and explains that it has done so

        # the user visits the unique url and sees that
        # the list is still there

if __name__ == '__main__':
    unittest.main(warnings='ignore')
            
