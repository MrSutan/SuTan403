#!/usr/bin/python

import os 
import random 
import sys 
import time 
import socket
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1) 
angka = 0
while(angka<5):
    mengetik('TOOLS Jowo by Fani An & Mod by Fedly M.F.....')
    angka+=1
print ("+---------------------------------------------------------------------------+")
print ("|+-------------------------------------------------------------------------+|")
print ("||                  ________                                               ||")
print ("||                  |______|     /\        /\                              ||")
print ("||                  ________     \ \  /\  / / _______           +------+   ||")
print ("||                  |      |      \ \/  \/ /  |_____|   /\    /\|+-----+   ||")
print ("||                  |      |       \  /\  /   ||___||  /  \  / /||  ______ ||")
print ("||                  |      |        \/  \/    |_____| / /\ \/ / ||  ----|| ||")
print ("||                  |      |                         / /  \  /  ||______|| ||")
print ("||                  |      |                         \/    \/   |________| ||")
print ("||                  |      |  ________                         ________    ||")
print ("||                  |      | |        |  /\              /\   |       |    ||")
print ("||           --------      | | _____  | /  \            /  \  | _____ |    ||")
print ("||           |    TOOLS    | | |    | | \   \    /\    /   /  | |   | |    ||")
print ("||           |    JOWO     | | |____| |  \   \  /  \  /   /   | |___| |    ||")
print ("||           |_____________| |________|   \   \/    \/   /    |_______|    ||")
print ("||                                         \      /\    /                  ||")
print ("||                                          \    /  \  /                   ||")
print ("||                                           \  /    \/                    ||")
print ("||                                            \/                           ||")
print ("||                                                                         ||")
print ("||                   /\      /\                                            ||")
print ("||                   \ \    / /    222222                                  ||")
print ("||                    \ \  / /        22                                   ||")
print ("||                     \ \/ /        22                                    ||")
print ("||                      \  /        22                                     ||")
print ("||                       \/  ()    222222                                  ||")
print ("||                                                                         ||")
print ("||         by Fani AN                                                      ||")
print ("||                  +----------------------------------------+             ||")
print ("||                  |      >>>>TOOLS JAWA BY FANI AN<<<<     |             ||")
print ("||                  |                                        |             ||")
print ("||                  |          >>>MOD BY FEDLY.M.F<<<        |             ||")
print ("||                  |                                        |             ||")
print ("||                  |     >>>>>HARGAI PEMBUAT SCRIPT<<<<<    |             ||")
print ("||                  +----------------------------------------+             ||")
print ("||                                                                         ||")
print ("|+-------------------------------------------------------------------------+| ")
print ("+---------------------------------------------------------------------------+")



def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.2)
mengetik('TOOLS JOWO BUATAN FANY AN DI MOD OLEH FEDLY.MF HARGAI PEMBUAT TOOLS KALO MAU MERUBAH TOOLS INI IJIN TERLEBIH DAHULU DENGAN PEMBUAT SCRIPT')
key = raw_input("pencet enter untuk lanjut.....")


print "      hallo pakde :v     "
print "      niki gaweane kulo  "
print "      sederhana tapi banyak manfaat :'v"
print "      seng nggawe=fani an"
print "      fesbuk=Fani AN"


print "1.goleki link admin melbu (admin login scan)"
print "2.gawe virus"
print "3.Auto comment pesbuk"
print "4.dedeos"
print "5.Gawe script depes"
print "6.Recondog"
print "7.upload panel finder"
print "8.whois lookup"
print "0.gawe metu"

jowo =raw_input("[+]monngo dipilih>>>>")


if jowo == '01' or jowo == '1':
	try:
		import gam
	except(ImportError):
		print "file raono mungkin kehapus"
		sys.exit()

elif jowo == '02' or jowo == '2':
        print "NOTE..!!!"
        print "(virus akan ke simpan di file jowo)"
	try:
		import vbugmap
	except(ImportError):
		print "file raono mungkin kehaapus"
		sys.exit()

elif jowo == '03' or jowo == '3':
        print "NOTE...!!!!"
        print "(UBAH TEKS COMMENT DI msg.txt)"
	try:
		import bot_komen
	except(ImportError):
		print "file raono mungkin kehapus"
		sys.exit()

elif jowo == '04' or jowo == '4':
	try:
		import ilucx
	except(ImportError):
		print "file raono mungkin kehapus"
		sys.exit()

elif jowo == '05' or jowo == '5':
	try:
		import create
	except(ImportError):
		print "file raono mungkin kehapus"
		sys.exit()

elif jowo == '06' or jowo == '6':
	try:
		import dog
	except(ImportError):
		print "file raono mungkin kehapus"
		sys.exit()
	
elif jowo == '07' or jowo == '7':
	try:
		import upf
	except(ImportError):
		print "file raono mungkin kehapus"
		sys.exit()

elif jowo == '08' or jowo == '8':
        try:
                import whs
        except(ImportError):
                print"file raono mungkin kehapus"
                sys.exit()

elif jowo == '00' or jowo == '0':
    sys.exit()
    
else:
	print "\n[!] salah pakde\n"
	time.sleep(2)
	restart_program()
