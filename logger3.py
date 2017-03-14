import serial
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials


# Initial Authorization and initialization of gspread
scope = ['https://spreadsheets.google.com/feeds']

# Not sure if opening is necessary here. 
credentials = ServiceAccountCredentials.from_json_keyfile_name('My Project-d27053acc111.json', scope)
gc = gspread.authorize(credentials) # Authorize
wks = gc.open("logger").sheet1 # open the sheet

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

datalist = [] # List for batch uploading to gspread

# Save data to file
with open("logger2datalist.txt", "a+") as datafile:
def writeToSheeT
    for n in range (2,1500):
        # Open serial comm port for reading from arduino
        ser = serial.Serial('/dev/ttyACM0', 9600)
        reading = ser.readline()
        temp = reading[2:7]
        hum = reading[10:15]
        curtime = time.strftime('%H:%M')
            
        row =[n, curtime, temp, hum]
        print(row)
        datalist.append(row)
        datafile.write(str(row)+"\n")
        if (n % 3 == 0):
##            RE-Authorization and initialization of gspread
##            scope = ['https://spreadsheets.google.com/feeds']
##            credentials = ServiceAccountCredentials.from_json_keyfile_name('My Project-d27053acc111.json', scope)
##            gc = gspread.authorize(credentials)
            wks = gc.open("logger").sheet1
            headers = gspread.httpsession.HTTPSession(headers={'Connection': 'Keep-Alive'})
            gc = gspread.Client(auth=credentials, http_session=headers)
            gc.login()

            for x in range(len(datalist)):
                wks.update_acell('A'+str(datalist[int(x)][0]), datalist[int(x)][1]) # Time entry
                wks.update_acell('B'+str(datalist[int(x)][0]), datalist[int(x)][2]) # Temp entry
                wks.update_acell('C'+str(datalist[int(x)][0]), datalist[int(x)][3]) # Hum entry  
                wks.update_acell('D'+str(datalist[int(x)][0]), time.strftime('%Y%m%d')) #date string
            
            datalist =[]
        if curtime
        n+=1    
print("Successful Clean termination")
wks.update_acell('E1', 'Successful Clean termination')
