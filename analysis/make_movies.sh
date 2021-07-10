variations=(
    m12i
    m11a
    m11c
    m12i_md
    m12r_md
    m12w_md
    m12f_md
    m12c_md
    m12b_md
    m11d_md
    m11e_md
    m11h_md
    m11i_md
    m11q_md
    m12i_cr
)
base_dir=/Users/zhafen/Data/hot_halo_accretion/movies

copy=True
make_movie=True

# Copy
if $copy; then
    for var in ${variations[*]}; do
        local_dir=${base_dir}/frames/${var}
        mkdir $local_dir
        remote_dir=/scratch/03057/zhafen/hot_accretion_data/${var}/projected_frames
        rsync -r --progress -u zhafen@stampede2.tacc.utexas.edu:$remote_dir $local_dir
    done
fi

# Make Movie
if $make_movie; then
    for var in ${variations[*]}; do
        frames_dir=${base_dir}/frames/${var}/projected_frames
        ffmpeg -r 30 -f image2 -s 1080x1080 -i ${frames_dir}/${var}_%03d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p ${base_dir}/${var}.mp4
        ffmpeg -r 10 -f image2 -s 1080x1080 -i ${frames_dir}/${var}_focused_%03d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p ${base_dir}/${var}_focused.mp4
    done
fi
