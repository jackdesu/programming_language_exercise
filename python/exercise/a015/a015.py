#!/usr/bin/env python

import sys

def main():
  #secondsOfDay =24 * 60 * 60
  #secondsOfHour = 60 * 60
  #print "hours of day by //: " + str(secondsOfDay // secondsOfHour)
  #print "hours of day by /: " + str(secondsOfDay / secondsOfHour)

  x = raw_input(">>> Input: ")
  inputs = x.split(" ")
  rowSize = inputs[0]
  columnSize = inputs[1]

  print "columnSize: " + columnSize

  rawData = list()
  for x in range(0, int(rowSize)):
    currentRow = raw_input(">>> Input " + str(x) + " row data: ")
    rawData.append(currentRow.split(" "))

  for x in range(0, int(rowSize)):
    print str(x) + " row data: " + "".join(rawData[x])

  resultArray = list()
  for x in range(0, int(columnSize)):
    tmpRow = list()
    for y in range(0, int(rowSize)):
      tmpRow.append(rawData[y][x])
    resultArray.append(tmpRow)

  for x in range(0, len(resultArray)):
    print resultArray[x]
    
if __name__ == "__main__":
  main()
