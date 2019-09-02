#!/bin/python


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from utils.sparse_image_warp import specaug
from utils.args_asr import parse

import torch
import argparse
import kaldi_io

def main():

    args = parse()

    spec_time_warp = args.spec_time_warp
	spec_freq_mask_width = args.spec_freq_mask_width
	spec_time_mask_width = args.spec_time_mask_width
	spec_num_freq_masks = args.spec_num_freq_masks
	spec_num_time_masks = args.spec_num_time_masks
	spec_time_mask_bound_ratio = args.spec_time_mask_bound_ratio
	spec_replace_with_zero = args.spec_replace_with_zero

    featdir = args.spec_feat_dir
    featscp = os.path.join(featdir, 'feats.scp')

    ark_scp_output='ark:| copy-feats --compress=true ark:- ark,scp:${featdir}/feats.ark,${featdir}/feats.scp'
	with kaldi_io.open_or_fd(ark_scp_output, 'wb') as w:
		for key,mat in kaldi_io.read_mat_scp(featscp):
			spec_feat = specaug(mat, spec_time_warp, spec_freq_mask_width, spec_time_mask_width, \
    							  	  spec_num_freq_masks, spec_num_time_masks, \
    							  	  spec_time_mask_bound_ratio, spec_replace_with_zero)
			
			kaldi_io.write_mat(w, spec_feat, key=key)

if __name__ == '__main__':
    main()