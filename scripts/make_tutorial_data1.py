"""
make_tutorial_data1.py
"""
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../molass-library')))
from molass import get_version

assert get_version() >= '0.0.17', "Incompatible molass version"

from molass.Local import get_local_settings
from molass.Global.Options import set_molass_options
set_molass_options(flowchange='auto')
local_settings = get_local_settings()
DATA_ROOT_FOLDER = local_settings['DATA_ROOT_FOLDER']

DATA1 = os.path.join(DATA_ROOT_FOLDER, "sample_data")

import matplotlib.pyplot as plt
from molass.DataObjects import SecSaxsData as SSD
ssd = SSD(DATA1)
ssd.plot_compact()
plt.show()

trimmed_ssd = ssd.trimmed_copy()
trimmed_ssd.plot_compact()
plt.show()

trimmed_ssd.export('SAMPLE1', 'PREFIX1_', fmt='%.8e')

check_ssd = SSD('SAMPLE1')
check_ssd.plot_compact()
plt.show()
