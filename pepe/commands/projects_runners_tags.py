import os
import sys

from progress.bar import Bar
from pytablewriter import MarkdownTableWriter

from ..helpers.gitlab_pipelines import get_project_runner_tags
from ..helpers.gitlab_api_client import build_gitlab_api_client

def pepe_commands_projects_runners():
    gl = build_gitlab_api_client()
    
    projects = gl.projects.list(all=False, archived=False, simple=True)
    
    #io_table = pepe_io_get_table(['Project URL', 'Runner tags'])
    
    bar = Bar('Processing', max=len(projects))
    
    out_list = []
    
    for project in projects:      
        runner_tags = get_project_runner_tags(project)
        
        if len(runner_tags) > 0:
            out_list.append([project.web_url, runner_tags])
        
        bar.next()
    
    bar.finish()
    
    writer = MarkdownTableWriter(
        headers = ["project URL", "runners tags"],
        value_matrix = out_list
    )
    
    writer.write_table()