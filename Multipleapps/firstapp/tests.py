from django.test import TestCase

# Create your tests here.

from pathlib import Path 
print(__file__) # It returns the name of the file 
fpath = Path(__file__)
print(type(fpath)) #<class 'pathlib.WindowsPath'>
complete_path=fpath.resolve()
print(complete_path)

# use short 
print(Path(__file__).resolve()) 
#C:\Users\Akshay\Documents\ALL Folders\DSJ\Multipleapps\firstapp\tests.py
print(Path(__file__).resolve().parent)
# C:\Users\Akshay\Documents\ALL Folders\DSJ\Multipleapps\firstapp
print(Path(__file__).resolve().parent.parent)
#C:\Users\Akshay\Documents\ALL Folders\DSJ\Multipleapps