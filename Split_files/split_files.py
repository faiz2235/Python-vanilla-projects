'''
    This accepts split index and file name than spilts it according to the index
    provided.
    ### Prerequisites
    To execute this script python must be installed the host system.
    ### How to run the script
    just type this in the terminal:-
    `python split_files.py <csv/text_file> <split/line_number>`
'''
import os
import sys
import pandas as pd
import shutil


class Split_files:
    '''
        class files for split program
    '''
    def __init__(self, filename, split_number):
        '''
            Getting the file name and split index
            Initialzing the output directory, if present then truncate it.
            Getting the extention
        '''
        self.file_name = filename
        self.directory = "file_split"
        self.split = int(split_number)
        if os.path.exists(self.directory):
            shutil.rmtree(self.directory)
        os.mkdir(self.directory)
        if self.file_name.endswith('.txt'):
            self.file_extension = '.txt'
        else:
            self.file_extension = '.csv'
        self.file_number = 1


    def split_data(self):
        '''
            splitting th input csv/txt file according to the index provided
        '''
        data = pd.read_csv(self.file_name, header=None)
        data.index += 1


        split_frame = pd.DataFrame()
        output_file = f"{self.directory}/split_file{self.file_number}{self.file_extension}"


        for i in range(1, len(data)+1):
            split_frame = split_frame.append(data.iloc[i-1])
            if i % self.split == 0:
                output_file = f"{self.directory}/split_file{self.file_number}{self.file_extension}"
                if self.file_extension == '.txt':
                    split_frame.to_csv(output_file, header=False, index=False, sep='')
                else:
                    split_frame.to_csv(output_file, header=False, index=False)

                split_frame.drop(split_frame.index, inplace=True)
                self.file_number += 1
            if not split_frame.empty:
                output_file = f"{self.directory}/split_file{self.file_number}{self.file_extension}"
                split_frame.to_csv(output_file, header=False, index=False)


if __name__ == "__main__":
    file, split_number = sys.argv[1], sys.argv[2]
    sp = Split_files(file, split_number)
    sp.split_data()
                    
