import math
import re

seconds = (input('Masukan Detik :'))# input caller

def timeConverter(seconds): #function( parameter seconds )
    
    check = re.search("[a-z]",seconds) or re.search("[A-Z]",seconds) or re.search("[$#@]",seconds)
    # check apakah ada [a-z]atau[A-Z]atau[$#@] 
    if not check: # kalau check tdk ada, berarti hanya angka
        seconds = int(seconds) #ubah ke int

        if seconds > 359999: #kalau lebih dr 35999, print Invalid Input
            print('Invalid Input')
        else:
            hour = math.floor(seconds/3600) #mencari jumlah jam
            minute = math.floor((seconds%3600)/60) #mencari jumlah menit, modulo detik dari jam, dibagi 60
            second = math.floor(seconds-(hour*3600)-(minute*60)) #mencari jumlah detik tersisa


        #print('Konversi :', hour,':',minute,':',second) --> utk print biasa(tdk digunakan)

        #penampilan 00 : 00 : 00
            if hour >= 10 and minute >= 10 and second >= 10:
                print('Konversi :', hour,':',minute,':',second)
            elif hour >= 10 and minute < 10 and second < 10:
                print('Konversi :', hour, ':', '0', minute,':', '0', second)
            elif hour >= 10 and minute >= 10 and second < 10:
                print('Konversi :', hour, ':', minute,':', '0', second)
            elif hour >= 10 and minute < 10 and second >= 10:
                print('Konversi :', hour, ':', '0', minute,':', second)
            elif hour < 10 and minute < 10 and second < 10:
                print('Konversi :', '0', hour, ':', '0', minute,':', '0', second)
            elif hour < 10 and minute < 10 and second >= 10:
                print('Konversi :', '0', hour, ':', '0', minute,':', second)
            elif hour < 10 and minute >= 10 and second >= 10:
                print('Konversi :', '0', hour, ':', minute,':', second)
            elif hour < 10 and minute >= 10 and second < 10:
                print('Konversi :', '0', hour, ':', minute,':','0', second)


    else:
        print('Invalid Input')


    
timeConverter(seconds)
