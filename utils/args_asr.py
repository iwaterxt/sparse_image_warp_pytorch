#! /usr/bin/env python
# -*- coding: utf-8 -*-


"""Args option for the ASR task."""

import configargparse
from distutils.util import strtobool


def parse():
    parser = configargparse.ArgumentParser(
        config_file_parser_class=configargparse.YAMLConfigFileParser,
        formatter_class=configargparse.ArgumentDefaultsHelpFormatter)

    #specaugment parameters

    parser.add_argument('--spec_feat_dir', type=str, default=[], nargs='+',
                        help='dir name for raw features')
    parser.add_argument('--spec_time_warp', type=int, default=80,
                        help='time warp parameter W')
    parser.add_argument('--spec_freq_mask_width', type=int, default=27,
                        help='frequence mask width')
    parser.add_argument('--spec_time_mask_width', type=int, default=70,
                        help='time mask width')
    parser.add_argument('--spec_num_freq_masks', type=int, default=2,
                        help='number of frequence masks')
    parser.add_argument('--spec_num_time_masks', type=int, default=2,
                        help='number of time masks')
    parser.add_argument('--spec_time_mask_bound_ratio', type=float, default=0.2,
                        help='an upper bound on the time mask so that a time mask cannot \
                        be wider than p times the number of time steps')
    
    args = parser.parse_args()
    return args
