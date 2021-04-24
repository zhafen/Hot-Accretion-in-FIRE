#!/bin/bash
########################################################################
# Input Arguments
########################################################################

# What simulation to use, and where to put the output
HALO_DATA_DIR=$1
ARCHIVE_TAR=${ARCHIVER}:halo_files/$2/mt_halo_files.tar

########################################################################
# Start Data Processing
########################################################################

# Stop on errors
set -e

rsync --progress $ARCHIVE_TAR $HALO_DATA_DIR

tar -xvf $HALO_DATA_DIR/mt_halo_files.tar -C $HALO_DATA_DIR

