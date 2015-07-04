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

if (len(sys.argv) != 2):
    print "usage: rmpass.py <id>"
    os._exit(1)


record = [sys.argv[1]]

c.execute("delete from accounts where id=?;", record)

for record in c.execute("select * from accounts;"):
    print record

    
conn.commit()
conn.close()

print "Account deleted"

