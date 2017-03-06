from flask import Flask
from flask_mail import Mail
import envcfg.smart.app
import logging

mail = Mail()
app = Flask(__name__)
app.config.from_object('envcfg.smart.app')


def check_app_config_set(app):
    if "MAIL_SENDER_ADDRESS" in app.config:
        app.config["MAIL_DEFAULT_SENDER"] = ("Insolvency Service Jira", app.config["MAIL_SENDER_ADDRESS"])

    if not app.config["DEBUG"]:
        app.logger.addHandler(logging.StreamHandler())
        app.logger.setLevel(logging.INFO)
    return app


check_app_config_set(app)

mail.init_app(app)

import jira_receiver.routes
