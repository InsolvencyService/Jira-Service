from jinja2 import PackageLoader, Environment
from flask_mail import Message
from logging import getLogger

logger = getLogger(__name__)


def _render_template(model, template):
    env = Environment(loader=PackageLoader('jira_receiver', 'templates'))
    html_template = env.get_template(template + '.j2.html')
    return html_template.render(model)


def build_email(model, template, recipients):
    email = Message(
        "Production Release",

    )
    email.html = _render_template(model, template)
    for recipient in recipients:
        email.add_recipient(recipient)
    return email
