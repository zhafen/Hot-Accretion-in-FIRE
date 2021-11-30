def get_tchange_label( pm=None, central_indices=None ):

    if central_indices is None:
        central_indices = pm['central_indices']

    if central_indices == 'tcools_inds':
        tchange_label = (
            r'$t_{T=10^{' +
            str( pm['logTcools'] ) +
            r'}{\rm K}}$'
        )
    elif central_indices == 'tacc_inds':
        tchange_label = r'$t_{\rm acc}$'
    else:
        tchange_label = r'$t_{\rm change}$' 

    return tchange_label

def get_tchange_name( pm ):

    if pm['central_indices'] == 'tcools_inds':
        tchange_name = 'cooling'
    elif pm['central_indices'] == 'tacc_inds':
        tchange_name = 'accretion'
    else:
        tchange_name = pm['central_indices']

    return tchange_name

def get_t_tchange_label( pm ):

    t_tchange_label = (
        r'time relative to ' + 
        get_tchange_name( pm ) + 
        r', $t - ' +
        get_tchange_label( pm )[1:] + 
        r' [Myr]'
    )
        

    return t_tchange_label

quantity_labels = {
    'delta_thin_disk': r'$\Delta f_{\rm thin}$',
    'median_R1e5K': r'median $R_{T=10^5\, {\rm K}}$ (kpc)',
    'median_R1e5K_rgal': r'median $R_{T=10^5\, {\rm K}}$ / $R_{\rm gal}$',
    'thin_disk_frac': r'stellar thin disk fraction',
    'thin_disk_frac_recent': r'$f_{\rm thin\,disk,\,recent}$',
    'thin_disk_frac_tracked': r'$f_{\rm thin}(\star,z=0,$ tracked)',
    'thin_disk_frac_sloanr': r'$f_{\rm thin\,disk}$($z=0$, Sloan r band)',
    'mvir': r'$M_{\rm vir}$ $[M_\odot]$',
    'mstar': r'$M_{\star}$ $[M_\odot]$',
    'rstar': r'$R_{\star, 0.5}$ [kpc]',
    'tcool_tff': r'$t_{\rm cool}^{(s)}$ / $t_{\rm ff}$ at $0.1 R_{\rm vir}$', 
    'sigma_cosphi': r'$\sigma( \cos\theta )$',
    'negative_delta_sigma_cosphi': r'$\sigma_{\cos\theta,\,{\rm hot}}$ - $\sigma_{\cos\theta,\,{\rm cool}}$',
    'sigma_cosphi_ratio': r'$\sigma_{\cos\theta,\,{\rm hot}}$ / $\sigma_{\cos\theta,\,{\rm cool}}$',
    'std_cosphi_ratio': r'${\rm STD}_{\cos\theta,\,{\rm hot}}$ / ${\rm STD}_{\cos\theta,\,{\rm cool}}$',
    'delta_pdfcosphi': r'$( dM_{\rm after\,cooling} - dM_{\rm before\,cooling} )\mid_{\rm galaxy\,plane}$',
    'ratio_pdfcosphi': r'${\rm PDF}(\cos\theta=0)_{\rm cool}$ / ${\rm PDF}(\cos\theta=0)_{\rm hot}$',
    'pdfcosphi_0': r'${\rm PDF}(\cos\theta=0)$',
    'disk_frac': r'aligned accretion, $f_{\rm aligned}$',
    'delta_disk_frac': r'$\Delta$(aligned accretion), $\Delta f_{\rm aligned}$',
    'jdisk_frac': r'aligned accretion, $f_{\rm aligned,\,j}$',
    'delta_jdisk_frac': r'$\Delta$(aligned accretion), $\Delta f_{\rm aligned,\,j}$',
    'smooth_disk_frac': r'spatial aligned accretion',
    'delta_smooth_disk_frac': r'$\Delta$(spatial aligned accretion fraction)',
    'smooth_jdisk_frac': r'spin aligned accretion fraction',
    'delta_smooth_jdisk_frac': r'$\Delta$(spin aligned accretion fraction)',
    'min_delta_disk_frac': r'$\Delta$(aligned accretion), $\Delta f_{\rm aligned,\,min}$',
    'disk_frac_pdf': r'aligned accretion under curve, $f_{\rm aligned}$',
    'delta_disk_frac_pdf': r'$\Delta$(aligned accretion under curve), $\Delta f_{\rm aligned}$',
    'disk_frac_pdf_all': r'aligned accretion under all curve, $f_{\rm aligned}$',
    'delta_disk_frac_pdf_all': r'$\Delta$(aligned accretion under all curve), $\Delta f_{\rm aligned}$',
    'disk_frac_pdf_disk': r'aligned accretion under disk curve, $f_{\rm aligned}$',
    'delta_disk_frac_pdf_disk': r'$\Delta$(aligned accretion under disk curve), $\Delta f_{\rm aligned}$',
    'delta_q20': r'$\Delta q_{20}$',
    'delta_q33': r'$\Delta q_{33}$',
    'med_cosphi': r'$\cos\theta_{50}$',
    'delta_med_cosphi': r'$\Delta \cos\theta_{50}$',
    'abs_med_cosphi': r'$\mid \cos\theta_{50}\mid$',
    'delta_abs_med_cosphi': r'$\mid \Delta \cos\theta_{50}\mid$',
    'quiet_frac': r'CCF fraction, no R cut',
    'quiet_frac_strict': r'CCF fraction',
}