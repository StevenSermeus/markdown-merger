from utils.file_manipulation import create_file, ensure_file_exists
from logging import getLogger
logger = getLogger(__name__)

class Merger:
    def __init__(self, file_input, file_output):
        self.file_input = file_input
        self.file_output = file_output
        create_file(file_output)
        ensure_file_exists(file_input)


    def find_merge_token(self, line):
        if line.find('![$include-md]') != -1:
            start = line.find('(')
            end = line.find(')')
            logger.debug('File to merge: {}'.format(line[start + 1:end]))
            return line[start + 1:end]
        else:
            return None
    
    def merge(self):
        file_input_dir = self.file_input.replace(self.file_input.split('/')[-1], '')
        with open(self.file_output, 'w') as f_out:
            with open(self.file_input, 'r') as f:
                for line in f:
                    merge_file = self.find_merge_token(line)
                    if merge_file:
                        if merge_file[0] == '.':
                            merge_file = file_input_dir + merge_file[1:]
                        ensure_file_exists(merge_file)
                        with open(merge_file, 'r') as f_merge:
                            for merge_line in f_merge:
                                f_out.write(merge_line)
                    else:
                        f_out.write(line)
    

                        
                    