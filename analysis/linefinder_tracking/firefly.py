'''Perform visualization.'''

import sys

import linefinder.visualize as visualize

import trove

########################################################################

pm = trove.link_params_to_config(
    config_fp = sys.argv[1],
)

export_to_firefly_kwargs = {
    'firefly_dir': pm['firefly_dir'],
    'classifications': [ None, ],
    'classification_ui_labels': [ 'Tracks', ],
    'tracked_properties': [
        'logT',
        'logZ',
        'logDen',
        'PType',
        't_t_1e5',
        'Vr',
    ],
    'use_default_colors': True,
    'include_halo_tracks': True,
}

visualize.export_to_firefly(
    out_dir = pm['data_dir'],
    tag = pm['tag'],
    halo_data_dir = pm['halo_data_dir'],
    install_firefly = False,
    include_instantaneous = False,
    export_to_firefly_kwargs = export_to_firefly_kwargs,
)
