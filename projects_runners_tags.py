import gitlab
import os
import sys
from prettytable import PrettyTable
from progress.bar import Bar

sys.path.insert(1, os.path.join(sys.path[0], "./helpers"))

from gitlab_pipelines import get_project_runner_tags

gl = gitlab.Gitlab(os.environ["GITLAB_URL"], private_token=os.environ["GITLAB_TOKEN"])

if __name__ == '__main__':
    projects = gl.projects.list(all=True, archived=False, simple=True)
    
    t = PrettyTable(['Project URL', 'Runner tags'])
    t.align = "l"
    
    bar = Bar('Processing', max=len(projects))
    
    for project in projects:      
        runner_tags = get_project_runner_tags(project)
        t.add_row([project.web_url, runner_tags])
        bar.next()
    
    bar.finish()
        
    print(t)