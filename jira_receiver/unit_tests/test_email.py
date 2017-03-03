import unittest

from hamcrest import assert_that
from hamcrest import equal_to

from jira_receiver.email_builder import _render_template
from jira_receiver.unit_tests.test_data import expected_output_dict, expected_empty_output_dict


class TestEmailRenderer(unittest.TestCase):
    def test_email_content_rendered_from_model_sc(self):
        html = _render_template(expected_output_dict, "released_to_production")
        expected_response = open("jira_receiver/unit_tests/test_emails/test_email_sc.html", "r").read()

        assert_that(html, equal_to(expected_response))

    def test_email_content_rendered_from_model_ar(self):
        html = _render_template(expected_output_dict, "awaiting_release")
        expected_response = open("jira_receiver/unit_tests/test_emails/test_email_ar.html", "r").read()

        assert_that(html, equal_to(expected_response))

    def test_renders_blank_template_if_empty_model_sc(self):
        html = _render_template(expected_empty_output_dict, "released_to_production")
        expected_response = open("jira_receiver/unit_tests/test_emails/test_email_empty_sc.html", "r").read()

        assert_that(html, equal_to(expected_response))

    def test_renders_blank_template_if_empty_model_ar(self):
        html = _render_template(expected_empty_output_dict, "awaiting_release")
        expected_response = open("jira_receiver/unit_tests/test_emails/test_email_empty_ar.html", "r").read()

        assert_that(html, equal_to(expected_response))