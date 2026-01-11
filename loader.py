
import yaml
#pip install PyYAML, the pyyaml libraryused to parse and work on yaml files
#there are 2 extensions for yaml files .yaml and .yml
#we will also be using file handling to read the yaml file

file_path = "E:\clang\test_cases.yaml"
def loader(file_path):
    with open(file_path,'r')as file:
        data = yaml.safe_load(file)
        return data

#so here we defined a function that opens the file test_cases.yaml in read mode, names it file and can be loaded as 
#key value pairs using yaml.full_load() method and returns the data

#pyyaml functions
#load()
#full_load()
#safe_load()
#load_all()