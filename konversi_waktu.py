{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print('Konversi Waktu')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Masukan Detik :72901\n",
      "Konversi : 20 : 15 : 0 1\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "import re\n",
    "\n",
    "seconds = (input('Masukan Detik :'))# input caller\n",
    "\n",
    "def timeConverter(seconds): #function( parameter seconds )\n",
    "    \n",
    "    check = re.search(\"[a-z]\",seconds) or re.search(\"[A-Z]\",seconds) or re.search(\"[$#@]\",seconds)\n",
    "    # check apakah ada [a-z]atau[A-Z]atau[$#@] \n",
    "    if not check: # kalau check tdk ada, berarti hanya angka\n",
    "        seconds = int(seconds) #ubah ke int\n",
    "\n",
    "        if seconds > 359999: #kalau lebih dr 35999, print Invalid Input\n",
    "            print('Invalid Input')\n",
    "        else:\n",
    "            hour = math.floor(seconds/3600) #mencari jumlah jam\n",
    "            minute = math.floor((seconds%3600)/60) #mencari jumlah menit, modulo detik dari jam, dibagi 60\n",
    "            second = math.floor(seconds-(hour*3600)-(minute*60)) #mencari jumlah detik tersisa\n",
    "\n",
    "\n",
    "        #print('Konversi :', hour,':',minute,':',second) --> utk print biasa(tdk digunakan)\n",
    "\n",
    "        #penampilan 00 : 00 : 00\n",
    "            if hour >= 10 and minute >= 10 and second >= 10:\n",
    "                print('Konversi :', hour,':',minute,':',second)\n",
    "            elif hour >= 10 and minute < 10 and second < 10:\n",
    "                print('Konversi :', hour, ':', '0', minute,':', '0', second)\n",
    "            elif hour >= 10 and minute >= 10 and second < 10:\n",
    "                print('Konversi :', hour, ':', minute,':', '0', second)\n",
    "            elif hour >= 10 and minute < 10 and second >= 10:\n",
    "                print('Konversi :', hour, ':', '0', minute,':', second)\n",
    "            elif hour < 10 and minute < 10 and second < 10:\n",
    "                print('Konversi :', '0', hour, ':', '0', minute,':', '0', second)\n",
    "            elif hour < 10 and minute < 10 and second >= 10:\n",
    "                print('Konversi :', '0', hour, ':', '0', minute,':', second)\n",
    "            elif hour < 10 and minute >= 10 and second >= 10:\n",
    "                print('Konversi :', '0', hour, ':', minute,':', second)\n",
    "            elif hour < 10 and minute >= 10 and second < 10:\n",
    "                print('Konversi :', '0', hour, ':', minute,':','0', second)\n",
    "\n",
    "\n",
    "    else:\n",
    "        print('Invalid Input')\n",
    "\n",
    "\n",
    "    \n",
    "timeConverter(seconds)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Masukan Detik :346666\n",
      "Konversi : 96 : 17 : 46\n"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
