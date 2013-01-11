#!/usr/bin/python
#
# client.py
#
# Author: Zex

from basic import *

sk = s.socket(s.AF_INET, s.SOCK_DGRAM)
message = file('Xfile')

sk.sendto(file.read(message), (basic['host'], basic['port']))

reply, server = sk.recvfrom(basic['maxsize'])

person = Person()
person.ParseFromString(reply)

print 'server says:'
print 'person id: [', getattr(person, 'id'), ']'
print 'person name: [', getattr(person, 'name'), ']'
print 'person email: [', getattr(person, 'email'), ']'

sk.close()
file.close(message)
