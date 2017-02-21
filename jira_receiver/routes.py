from jira_receiver import app as jira_receiver, mail
from flask import request, current_app
from jira_receiver.transformations import transform_issue_updated_data
from jira_receiver.email_builder import build_email
from logging import getLogger

logger = getLogger(__name__)


@jira_receiver.route('/health-check', methods=["GET"])
def health_check():
    return "Service Running", 200


@jira_receiver.route('/story-complete', methods=["POST"])
def accept_post():
    logger.info("Request Received")
    if request.data:
        model = transform_issue_updated_data(request.data)
        logger.info("Calling Mail Builder")
        email = build_email(model, "released_to_production", current_app.config["RECIPIENTS"])
        logger.info("Mail Built - Sending")
        mail.send(email)
        logger.info("Mail Sent")
        return "Request Received", 202
    else:
        logger.error("No Request Data")
        return "Bad Request", 400
