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

DATA2 = os.path.join(DATA_ROOT_FOLDER, "20211222", "PKS")

import matplotlib.pyplot as plt
from molass.DataObjects import SecSaxsData as SSD
ssd = SSD(DATA2)
ssd.plot_compact()
plt.show()

trim = ssd.get_trimming_info()
print(trim)

manual_trim = trim.copy(xr_slices=(slice(None, None), slice(200, 1200)),
                        uv_slices=(slice(None, None), slice(200, 1200)))
trimmed_ssd = ssd.trimmed_copy(trim=manual_trim, trimmed=False)
trimmed_ssd.plot_compact()
plt.show()

trimmed_ssd.export('SAMPLE2', 'PREFIX2_', fmt='%.8e')

check_ssd = SSD('SAMPLE2')
check_ssd.plot_compact()
plt.show()
