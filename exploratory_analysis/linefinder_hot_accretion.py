import os

import linefinder.linefinder as linefinder

########################################################################

sim_name = 'm12i_cr'

pm = {
    # Identifying tag used as part of the filenames.
    # E.g. the IDs file will have the format `ids_{}.hdf5.format( tag )`.
    'tag': '{}_hothaloacc'.format( sim_name ),

    'sim_name': sim_name,
    
    # Location to place output in
    'out_dir': '$SCRATCH/linefinder_data/cr_heating_fix/m12i_res7100/data',

    # Location of simulation data
    'sim_data_dir': '/scratch/projects/xsede/GalaxiesOnFIRE/cr_heating_fix/m12i_res7100/output',

    # Location of halo file data
    'halo_data_dir': '/scratch/03057/zhafen/halo_files/cr_heating_fix/m12i_res7100',

    # Arguments for id sampling
    'sampler_kwargs': {
        'ignore_duplicates': True,
        'p_types': [0, 4],
        'snapshot_kwargs': {
            'ahf_index': 600,
            'length_scale_used': 'R_vir',
        },
    },

    # Arguments used for the particle tracking step
    'tracker_kwargs': {
        # What particle types to track. Typically just stars and gas.
        'p_types': [ 0, 4,],

        # What snapshots to compile the particle tracks for.
        'snum_start': 1,
        'snum_end': 600,
        'snum_step': 1,
    },

    # Arguments used for the visualization step
    'visualization_kwargs': {
        'install_firefly': False,
        'include_instantaneous': False,
        # These kwargs are used for tuning the Firefly visualization
        'export_to_firefly_kwargs': {
            'firefly_dir': '/scratch/03057/zhafen/firefly_repos/FireflyTest',
            'classifications': [
                None,
            ],
            'classification_ui_labels': [
                'All',
            ],
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
            # 'preset_filepath': '/scratch/03057/zhafen/firefly_repos/hot-halo-accretion/data/preset.json',
        },
    },

    # IDs are selected independently
    'run_id_selecting': False,
    'run_id_sampling': True,
    'run_tracking': True,
    'run_galaxy_linking': True,
    'run_classifying': True,
    'run_visualization': True,
}

import trove
import sys
pm, pm_new = trove.link_params_to_config(
    sys.argv[1],
    split_existing_and_new = True,
    **pm
)

# Individual updates
pm['sim_name'] = pm_new['variation']
pm['out_dir'] = pm_new['data_dir']
pm['tag'] = '{}_hothaloacc'.format( pm_new['variation'] )

# THIS DOESN'T WORK!
# Jug uses the passed parameters as IDs. Changing the passed parameters
# changes the ids, so it will try to run something different.
# # Update which parts still need to be run
# # This could probably be moved inside run_linefinder.
# run_kwargs = [
#     'run_id_sampling',
#     'run_tracking',
#     'run_galaxy_linking',
#     'run_classifying',
# ]
# filenames = [
#     'ids_{}.hdf5',
#     'ptracks_{}.hdf5',
#     'galids_{}.hdf5',
#     'classifications_{}.hdf5',
# ]
# for i, run_kwarg in enumerate( run_kwargs ):
#     filename = filenames[i].format( pm['tag'] )
#     fp = os.path.join(
#         pm_new['data_dir'],
#         filename
#     )
#     pm[run_kwarg] = not os.path.exists( fp )
#     if pm[run_kwarg]:
#         print( '{} complete, skipping!'.format( filename ) )

# Actually run Linefinder
linefinder.run_linefinder_jug(
    **pm
)
