import unittest
import json

from hamcrest import assert_that, equal_to
from test_data import issue_updated_json, expected_output_dict, expected_empty_output_dict
from jira_receiver.transformations import transform_issue_updated_data, _get_nested_value, _map_values


class TestTransformations(unittest.TestCase):
    def test_transform_returns_story_number(self):
        output = transform_issue_updated_data(json.dumps(issue_updated_json))

        assert_that("story_number" in output)
        assert_that(output.get("story_number"), equal_to("ADS-166"))

    def test_transform_returns_no_story_number(self):
        output = transform_issue_updated_data(json.dumps({}))

        assert_that("story_number" in output)
        assert_that(output.get("story_number"), equal_to(""))

    def test_transform_returns_story_title(self):
        output = transform_issue_updated_data(json.dumps(issue_updated_json))

        assert_that("title" in output)
        assert_that(output.get("title"), equal_to("Notify Service Management of Release"))

    def test_transform_returns_no_story_title(self):
        output = transform_issue_updated_data(json.dumps({}))

        assert_that("title" in output)
        assert_that(output.get("title"), equal_to(""))

    def test_transform_returns_transitioned_by(self):
        output = transform_issue_updated_data(json.dumps(issue_updated_json))

        assert_that("transitioned_by" in output)
        assert_that(output.get("transitioned_by"), equal_to("Andy Price"))

    def test_transform_returns_no_transitioned_by(self):
        output = transform_issue_updated_data(json.dumps({}))

        assert_that("transitioned_by" in output)
        assert_that(output.get("transitioned_by"), equal_to(""))

    def test_transform_returns_assignee(self):
        output = transform_issue_updated_data(json.dumps(issue_updated_json))

        assert_that("assignee" in output)
        assert_that(output.get("assignee"), equal_to("Andy Price"))

    def test_transform_returns_no_assignee(self):
        output = transform_issue_updated_data(json.dumps({}))

        assert_that("assignee" in output)
        assert_that(output.get("assignee"), equal_to(""))

    def test_transform_returns_sign_off_by(self):
        output = transform_issue_updated_data(json.dumps(issue_updated_json))

        assert_that("sign_off_by" in output)
        assert_that(output.get("sign_off_by"), equal_to("James Warren"))

    def test_transform_returns_no_sign_off_by(self):
        output = transform_issue_updated_data(json.dumps({}))

        assert_that("sign_off_by" in output)
        assert_that(output.get("sign_off_by"), equal_to(""))

    def test_transform_returns_estimated_release_date(self):
        output = transform_issue_updated_data(json.dumps(issue_updated_json))

        assert_that("estimated_release_date" in output)
        assert_that(output.get("estimated_release_date"), equal_to("2017-02-20"))

    def test_transform_returns_no_estimated_release_date(self):
        output = transform_issue_updated_data(json.dumps({}))

        assert_that("estimated_release_date" in output)
        assert_that(output.get("estimated_release_date"), equal_to(""))

    def test_transform_returns_full_dataset(self):
        output = transform_issue_updated_data(json.dumps(issue_updated_json))

        assert_that(output, equal_to(expected_output_dict))

    def test_transform_returns_no_assignee(self):
        output = transform_issue_updated_data(json.dumps({}))

        assert_that(output, equal_to(expected_empty_output_dict))


class TestNestedGetValue(unittest.TestCase):
    def test_get_value_returns_empty_if_all_empty(self):
        input_dict = dict()
        path = tuple()
        result = _get_nested_value(input_dict, path)
        assert_that(result, equal_to(""))

    def test_get_value_returns_empty_string(self):
        input_dict = dict()
        path = ("key", "key2")
        result = _get_nested_value(input_dict, path)
        assert_that(result, equal_to(""))

    def test_get_value_returns_single_nested_value(self):
        input_dict = {
            "key": {
                "key2": "value"
            }
        }
        path = ("key", "key2")
        result = _get_nested_value(input_dict, path)
        assert_that(result, equal_to("value"))

    def test_get_value_returns_double_nested_value(self):
        input_dict = {
            "key": {
                "key2": {
                    "key3": "value"
                }
            }
        }
        path = ("key", "key2", "key3")
        result = _get_nested_value(input_dict, path)
        assert_that(result, equal_to("value"))


class TestMapValues(unittest.TestCase):
    def test_map_values_returns_empty_set(self):
        input_dict = dict()
        mapping_dict = {
            "story_number": "",
            "title": "",
            "transitioned_by": "",
            "assignee": "",
            "sign_off_by": "",
            "estimated_release_date": ""
        }

        output_dict = _map_values(input_dict, mapping_dict)
        assert_that(output_dict, equal_to(expected_empty_output_dict))

    def test_map_values_returns_full_set(self):
        mapping_dict = {
            "story_number": ("issue", "key"),
            "title": ("issue", "fields", "summary"),
            "transitioned_by": ("user", "displayName"),
            "assignee": ("issue", "fields", "assignee", "displayName"),
            "sign_off_by": ("issue", "fields", "customfield_11300"),
            "estimated_release_date": ("issue", "fields", "customfield_11301")
        }

        output_dict = _map_values(issue_updated_json, mapping_dict)
        assert_that(output_dict, equal_to(expected_output_dict))
