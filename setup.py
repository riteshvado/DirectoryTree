from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Directory Tree'
LONG_DESCRIPTION = 'Allows you to filter directory files based on name , extension , path , size, permission etc. Also helps shows hierarchical view of the strcuture.'

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="DirectoryTree",
    version="1.1.0",
    author="Ritesh Vadodaria",
    author_email="riteshvado@gmail.com",
    description='Directory Tree',
    long_description='Allows you to filter directory files based on name , extension , path , size, permission etc. Also helps shows hierarchical view of the strcuture.',
    packages=find_packages(),
    install_requires=[], # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'
    keywords=['python', 'Directory Tree', 'File Search'],
    classifiers= [
        "Development Status :: Beta",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)