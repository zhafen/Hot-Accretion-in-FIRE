def get_tchange_label( pm=None, central_indices=None ):

    if central_indices is None:
        central_indices = pm['central_indices']

    if central_indices == 'tcools_inds':
        tchange_label = (
            r'$t_{10^{' +
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
    'thin_disk_frac_tracked': r'$f_{\rm thin\,disk,\,tracked}$',
    'thin_disk_frac_sloanr': r'$f_{\rm thin\,disk}$($z=0$, Sloan r band)',
    'superthin_disk_frac': r'stellar thin disk fraction',
    'superthin_disk_frac_recent': r'$f_{\rm thin\,disk,\,recent}$',
    'superthin_disk_frac_tracked': r'$f_{\rm thin\,disk,\,tracked}$',
    'superthin_disk_frac_sloanr': r'$f_{\rm thin\,disk}$($z=0$, Sloan r band)',
    'thin_disk_frac_recent_orig': r'uncorrected $f_{\rm thin\,disk,\,recent}$',
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
    'smooth_disk_frac': r'aligned accretion',
    'delta_smooth_disk_frac': r'$\Delta$(aligned accretion fraction)',
    'smooth_jdisk_frac': r'spin-aligned accretion fraction',
    'delta_smooth_jdisk_frac': r'$\Delta$(spin-aligned accretion fraction)',
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
    'f_hot': 'hot accretion fraction',
    'f_valid': 'valid fraction',
    'n_hot': r'$n_{\rm hot}$',
    'n_tracked': r'$n_{\rm tracked}$',
    'n_valid': r'$n_{\rm valid}$',
    'delta_jperp': r'$j_\perp - j_{\perp,0}$' + '\n[kpc km/s]',
    'delta_jmag': r'$j - j_0$' + '\n[kpc km/s]',
    'delta_jperp_frac': r'$(j_\perp - j_{\perp,0})/j_{\rm DM}$',
    'delta_jz': r'$j_z - j_{z,0}$' + '\n[kpc km/s]',
    'delta_support': r'$\Delta \left( \vert j \vert / rv_c(r) \right)$',
    'torque_perp': r'$\vert \tau_\perp \vert$' + '\n[kpc km/s/Myr]',
    'torque_z': r'$\tau_z$' + '\n[kpc km/s/Myr]',
    'torque_mag': r'$\vert \vec \tau \vert$' + '\n[kpc km/s/Myr]',
    'torque_normalized': r'$\vert \vec \tau \vert / j_{\rm DM}$' + '\n[1/Myr]',
    'spin_param': r'$\lambda$',
    'f_j_disk': r'$J_{\rm thin\,disk\,stars}$ / $J_{\rm DM}$',
    'f_j_galaxy': r'$J_{\rm all\,stars}$ / $J_{\rm DM}$',
}

custom_lims = {
    'median_R1e5K_rgal': [ 0, 4 ],
    'mvir': [ 3e10, 2e12 ],
    'mstar': [ 7e7, 2e11 ],
    'tcool_tff': [ 0.08, 30 ],
    'delta_smooth_disk_frac': [ -0.1, 0.4 ],
    'delta_smooth_jdisk_frac': [ -0.1, 0.6 ],
    'delta_jmag': [ -4200, 500 ],
    'delta_jperp': [ -3100, 250 ],
    'delta_jmag_frac': [ -2, 0.2 ],
    'delta_jperp_frac': [ -2, 0.2 ],
    'torque_z': [ 0, 10 ],
    'torque_mag': [ 0, 50 ],
    'torque_perp': [ 0, 40 ],
    'torque_normalized': [ 0., 0.05 ],
    'n_hot': [ 100, 100000 ],
    'n_tracked': [ 100, 100000 ],
    'n_valid': [ 100, 100000 ],
}