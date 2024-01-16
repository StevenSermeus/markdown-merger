from utils.cli import get_args
from utils.merger import Merger

def main():
    args = get_args()
    merger = Merger(args.file_path, args.output)
    merger.merge()

if __name__ == '__main__':
    main()