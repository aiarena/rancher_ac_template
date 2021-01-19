### Prerequisites 
- `pip install -r requirements.txt`
- [kustomize](https://kubectl.docs.kubernetes.io/references/kustomize) Installed and in path
- [kubectl](https://kubectl.docs.kubernetes.io/installation/kubectl) Installed and in path
- A valid config.py file placed in `deployment/overlay/production/configs` (containing the relevant secrets that will over write the blank default values)


### Automated Generation

- `python -m generate` will generate the yaml files (with unique identifiers for easier version control ) and also a bulk.yaml  


Those files will then be placed in the relevant components in rancher ( This is still a manual process),  
TODO   explain  this process 
