#!/usr/bin/python
#
# server.py
#
# Author: Zex

from basic import *

sk = s.socket(s.AF_INET, s.SOCK_DGRAM, 0)

sk.bind(('', basic['port']))

person = Person()

while True:
  message, client = sk.recvfrom(basic['maxsize'])
	print 'call-in client: ', client
#	reply = 'recieved message: [\n' + message + ']'
	name = ''.join([rd.choice(string.lowercase) for x in range(5)])\
		+ ' ' +\
		''.join([rd.choice(string.lowercase) for x in range(5)])
	site = ''.join([rd.choice(string.letters + string.digits)\
		for x in range(6)]) + '.com'

	setattr(person, 'email', name.split(' ')[1] +'@' + site)
	setattr(person, 'name', name)
	setattr(person, 'id', rd.randint(10000, 99999))
	
	reply = person.SerializeToString()
	sk.sendto(reply, client)
