from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unittest


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # user browses to homepage of app
        self.browser.get(self.live_server_url)
        
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

        # pressing enter, the user is taken to a new URL,
        # now the page lists "1: Buy peacock feathers" as an item
        # in a to-do list table
        inputbox.send_keys(Keys.ENTER)
        test_user_list_url = self.browser.current_url
        self.assertRegex(test_user_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # textbox asks user to add another item
        # so the user adds another item
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        
        # the page updates again and now shows both items
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table(
            '2: Use peacock feathers to make a fly')
        
        # now a new user visits the site
        # we start a new browser session to make sure no information
        # from the first user is coming through cookies, etc
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # new user visits the home page
        # there is no sign of the first user's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # new user starts a new list by entering an item
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        # new user gets a unique URL
        new_user_list_url = self.browser.current_url
        self.assertRegex(new_user_list_url, '/lists/.+')
        self.assertNotEqual(new_user_list_url, test_user_list_url)

        # still no trace of Edith's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        self.fail('Finish the test!')
        # the user visits the unique url and sees that
        # the list is still there