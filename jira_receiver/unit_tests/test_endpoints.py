import unittest
import json

from hamcrest import assert_that, equal_to
from jira_receiver.routes import jira_receiver
from mock import patch


class TestEndpoints(unittest.TestCase):
    issue_updated_json = {
        "user": {
            "displayName": "Andy Price",
        },
        "issue": {
            "key": "ADS-166",
            "fields": {
                "issuetype": {
                    "name": "Story",
                },
                "customfield_11300": "James Warren",
                "customfield_11301": "2017-02-20",
                "assignee": {
                    "displayName": "Andy Price",
                },
                "updated": "2017-02-14T11:51:10.766+0000",
                "summary": "Notify Service Management of Release",
            },
        },
    }

    def setUp(self):
        self.app = jira_receiver.test_client()

    def test_health_check(self):
        response = self.app.get('/health-check')
        assert_that(response.status, equal_to('200 OK'))
        assert_that(response.data, equal_to('Service Running'))

    #Story complete

    def test_receiver_returns_400_on_get_sc(self):
        response = self.app.get('/story-complete')
        assert_that(response.status, equal_to('405 METHOD NOT ALLOWED'))

    def test_receiver_returns_error_if_no_data_sc(self):
        response = self.app.post('/story-complete', headers={'Content-Type': 'application/json'})
        assert_that(response.status, equal_to('400 BAD REQUEST'))

    def test_receiver_accepts_json_sc(self):
        response = self.app.post('/story-complete', data="{}", headers={'Content-Type': 'application/json'})
        assert_that(response.status, equal_to('202 ACCEPTED'))
        assert_that(response.data, equal_to('Request Received'))

    def test_receiver_accepts_jira_json_sc(self):
        response = self.app.post('/story-complete', data=json.dumps(self.issue_updated_json), content_type='application/json')
        assert_that(response.status, equal_to('202 ACCEPTED'))
        assert_that(response.data, equal_to('Request Received'))

    @patch('jira_receiver.routes.transform_issue_updated_data')
    def test_receiver_calls_transformation_sc(self, transform):
        self.app.post('/story-complete', data=json.dumps(self.issue_updated_json), content_type='application/json')
        transform.assert_called()

    #Awaiting release

    def test_receiver_returns_400_on_get_ar(self):
        response = self.app.get('/awaiting-release')
        assert_that(response.status, equal_to('405 METHOD NOT ALLOWED'))

    def test_receiver_returns_error_if_no_data_ar(self):
        response = self.app.post('/awaiting-release', headers={'Content-Type': 'application/json'})
        assert_that(response.status, equal_to('400 BAD REQUEST'))

    def test_receiver_accepts_json_ar(self):
        response = self.app.post('/awaiting-release', data="{}", headers={'Content-Type': 'application/json'})
        assert_that(response.status, equal_to('202 ACCEPTED'))
        assert_that(response.data, equal_to('Request Received'))

    def test_receiver_accepts_jira_json_ar(self):
        response = self.app.post('/awaiting-release', data=json.dumps(self.issue_updated_json), content_type='application/json')
        assert_that(response.status, equal_to('202 ACCEPTED'))
        assert_that(response.data, equal_to('Request Received'))

    @patch('jira_receiver.routes.transform_issue_updated_data')
    def test_receiver_calls_transformation_ar(self, transform):
        self.app.post('/awaiting-release', data=json.dumps(self.issue_updated_json), content_type='application/json')
        transform.assert_called()



