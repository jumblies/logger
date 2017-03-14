import gspread
from oauth2client.service_account import ServiceAccountCredentials
import serial
import time


def writeSheet():
    pass
scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('My Project-d27053acc111.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open("logger").sheet1 
wks.update_acell('D1', 'The thing works')
wks.update_acell('A1', 'Time')
wks.update_acell('B1', 'Temp')
wks.update_acell('C1', 'Date')


# Select a cell range
cell_list = wks.range('A2:D1000')

# Update values
for cell in cell_list:
    cell.value = ""

# Send update in batch mode
wks.update_cells(cell_list)

# Temperature and humidity lists for batch uploading
readList=[]


with open("templog.txt", "a+") as datafile:

    ser = serial.Serial('/dev/ttyACM0', 9600)
    n = 0
    for n in range(2,1000):
        reading = ser.readline()
        if "T:" in reading:
            readList.append([0])
            
        wks.update_acell('B'+str(n), reading)
        wks.update_acell('A'+str(n), time.strftime('%H:%M')) #Stringtime
        wks.update_acell('C'+str(n), time.strftime('%Y%m%d')) #date string
        n+=1

        datafile.write(str(reading))
        print(reading, n)
##        if n >= 21:
##            datafile.close()
##            datafile = open("templog.txt", "a+")
##            n=0
datafile.close()




    

