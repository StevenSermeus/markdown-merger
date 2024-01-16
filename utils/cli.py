import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file-path', type=str, default='index.md')
    parser.add_argument('--output', type=str, default='output/out.md')

    args = parser.parse_args()
    return args