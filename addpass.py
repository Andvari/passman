#!/usr/bin/env python
'''
Created on Jul 3, 2015

@author: nemo
'''

import sqlite3
import sys
import os

conn = sqlite3.connect("/home/nemo/pass.db")   #@UndefinedVariable

c = conn.cursor()

c.execute("create table if not exists accounts(id integer primary key, site text, login text, password text, comments text);");

if ((len(sys.argv) < 4)or(len(sys.argv) > 5)):
    print "usage: addpass.py <site> <login> <passwd> [<comments>]"
    os._exit(1)


record = [sys.argv[1], ]

if (len(sys.argv) == 4):
    record = [sys.argv[1], sys.argv[2], sys.argv[3]]
    c.execute("insert into accounts(site, login, password) values(?,?,?);", record)
    
if (len(sys.argv) == 5):
    record = [sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]]
    c.execute("insert into accounts(site, login, password, comments) values(?,?,?,?);", record)

for record in c.execute("select * from accounts;"):
    print record

    
conn.commit()
conn.close()

print "Account added successfully"

