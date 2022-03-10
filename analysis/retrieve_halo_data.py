import os
import shutil
import subprocess
import sys

import trove
pm = trove.link_params_to_config(
    config_fp = sys.argv[1],
)

archive_dir = 'ranch.tacc.utexas.edu:' + os.path.join(
    'halo_files',
    pm['subpath']
)
os.makedirs( pm['data_dir'], exist_ok=True )
os.makedirs( pm['halo_data_dir'], exist_ok=True )

halo_file_tars = [
    'mt_halo_files.tar',
    'AHF_halos.tar',
    'AHF_profiles.tar'
]
for tar in halo_file_tars:

    archive_fp = archive_dir + '/' + tar

    # Unarchive
    subprocess.run([
        'rsync',
        archive_fp,
        pm['halo_data_dir'],
        '--progress',
    ])

    # Untar
    subprocess.run([
        'tar',
        '-xvf',
        os.path.join( pm['halo_data_dir'], tar ),
        '-C',
        pm['halo_data_dir'],
    ])

# Copy the main halo file for safekeeping and cataloging progress
shutil.copy(
    os.path.join( pm['halo_data_dir'], 'halo_00000_smooth.dat' ),
    pm['data_dir'],
)
