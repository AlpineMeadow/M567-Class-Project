#! /usr/bin/env python3

def main() :
    import ClassReadDataFunctions as CRDF

    #The name of the stock we are looking at.
    StockAbbrev = 'nflx'

    #The date and time for the data.  These will have to match up with the
    #data file you want to look at.
    year = 2020
    month = 2
    day = 26
    hour = 7
    minute = 31

    #Convert to strings with the proper formatting.
    yearStr = str('{0:04d}'.format(year))
    monthStr = str('{0:02d}'.format(month))
    dayStr = str('{0:02d}'.format(day))
    hourStr = str('{0:02d}'.format(hour))
    minuteStr = str('{0:02d}'.format(minute))    

    #Create the dateTime string needed to access the file.
    dateTime = yearStr + monthStr + dayStr + hourStr + minuteStr

    #Create a filename that is holding the data.
    path = '/path/to/where/you/are/storing/data/'
    fname = 'StockPrice_' + StockAbbrev + dateTime + '.txt'
    filename = path + fname


    #Get the data.  It will be returned as a numpy array with first column being time
    #that the data were collected and the second column being the price at that time.
    Data = CRDF.readData(dateTime, filename)

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  main()
