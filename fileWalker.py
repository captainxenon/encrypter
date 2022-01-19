import os

# WORKING OS WALK LOOP
for dirpath, dirnames, filenames in os.walk('/Users/dhruvkulkarni/Desktop'):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()
