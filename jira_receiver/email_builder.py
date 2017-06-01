from jinja2 import PackageLoader, Environment
from flask_mail import Message
from logging import getLogger

logger = getLogger(__name__)


def build_email(model, template, recipients, subject):
    email = Message(
        subject,
    )

    email.html = _render_template(model, template)

    _add_recipients(email, model, recipients)

    return email


def _render_template(model, template):
    env = Environment(loader=PackageLoader('jira_receiver', 'templates'))
    html_template = env.get_template(template + '.j2.html')
    return html_template.render(model)


def _add_recipients(email, model, recipients):
    for recipient in recipients:
        email.add_recipient(recipient)

    if model.get("transitioned_by_email") != "":
        email.add_recipient(model.get("transitioned_by_email"))
    if model.get("assignee_email") != "":
        email.add_recipient(model.get("assignee_email"))
