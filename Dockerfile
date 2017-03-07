FROM python:2.7.13-alpine
MAINTAINER "The Insolvency Service DigitalWebApps@insolvency.gsi.gov.uk"
ARG BUILD_NUMBER=0
EXPOSE 5000
ENV APP_DEBUG=true \
    APP_TESTING=true \
    APP_MAIL_SENDER_ADDRESS=test_email@test.com \
    APP_RECIPIENTS=[\"test_email@test.com\"]
COPY dist/JiraService-$BUILD_NUMBER-py2-none-any.whl /
RUN pip install --no-cache-dir /JiraService-$BUILD_NUMBER-py2-none-any.whl
CMD ["gunicorn","-b :5000","-w 4","jira_receiver:app"]