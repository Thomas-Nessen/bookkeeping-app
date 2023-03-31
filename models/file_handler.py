import pandas as pd
import locale as lc

class FileHandler(object):
    def __init__(self, local=None):
      self.local = lc.setlocale(lc.LC_ALL, 'nl_NL')

		
   #reads the transaction csv file. selects and renames columns
    '''
    Read csv file, select columns, set data types
    '''
    @classmethod
    def readFile(self, path, file, sep=';'):
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
    Rename columns to a more appropriate name
    '''
    @classmethod
    def renameColumns(self, ta_data):
        ta_data = ta_data.rename(columns={
            "Name / Description": "Name",
            "Amount (EUR)": "Amount",
            "Notifications": "Description"
            })
        return ta_data
    
    '''
    Changes the amount to positive or negative according to if it is debit or credit.
    '''
    @classmethod
    def formatAmounts(self, amount, deb_cred):
        if deb_cred == "Debit":
            return (amount * -1)
        elif deb_cred == "Credit":
            return amount
        
    def fileHandlerController(self, path, file):
        
        data = self.readFile(path, file)
        clean_data = self.renameColumns(data)
        clean_data['Amount'] = clean_data.apply(lambda x: 
            self.formatAmounts(x['Amount'], x['Debit/credit']), axis=1)
        
        return clean_data
