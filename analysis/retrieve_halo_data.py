import os
import subprocess
import sys

import trove
pm = trove.link_params_to_config(
    config_fp = sys.argv[1]
)

os.makedirs( pm['data_dir'], exist_ok=True )

subprocess.run([
    os.path.join( pm['code_dir'], 'retrieve_halo_data.sh' ),
    pm['halo_data_dir'],
    pm['subpath']
])
