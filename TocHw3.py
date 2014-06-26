#encoding: utf-8
#coding: utf-8

# Theory of Computation - Homework 3 -
# Name: 魏喬浩
# Student ID: F74007125
# Compilation: python2 TocHw3.py <URL> <City/District> <Road> <Year>
# Description: This program reads a JSON file and look for matches between the file and the parameters used as input
# during compilation, after getting the matches, the program will retrieve their prices and print the average of them


import sys
import json #to read the JSON object
import urllib2 #to fetch from URL

if len(sys.argv) != 5:  #check for correct number of arguments
        sys.exit('Error on Input, it must be as follows --> %s <URL> <鄉鎮市區> <Road> <Year>' % sys.argv[0])

URL = sys.argv[1]
info = json.load(urllib2.urlopen(URL)) #Get JSON object from URL
sys.argv[4] = int(sys.argv[4]+"00")

total_price = 0
count = 0

for data in info:

        if  sys.argv[2] == data[u'鄉鎮市區'].encode('utf-8') and sys.argv[3] in data[u'土地區段位置或建物區門牌'].encode('utf-8') and sys.argv[4] <= data[u'交易年月']: #Retrieve data when City/District, Road and year have instances in common

                total_price += data[u'總價元']
                count += 1


if count != 0:
        average = total_price/count

        print (average)

else:   #In case there's no parameter match and counter remains in zero, program will print an error
        print('Error: Counter is zero, can not divide by zero~')
                                                                                                                
