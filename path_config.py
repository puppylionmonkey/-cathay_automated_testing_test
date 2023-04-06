import os
import getpass
import sys

os_system = sys.platform
your_name = getpass.getuser()
# print(getpass.getuser())

# project_path
current_directory = os.path.dirname(os.path.abspath(__file__))
# print(current_directory)
project_path = current_directory + '/'

# chrome_path
chrome_path = ''
if os_system == 'win32' or os_system == 'cygwin':  # windows
    chrome_path = 'C:/Users/' + your_name + '/AppData/Local/Google/Chrome/'
elif os_system == 'darwin':  # mac
    your_name = getpass.getuser()
    chrome_path = 'Users/' + your_name + '/Library/Application Support/Google/Chrome'
