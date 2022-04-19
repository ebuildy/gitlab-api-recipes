import gitlab
import yaml

def get_pipeline_runner_tags(pipeline):
    tags = []
    
    if type(pipeline) is dict:
        for k,v in pipeline.items():
            if "tags" in v:
                tags += v["tags"]

    return list(set(tags))
        
def get_project_runner_tags(project):
    tags = []
    
    lookup_refs = ["main", "master", "develop"]
    
    for lookup_ref in lookup_refs:
        try:
            pipeline_raw = project.files.raw(file_path=".gitlab-ci.yml", ref=lookup_ref)
            
            pipeline_data = yaml.load(pipeline_raw, Loader=yaml.FullLoader)
            
            tags += get_pipeline_runner_tags(pipeline_data)
        except:
            pass
    
    return list(set(tags))