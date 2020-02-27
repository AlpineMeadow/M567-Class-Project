#! /usr/bin/env python3

#A function to read data.
def readData(dateTime, StockAbbrev) :
  import time
  import numpy as np

  path = '/path/to/where/you/are/storing/data/'
  fname = 'StockPrice_' + StockAbbrev + dateTime + '.txt'
  filename = path + fname

  #Read in the data.
  data = np.loadtxt(filename, delimiter = ',')

  #Get rid of duplicate data points.
  datetime, price = getGoodValues(data[:,0], data[:,1])

  #Return the array of datetimes and prices.
  return np.c_[datetime, price]
#End of the function readData.py
##################################################################################

##################################################################################
#Create a function that gets rid of duplicate times.
def getGoodValues(time, price) :
  #Each Input is assumed to be an array of floats.
  #Each output is an array of floats.
  import numpy as np

  #Declare some lists.
  goodtime = []
  goodprice = []

  #Check to see if the inputs are floats.  If not make them.
  if isinstance(time, list) :
    time = np.asarray(time)
  if isinstance(price, list) :
    price = np.asarray(price)
    
  #Pass through the data.
  for i in range(len(time)) :
    #For each time value subtract time from itself to find values that are the same.
    temp = time[i] - time

    #Now create a vector of indices that have the same time.
    b = np.asarray(temp == 0).nonzero()

    #Pick the first of the indices.
    startin = b[0][0]
    
    if (startin < i) :  #if the index is less than i. We are looking at a duplicate time so just pass.
        pass
    if (startin == i) :  #if the index is the same as i. Append that time and price to the lists.
        goodtime.append(time[b[0][0]])
        goodprice.append(price[b[0][0]])

  #Now convert the lists to numpy arrays.
  time = np.asarray(goodtime)
  price = np.asarray(goodprice)
   
  #Return the good times and prices.
  return time, price 
#End of the function GetGoodValues.py
