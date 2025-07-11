"""
make_tutorial_data1.py
"""
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../molass-library')))
from molass import get_version

assert get_version() >= '0.2.0', "Incompatible molass version"

from molass.Local import get_local_settings
from molass.Global.Options import set_molass_options
set_molass_options(flowchange='auto')
local_settings = get_local_settings()
DATA_ROOT_FOLDER = local_settings['DATA_ROOT_FOLDER']

# DATA1 = os.path.join(DATA_ROOT_FOLDER, "20220716", "OA_ALD_201")
DATA1 = os.path.join(DATA_ROOT_FOLDER, "20230706", "ALD_OA002")

import matplotlib.pyplot as plt
from molass.DataObjects import SecSaxsData as SSD
ssd = SSD(DATA1)
result = ssd.plot_compact(moment_lines=True)
plt.show()

moment = result.moment
mean, std = moment.get_meanstd()
xr_jrange = mean - 1.5*std, mean + 1.5*std
mapping = result.mapping
uv_jrange = mapping.get_mapped_x(xr_jrange)
trimmed_ssd = ssd.trimmed_copy(jranges=(xr_jrange, uv_jrange), mapping=mapping)
trimmed_ssd.plot_compact(moment_lines=True)
plt.show()

trimmed_ssd.export('SAMPLE1', 'PREFIX1_', fmt='%.8e')

check_ssd = SSD('SAMPLE1')
check_ssd.plot_compact(moment_lines=True)
plt.show()
