# API_Testing_practise_using_pytest_added_workflow_that_checks
This repo is based on https://github.com/vinodvr81/API_Testing_practise_using_pytest_and_unittest however the checks are failing because the JSON server is local one. Therefor here an outside website is added that checks to make sure all checks pass as part of the workflow


Important commands

pytest --cov-config=.coveragerc

pytest --cov=tests

pytest -m smoke

pytest --html=report.html

https://codecov.io/gh/vinodvr81/API_Testing_practise_using_pytest_added_workflow_that_checks/branch/main/graph/badge.svg
