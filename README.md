# bookkeeping-app
 Sorts a categories personal transactions to generate insights on your financial status.

 This app uses my personal daily transactions from ING Bank.
 It sorts and categorises known bankaccounts/names that are associated with certain expenses.
 Such as the "Albert Heijn B.V." going into groceries. 

After sorting the expenses and income streams it will visuals the results 


<!-- pip install virtualenv
python -m venv venv -->

# In cmd.exe
venv\Scripts\activate.bat
# In PowerShell
venv\Scripts\Activate.ps1

# if 'running' scripts is disabled in your PowerShell
Set-ExecutionPolicy Unrestricted -Scope Process
Set-ExecutionPolicy Unrestricted -Force


pip freeze > requirements.txt
pip install -r requirements.txt

deactivate