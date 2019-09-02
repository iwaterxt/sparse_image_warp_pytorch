#!/bin/python


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from utils.sparse_image_warp import specaug
from utils.args_asr import parse
from tqdm import tqdm
from kaldiio import WriteHelper
from kaldiio import ReadHelper
import torch
import argparse

import os

def main():

    args = parse()

    spec_time_warp = args.spec_time_warp
    spec_freq_mask_width = args.spec_freq_mask_width
    spec_time_mask_width = args.spec_time_mask_width
    spec_num_freq_masks = args.spec_num_freq_masks
    spec_num_time_masks = args.spec_num_time_masks
    spec_time_mask_bound_ratio = args.spec_time_mask_bound_ratio
    spec_replace_with_zero = args.spec_replace_with_zero

    featdir = args.spec_feat_dir[0]
    featscp = os.path.join(featdir, 'feats.scp')
    with open(featscp) as f:
        lines = f.readlines()
        pbar = tqdm(total=len(lines))

    feats_dict = {}
    with ReadHelper('scp:'+featscp) as reader:
    	for key,mat in reader:
        	spec_feat = specaug(torch.from_numpy(mat), spec_time_warp, spec_freq_mask_width, spec_time_mask_width, \
        						spec_num_freq_masks, spec_num_time_masks, spec_time_mask_bound_ratio, spec_replace_with_zero)
        	feats_dict[key] = spec_feat.numpy()
        	pbar.update(1)

    with WriteHelper('ark,scp:'+featdir+'/feats_spec.ark,'+featdir+'/feats_spec.scp') as writer:
    	for key,mat in feats_dict.items():
        	writer(key, mat)

if __name__ == '__main__':
	main()
