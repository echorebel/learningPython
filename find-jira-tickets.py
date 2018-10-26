#!/usr/bin/env python

# also here: https://gist.github.com/echorebel/9be0f22e4eac36d30467873528f75626
# finds jira tickets up until latest tag
# regex part inspired by https://github.com/pbetkier/add-issue-id-hook

import subprocess
import re

project_format = '[A-Z][A-Z]+'
issue_pattern = '{}-[\d]+'.format(project_format)
issues = []

try:
    result = subprocess.check_output('git log $(git describe --abbrev=0 --tag)..HEAD --oneline --decorate', shell=True)
    for line in result.splitlines():
        issue_id_match = re.search(issue_pattern, line)
        if issue_id_match:
            found_issue_id = issue_id_match.group()
            issues.append(found_issue_id)
    issues = list(set(issues))
    print(issues)
except subprocess.CalledProcessError as e:
    print "Calledprocerr"
