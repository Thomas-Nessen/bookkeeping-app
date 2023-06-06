import pandas as pd
import locale as lc
import json
import os

from models.cleaner_class import CleanerClass


class FileHandler(object):
    def __init__(self, local=None):
      self.local = lc.setlocale(lc.LC_ALL, 'nl_NL')

   #reads the transaction csv file. selects and renames columns
    '''
    Read csv file, select columns, set data types
    '''
    @classmethod
    def read_csv_file(self, path, file, sep=';'): # add cols
        cols = {"Date": str,
                "Name / Description": str,
                "Counterparty": str,	
                "Debit/credit":str,
                "Amount (EUR)": float,
                "Transaction type":str,
                "Notifications": str,
                "Tag": str
            }

        ta_data = pd.read_csv(
            filepath_or_buffer= path + file,
            sep= sep,
            usecols= list(cols.keys()),
            dtype= cols,
            parse_dates= ["Date"],
            decimal=','
        )
        return ta_data

        '''
    Read the contents from json file into a dictionary
    '''
    def read_txt_file(self, path2txt:str):
        try:
            with open(path2txt) as txt_file:
                txt_cont = txt_file.read()
            return txt_cont
        except Exception as e: 
            print(e)

    '''
    Read the contents from json file into a dictionary
    '''
    def read_json_file(self, path2json='bookkeeping-app\sorting_codes.json'):
        try:
            with open(path2json) as json_file:
                json_dict = json.load(json_file)
            return json_dict
        except Exception as e: 
            print(e)

    '''
    Write the contents of a dictionary into a json file
    '''
    def write_json_file(self, input_dict:dict, path='bookkeeping-app\sorting_codes.json'):
        try:
            with open(path, 'w') as outfile:
                json.dump(input_dict, outfile)
            return True
        except Exception as e:
            print(e)
            raise TypeError