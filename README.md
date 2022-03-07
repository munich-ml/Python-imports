# Python imports
## The common problem 
```Python
from my_package.my_module import my_class
```
raises `ModuleNotFoundError: No module named 'my_package'` if the `project_path` is not in the `PYTHONPATH`, with 
- `project_path`, being the folder where the package is located in
- `PYTHONPATH` can be listed with `sys.path`


## Definitions
A __module__ is a single Python file. For example `Containers.py` is a module with the name `container`. 

A __package__ is a collection (a directory) of Python modules. There are two types of packages:
- __regular packages__ must contain a ``__init__.py`` file
- __namespace packages__ (only for very special use cases) don't require a ``__init__.py`` file

## Useful articles about Python imports
- [Python Modules and Packages – An Introduction](https://realpython.com/python-modules-packages/)

- [How to Fix ModuleNotFoundError and ImportError](https://towardsdatascience.com/how-to-fix-modulenotfounderror-and-importerror-248ce5b69b1c)

- Why isn't VSCode adding the `project_path` automatically? [PYTHONPATH in VSCode – everything you need to know](https://linuxpip.org/vscode-pythonpath/) 

# Case study
Different import methods are beeing tried out within this very simple case study: A function `func` is defined in `module.py`. It sould be imported into `test_module.py` for the purpose of testing.

```Python
# module.py
def func():
    return 42
```
```Python
# test_module.py
def test_func():
    assert func() == 42  # func need to be imported from module.py
```

## Project1 top-down import
The `test_module1.py` is located above the `module1.py`. Thus there is no issue when doing the import:
```Python
from package1.module1 import func1
```
```
C:\Users\s00110656\Desktop\python\Python_Import\project1_top_down>pytest                    --> works
C:\Users\s00110656\Desktop\python\Python_Import\project1_top_down>python test_module1.py    --> works
```
--> all good!

## Project2 import the module
The `test_module2.py` is located beside the `module2.py`. There is no issue when doing the import:
```Python
from module2 import func2
```
```
C:\Users\s00110656\Desktop\python\Python_Import\project2_import_module>python package2\test_module2.py  --> works
C:\Users\s00110656\Desktop\python\Python_Import\project2_import_module>pytest                           --> works
```
--> all good!

## Project3 absolute import
The `test_module3.py` is located anywhere outside of the `package3`. The import looks like this:
```Python
from package3.module3 import func3
```
Even in this case `pytest` manages to locate `package3.module3` and runs. I don't know how!  :|
```
C:\Users\s00110656\Desktop\python\Python_Import\project3_absolute>pytest                --> works
```

However, executing as a script fails: 
```
C:\Users\s00110656\Desktop\python\Python_Import\project3_absolute>python tests\test_module3.py   --> ModuleNotFoundError
```
In order to solve this, we have to unserstand the Python's `import` search path...
# Import search path
When executing an import statement, and the resource is not within the __current directory__, it's path needs to be within the __`PYTHONPATH`__. that can be checked by
```Python
sys.path
```
If the resources path is not there, Phython can import it, resulting in an `ModuleNotFoundError` or `ImportError`. There are three ways to solve this

## 1. Set PYTHONPATH in environment variables
Setting the `PYTHONPATH` within the global __environment varibales__ requires admin rights, but one can also add one in the __user environment variables__: [How to set Path in Windows without admin rights](
https://kscodes.com/misc/how-to-set-path-in-windows-without-admin-rights/)

## 2. Add a `file.pth` to `site-packages` 
Add a `file.pth` with the absolute path to the projects root dir to the `site-packages` directory of the conda environment, like this:
```
# conda.pth  (ANY_NAME.pth)
# located in C:\ProgramData\Anaconda3\envs\ENV_NAME\Lib\site-packages
C:\Users\s00110656\Desktop\python\Python_Import\project3_absolute
```
The same can be accomplished by using this conda command:
```
conda develop PATH_TO_PROJECT_DIR
```
## 3. `sys.path.append()` at runtime 
The `PYTHONPATH` can be modified at runtime. 

Using this approach gets a little messy, because the `sys.path.append()` has to happen before the actual import:
```Python
import sys
sys.path.append("PATH_TO_CUSTOM_PACKAGE")   
import custom_package
```


