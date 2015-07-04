#!/usr/bin/env python
'''
Created on Jul 4, 2015

@author: nemo
'''

import sqlite3
import sys
import os

conn = sqlite3.connect("/home/nemo/pass.db")   #@UndefinedVariable

c = conn.cursor()

c.execute("create table if not exists accounts(id integer primary key, site text, login text, password text, comments text);");

if ( len(sys.argv) !=2 ):
    print "usage: showpass.py <site>"
    os._exit(1)

record = [sys.argv[1]]

if (sys.argv[1] == 'all'):
    for record in c.execute("select * from accounts;"):
        print "id: " + str(record[0])
        print "site: " + record[1]
        print "login: " + record[2]
        print "password: " + record[3]
        try:
            print "comments: " + record[4]
        except:
            pass
        print "---------------------"
else:
    for record in c.execute("select * from accounts where site=?;", record):
        print "id: " + str(record[0])
        print "site: " + record[1]
        print "login: " + record[2]
        print "password: " + record[3]
        try:
            print "comments: " + record[4]
        except:
            pass
        print "---------------------"
    
conn.commit()
conn.close()
