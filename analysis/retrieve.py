import os
import shutil
import subprocess
import sys

import trove
pm = trove.link_params_to_config(
    config_fp = sys.argv[1]
)

archive_dir = 'ranch.tacc.utexas.edu:hot_accretion_data'
os.makedirs( pm['data_dir'], exist_ok=True )

tar = '{}.tar'.format( pm['variation'] )

# Unarchive
subprocess.run([
    'rsync',
    os.path.join( archive_dir, tar ),
    pm['data_dir'],
    '--progress',
])

# Untar
subprocess.run([
    'tar',
    '-xvf',
    os.path.join( pm['data_dir'], tar ),
    '-C',
    pm['data_dir'],
])
