import glob
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

os.chdir( pm['data_dir'] )

# Tar
subprocess.run([
    'tar',
    '-cvf',
    tar,
    *glob.glob( '*' ),
])

# Archive
subprocess.run([
    'rsync',
    tar,
    archive_dir,
    '--progress',
])
