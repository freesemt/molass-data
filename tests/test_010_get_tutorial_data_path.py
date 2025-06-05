import sys
sys.path.insert(0, '../../molass-library')
sys.path.insert(0, '..')
from molass_data import get_version, get_data_path
print("Library version:", get_version())
print("Tutorial data path:", get_data_path("tutorial_data"))