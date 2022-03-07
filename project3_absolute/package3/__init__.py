"""
from pathlib import Path
import sys

# Add the project_path to the PYTHONPATH
#   The parent of this __init__.py is assumed to be a package.py.
#   The parent of the package.py is assumed to be the project, which path has to be
#   added to the `PYTHONPATH` in order for the absolute imports to work
project_path = Path(__file__).parent.parent
print(f"Appending {project_path} to the PYTHONPATH")
sys.path.append(str(project_path))
"""
