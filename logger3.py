import serial
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Global gspread variables

scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('logger3.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open("logger3").sheet1
headers = gspread.httpsession.HTTPSession(headers={'Connection': 'Keep-Alive'})
gc = gspread.Client(auth=credentials, http_session=headers)

def initSheet():
    """#Sets up sheet for new datalog clearing the first four columns and putting headings on them"""
    gc.login()
    # Clear Spreadsheet and write in new headings
    wks.update_acell('A1', 'Time')
    wks.update_acell('B1', 'Temp')
    wks.update_acell('C1', 'Humidity')
    wks.update_acell('D1', 'Date')
    wks.update_acell('E1', 'The thing works')
    # Select a cell range
    cell_list = wks.range('A2:D1000')
    # Update values
    for cell in cell_list:
        cell.value = ""
    # Send update in batch mode
    wks.update_cells(cell_list)


# list comprehension to generate data for testing
def dataGenerator(numDatapoints):
    cell = [q for q in range(2,numDatapoints)]
    temp = [x/10 for x in range(1000, 940, -1)]
    hum = [r/10 for r in range (900, 940) ]
    curtime = [y for y in range(2300, 2359)]
    datalist = [list(a) for a in zip(cell, curtime, temp, hum)]
    return datalist

def writeToSheet(datalist):
    """Writes data in datalist for the last 10 minutes to sheet"""
    gc.login()
    for x in range(0, len(datalist)):
        wks.update_acell('A'+str(datalist[int(x)][0]), datalist[int(x)][1]) # Time entry
        wks.update_acell('B'+str(datalist[int(x)][0]), datalist[int(x)][2]) # Temp entry
        wks.update_acell('C'+str(datalist[int(x)][0]), datalist[int(x)][3]) # Hum entry
        wks.update_acell('D' + str(datalist[int(x)][0]), time.strftime('%Y%m%d'))  # date string
try:
    datalist = dataGenerator(95)
    print(datalist)
    initSheet()
    writeToSheet(datalist)
    datalist = []
except:
    time.sleep(5)
    writeToSheet(datalist)
print("Successful Clean termination")