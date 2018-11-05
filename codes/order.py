import gspread
from oauth2client.service_account import ServiceAccountCredentials

'''
   + Download credentials and store in same folder
   + Open credentials and get client_email
   + Share it with the spreadsheet file you want to access
'''

print("\nAccessing Spreadsheet")

# APIs are used
scope = ['http://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

# keep secret
credentials = ServiceAccountCredentials.from_json_keyfile_name('Sheets Test-1b7944f419c8.json', scope)

# authorize
gc = gspread.authorize(credentials)

# open ss
worksheet = gc.open('test')

# main order cart
wks_1 = worksheet.get_worksheet(2)

# component with associated links
wks_2 = worksheet.get_worksheet(3)


# read, write, update, append, delete

def read_data():
    data = wks_2.get_all_records()
    print(data)


def empty_string(val):
    if len(val) == 0:
        raise ValueError("String is empty, SYSTEM ANGRY!")
    else:
        return val


def row_col(val):
    val_find = wks_1.find(val)
    row, col = val_find.row, val_find.col
    return row, col


def comp_list(comps):
    if len(comps) == 0:
        raise ValueError("You don't have anything on the order cart! What do you expect me to order?")
    else:
        return comps


print("\nListing values from cart....")

values_list = comp_list(wks_1.col_values(1)[1:])

print("\nChecking the library and retrieving the links....")

links = []

for component in values_list:

    find = wks_2.find(component)
    r, _ = find.row, find.col
    link = empty_string(wks_2.cell(r, 2).value)
    links.append(link)

print("\nHere are the links: ")
for l in links:
    print(l)








