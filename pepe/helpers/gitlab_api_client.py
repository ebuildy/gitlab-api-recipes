import gitlab
import os

def build_gitlab_api_client():
    return gitlab.Gitlab(os.environ["GITLAB_URL"], private_token=os.environ["GITLAB_TOKEN"])
