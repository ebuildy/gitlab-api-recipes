import os
import sys
import logging

from progress.bar import Bar
from pytablewriter import MarkdownTableWriter

from ..helpers.gitlab_api_client import build_gitlab_api_client

def pepe_commands_projects_gitops():
    gl = build_gitlab_api_client()
    
    keywords = ["argo", "argocd", "gitops", "git-ops", "cd", "k8s", "deploy"]
    
    gitops_projects = {}
    
    for keyword in keywords:
        projects = gl.projects.list(all=True, archived=False, simple=True, search=keyword)
    
        for p in projects:
            gitops_projects[p.id] = p
    
    logging.debug(f"Found {len(gitops_projects)} projects!")
    
    out_list = []
    
    for project_id, project in gitops_projects.items():
        members = project.members_all.list(all=True)
        
        members = list(map(lambda m : m.name, members))
        
        out_list.append([project.web_url, members])
        
    writer = MarkdownTableWriter(
        headers = ["project URL", "members"],
        value_matrix = out_list
    )
    
    writer.write_table()