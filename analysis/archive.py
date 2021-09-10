import os
import shutil
import subprocess
import sys

import trove
pm = trove.link_params_to_config(
    config_fp = sys.argv[1]
)

archive_dir = 'ranch.tacc.utexas.edu:hot_accretion_data'

tar = '{}.tar'.format( pm['variation'] )

# Tar
subprocess.run([
    'tar',
    '-cvf',
    os.path.join( pm['data_dir'], tar ),
    archive_dir,
])

# Archive
subprocess.run([
    'rsync',
    os.path.join( pm['data_dir'], tar ),
    archive_dir,
    '--progress',
])
