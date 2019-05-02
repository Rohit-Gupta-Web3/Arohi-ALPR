#!/usr/bin/env python3
from __future__ import absolute_import, division, print_function

import argparse
import json
import time
from glob import glob
from collections import OrderedDict
import requests


def parse_arguments():
    parser = argparse.ArgumentParser(
        description=
        'Read license plates from images and output the result as JSON.',
        epilog=
        'For example: python plate_recognition.py --api MY_API_KEY "/path/to/vehicle-*.jpg"'
    )
    parser.add_argument('--api', help='Your API key.', default="d821ed8a941715c65f9755bffb7c7ecb6e3a6616")
    parser.add_argument('FILE', help='Path to vehicle image or pattern.')
    return parser.parse_args()


def main():
    args = parse_arguments()
    result = []
    paths = glob(args.FILE)
    if len(paths) == 0:
        print('File {} does not exist.'.format(args.FILE))
        return
    for path in paths:
        with open(path, 'rb') as fp:
            response = requests.post(
                'https://api.platerecognizer.com/v1/plate-reader/',
                files=dict(upload=fp),
                headers={'Authorization': 'Token ' + args.api})
            result.append(response.json(object_pairs_hook=OrderedDict))
        time.sleep(1)
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
