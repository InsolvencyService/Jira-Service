import os
from setuptools import setup


def get_requirements():
    reqs = []
    for filename in ["requirements.production.txt"]:
        with open(filename, "r") as f:
            reqs += [x.strip() for x in f.readlines()
                     if x.strip() and not x.strip().startswith("#")]
    return reqs

setup(
    author="Insolvency Service",
    author_email="DigitalWebApps@insolvency.gsi.gov.uk",
    name='JiraService',
    packages=['jira_receiver'],
    version=os.environ.get('BUILD_NUMBER', '0'),
    install_requires=get_requirements(),
    include_package_data=True,
)