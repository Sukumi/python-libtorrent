#/* 
#Copyright: A. Zakai ('Kripken') <kripkensteiner@gmail.com> http://6thsenseless.blogspot.com
#
#2006-15-9
#
#This code is licensed under the terms of the GNU General Public License (GPL),
#version 2 or above; See /usr/share/common-licenses/GPL , or see
#http://www.fsf.org/licensing/licenses/gpl.html
#*/


import torrent
from   time    import sleep

torrent.init()

myTorrent = torrent.addTorrent("ubuntu.torrent")

while True:
	print "STATE:"
	print torrent.getState(myTorrent)
	print ""

#	print "PEER INFO:"
	print torrent.getName(myTorrent)
#	print torrent.getPeerInfo(myTorrent)
#	print ""

	sleep(1)
