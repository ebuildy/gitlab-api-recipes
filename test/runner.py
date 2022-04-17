import yaml
import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], "../helpers"))

from gitlab_pipelines import get_pipeline_runner_tags

def test_runner():
    with open("./no.yaml") as pipeline_content:
        pipeline_data = yaml.load(pipeline_content, Loader=yaml.FullLoader)
        
        tags = get_pipeline_runner_tags(pipeline_data)
        
        assert len(tags) == 0
        
    with open("./wrong.yaml") as pipeline_content:
        pipeline_data = yaml.load(pipeline_content, Loader=yaml.FullLoader)
        
        tags = get_pipeline_runner_tags(pipeline_data)
        
        assert len(tags) == 0
        
    with open("./pipeline1.yaml") as pipeline_content:
        pipeline_data = yaml.load(pipeline_content, Loader=yaml.FullLoader)
        
        tags = get_pipeline_runner_tags(pipeline_data)
        
        assert "k8s" in tags