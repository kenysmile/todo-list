import sqlite3
import model as dbHandles

a = []
users = dbHandles.selectUser()

#print(users)#
def filter_value(someList, value):
    for x, y in someList:
        if x == value:
            return 'Okie'
        else:
            return 'Error'

print(filter_value(users, 'asdsadsdsa'))
# a = ''.join(users)
#
    # for a in users:
    #     if a == 'Tu':
    #         print('Okie')
    #     else:
    #         print('False')

