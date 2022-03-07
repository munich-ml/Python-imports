"""
# Adding project_path to the PYTHONPATH this way is discouraged
import os, sys
sys.path.append(os.path.dirname(os.getcwd()))
print(sys.path)
"""

from package3.module3 import func3

def test_func3():
    assert func3() == 42