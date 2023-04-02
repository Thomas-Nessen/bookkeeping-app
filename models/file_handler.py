import pandas as pd
import locale as lc

from models.cleaner_class import CleanerClass


class FileHandler(object):
    def __init__(self, local=None):
      self.local = lc.setlocale(lc.LC_ALL, 'nl_NL')

   #reads the transaction csv file. selects and renames columns
    '''
    Read csv file, select columns, set data types
    '''
    @classmethod
    def readFile(self, path, file, sep=';'): # add cols
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

        
    def fileHandlerController(self, path, file):
        pass