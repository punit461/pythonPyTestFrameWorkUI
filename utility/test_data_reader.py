import os
import json
import configparser
import openpyxl
from test_cases import project_directory


class ReadData:
    def __init__(self):
        self.project_dir = project_directory

    def read_json(self, file_name, key=None):
        file_path = os.path.join(self.project_dir, "jsons", file_name)
        with open(file_path, 'r') as file:
            data = json.load(file)
        if key:
            return data.get(key)
        return data

    def read_ini(self, file_name, section, option):
        config = configparser.ConfigParser()
        ini_path = os.path.join(self.project_dir, "configurations", file_name)
        config.read(ini_path)
        return config.get(section, option)

    def read_excel(self, file_name, sheet_name, row_num, col_num):
        excel_path = os.path.join(self.project_dir, "worksheets", file_name)
        workbook = openpyxl.load_workbook(excel_path)
        sheet = workbook[sheet_name]
        cell_value = sheet.cell(row=row_num, column=col_num).value
        return cell_value

