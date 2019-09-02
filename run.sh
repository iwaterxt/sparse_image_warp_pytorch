#!/bin/bash

#begin config
nj=1
time_warp=80
freq_mask_width=27
time_mask_width=70
num_freq_masks=2
num_time_masks=2
time_mask_bound_ratio=0.2
replace_with_zero=False
#end config

. utils/parse_options.sh
. ./path.sh

if [ $# != 1 ]; then
   echo "Usage: $0 <data> "
   echo " e.g.: $0 data/train"
   echo "main options (for others, see top of script file)"
   echo "  --time-warp <int>  #time warp parameter"
   echo "  --freq_mask_width <int >     # frequence mask parameter"
   echo "  --time_mask_width <int> # time mask parameter"
   echo "  --num_freq_masks <int> # number of frequence masks"
   echo "  --num_time_masks  <int>  # number of time masks"
   echo "  --time_mask_bound_ratio <float>  # the up bound of time mask width"
   echo "  --replace_with_zero <bool> # replace the mask region with zero or spec mean"
   exit 1;
fi

set -e
set -u
set -o pipefail

data=$1

mkdir -p ${data}/splits${nj}
split_feats_scps=""
for n in $(seq $nj); do
    mkdir -p ${data}/splits${nj}/${n}
    split_feats_scps="$split_feats_scps ${data}/splits${nj}/${n}/feats.scp"
done
utils/split_scp.pl ${data}/feats.scp $split_feats_scps || exit 1;

rm -i ${data}/feats_spec.scp

for n in $(seq $nj); do
{
   {
	 python spec_augment.py  \
		--spec_feat_dir ${data}/splits${nj}/${n} \
		--spec_time_warp ${time_warp} \
		--spec_freq_mask_width ${freq_mask_width} \
		--spec_time_mask_width ${time_mask_width} \
		--spec_num_freq_masks ${num_freq_masks} \
		--spec_num_time_masks ${num_time_masks} \
		--spec_time_mask_bound_ratio ${time_mask_bound_ratio} \
		--spec_replace_with_zero ${replace_with_zero} \
		|| exit 1;

   cat ${data}/splits${nj}/${n}/feats_spec.scp >> ${data}/feats_spec.scp
	}&
}
done
wait