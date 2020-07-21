import os
import re
import datetime
import logging
from logging.handlers import RotatingFileHandler
import sys



from database import Database


class Process:

    def __init__(self):
        self.long = 'Long'
        self.lat = 'Lati'
        self.grid = 'Grid'
        self.boxes = 'Boxes'
        self.years = 'Years'
        self.multi = 'Multi'
        self.missing = 'Missing'

        self.grid_ref = 'Grid-ref'

        self.database = Database(r"C:\Projects\JBAConsulting\Source\jba-challenge\python\db\pythonsqlite.db")

        self.rows_to_insert = []
        self.year_start, self.year_end = None, None

        self.logger = self.setup_logging('data_process', r'C:\Projects\JBAConsulting\Source\jba-challenge\python\logs\data.log')

    @staticmethod
    def setup_logging(node_name, logging_filename_path):
        """
        Setup the logger
        :param node_name:
        :param logging_filename_path
        :return:
        """
        new_logger = logging.getLogger(node_name)
        new_logger.setLevel(logging.INFO)
        logging_format = logging.Formatter(fmt='%(asctime)s: %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(logging_format)
        new_logger.addHandler(stream_handler)
        logfile_name = logging_filename_path
        file_handler = RotatingFileHandler(logfile_name, maxBytes=10000000, backupCount=10, mode='a')
        file_handler.setFormatter(logging_format)
        new_logger.addHandler(file_handler)
        return new_logger

    def add_grid_ref_data(self, dataset_file):
        for line in dataset_file:
            if self.grid_ref in line:
                grid_ref_data = line.split('=')[1].strip().split(',')
                x_ref, y_ref = int(grid_ref_data[0]), int(grid_ref_data[1])
                for year in range(0, self.year_end - self.year_start + 1):
                    row_data = dataset_file.readline().replace('  ', ' ').split()
                    for index, value in enumerate(row_data):
                        date = f'{index + 1}/1/{self.year_start + year}'
                        insert_row = (x_ref, y_ref, date, int(value))
                        self.rows_to_insert.append(insert_row)

    def open_file(self, file_path):
        self.logger.info(f'Processing file {file_path}')
        try:
            with open(file_path, 'r') as dataset_file:
                # Header Lines are first 5 lines
                header_lines = [dataset_file.readline() for i in range(0, 5)]
                pattern = r'\[.*?\]'
                for line in header_lines:
                    for match in re.finditer(pattern, line):
                        match_group = match.group()[1:-1]
                        if self.years in match_group:
                            year_range_str = match_group.split('=')
                            year_range = year_range_str[1].strip().split('-')
                            self.year_start, self.year_end = int(year_range[0]), int(year_range[1])

                self.add_grid_ref_data(dataset_file)

                # insert all rows into table
                self.logger.info(f'Inserting {len(self.rows_to_insert)} into database')
                self.database.insert_many_rows(self.rows_to_insert)

        except Exception as ex:
            self.logger.error(ex)


if __name__ == '__main__':
    #path = r'C:\Projects\JBAConsulting\Raw\cru-ts-2-10.1991-2000-cutdown.pre'
    path = sys.argv[1]
    process = Process()
    process.open_file(path)
