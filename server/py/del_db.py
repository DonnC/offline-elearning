# dummy script to delete db using cmd
import os

DB_NAME = 'elearning_test.db'

print('== DELETE TEST DB ==\n')

print('[INFO] Test Database file: ', DB_NAME)

print()

resp = str(input("Are you sure? [y / n]: "))

if resp.lower() == 'y':
    if(os.path.isfile(DB_NAME)):
        os.remove(DB_NAME)
        print('\n> database deleted!')

    else:
        print('\n> database file not found!')

else:
    print('\n> you cancelled the operation')