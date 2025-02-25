from setuptools import find_packages,setup
from typing import list

hypen_e_dot='-e.'
def get_requirements(file_path:str)->List[str]:
    '''
    Requiremnts list will be returned
    '''
    requirements=[]
    with open(file_path)as file_obj:
        requirements=file.obj.readlines()
        requiremnts=[req.replace('\n',"")for req in requirements]
    if hypen_e_dot in requirements:
        requirements.remove(hypen_e_dot)
    return requirements

setup(
name ='mlproject',
version='0.1',
author='Shivam',
author_email='shivamsinha00101@gmail.com',
packages=find_packages(),
install_requires=['pandas','numpy','seaborn','matplotlib','scikit-learn','joblib'],

)