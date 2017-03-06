import unittest
from jira_receiver.__init__ import check_app_config_set
from hamcrest import assert_that, equal_to
from flask import Flask
testapp = Flask(__name__)

testapp.config.setdefault('MAIL_SENDER_ADDRESS', 'TestDefault')

class TestConfig(unittest.TestCase):
    def test_config_works(self):
        config_app = check_app_config_set(testapp)
        config_value = config_app.config.get('MAIL_DEFAULT_SENDER')
        expected_response = ('Insolvency Service Jira', 'TestDefault')
        assert_that(config_value, equal_to(expected_response))

