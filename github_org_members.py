# python 3 headers, required if submitting to Ansible
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.errors import AnsibleError
from ansible.plugins.lookup import LookupBase

from github import Github

try:
    from __main__ import display
except ImportError:
    from ansible.utils.display import Display
    display = Display()


class LookupModule(LookupBase):
    def run(self, terms, variables=None, **kwargs):
        api_key = kwargs.get('api_key', True)
        github_org = kwargs.get('github_org', True)
        g = Github(api_key)

        ret = []
        for member in g.get_organization(github_org).get_members():
            ret.append(member.login)
        return ret
