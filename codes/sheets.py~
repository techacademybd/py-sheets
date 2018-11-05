import gspread
from oauth2client.service_account import ServiceAccountCredentials
import webbrowser

'''
Ref: https://console.developers.google.com/apis/credentials?project=sheets-test-219809
    
   + Download credentials and store in same folder
   + Open credentials and get client_email
   + Share it with the spreadsheet file you want to access
'''

# which APIs are used
scope = ['http://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

# keep secret
credentials = ServiceAccountCredentials.from_json_keyfile_name('Sheets Test-1b7944f419c8.json', scope)

# authorize
gc = gspread.authorize(credentials)

# open ss
worksheet = gc.open('test')
wks_1 = worksheet.get_worksheet(0)
wks_2 = worksheet.get_worksheet(1)

# read, write, update, append, delete


def read_data():
    data = wks_2.get_all_records()
    print(data)


def cell_value(r, c):
    # take input row and col
    x = wks_1.cell(r, c).value
    # print(x)
    return x


def empty_string(val):
    if len(val) == 0:
        raise ValueError("String is empty, SYSTEM ANGRY!")
    else:
        return val


def row_col(val):
    val_find = wks_1.find(val)
    row, col = val_find.row, val_find.col
    return row, col


'''
name = cell_value(2, 1)
serial = cell_value(2, 2)

print("\n")
print("Your name is "+str(name) + " and your serial is " + str(serial))
print("\n")

'''

user_input_name = input("Enter person's name whose age you want to see: ")

# get row col for that input
# r, c = row_col(user_input_name)
# name header
# name = wks_1.cell(r, c).value
# age header
# age = empty_string(wks_2.cell(r, 2).value)
# link header
# link = empty_string(wks_2.cell(r, 3).value)

# get row col value from wks_1 and store in variable
r, c = row_col(user_input_name)

# find name in wks_1 and store it
name = wks_1.cell(r, c).value

# find name in wks_2 and get row, col
find = wks_2.find(name)
x, y = find.row, find.col

# get age for that name in wks_2
age = empty_string(wks_2.cell(x, 2).value)

# get link for that name in wks_2
link = empty_string(wks_2.cell(x, 4).value)

# print details
print("Name: " + str(user_input_name))
print("Age: " + str(age))
print("Link: " + str(link))


# open the link
# webbrowser.open(link)



























#print(worksheet.cell(2,1).value)
#worksheet.update_acell('B2', '0)
#worksheet.update_cell(3,2, 'new val')

#print(worksheet.find('Test'))

#list_of_cells = worksheet.findall('Test')


#list_of_cells[2].value = 'now'

#worksheet.update_cells(list_of_cells)

#for cell in list_of_cells:
 #   cell.value = 'Looped value'

#worksheet.update_cells(list_of_cells)








#https://www.youtube.com/watch?v=yPQ2Gk33b1U&t=19s

# delete row by indexing from ss
#index = 2
#worksheet.delete_row(index)

#append data
#worksheet.append_row(['Irfan', '4'])


