#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  peoplecgi.py
#  
#  Copyright 2018 yorlysoro <yorlysoro@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import cgi, shelve, sys, os
shelvename = 'class-shelve'
fieldnames = ('name', 'age', 'job', 'pay')

form = cgi.FieldStorage()
print('Content-type: text/html')
sys.path.insert(0, os.getcwd())

replyhtml = """
<html>
<title> People Input Form</title>
<body>
<form method=POST action="peoplecig.py">
	<table>
	<tr><th>Key<td><input type=text name=key value="%(key)s">
	$ROWS$
	</table>
	<p>
	<input type=submit value="Fetch", name=action>
	<input type=submit value="Update", name=action>
</form>
</body>
</html>
"""

rowhtml = '<tr><th>%s<td><input type=text name=%s value="%%(%s)s">\n'
rowshtml = ''
for fieldname in fieldnames:
	rowshtml += (rowhtml %((fieldname,)* 3))
replyhtml = replyhtml.replace('$ROWS$', rowshtml)

def htmlize(adict):
	new = adict.copy()
	for field in fieldnames:
		value = new[field]
		new[field] = cgi.escape(repr(value))
	return new
	
def fetchRecord(db, form):
	try:
		key = form['key'].value
		record = db[key]
		fields = record.__dict__
		fields['key'] = key
	except:
		fields =dict.fromkeys(fieldnames, '?')
		fields['key'] = 'Missing or invelid key!'
	return fields
	
def updateRecord(db, form):
	if not 'key' in form:
		fields = dict.fromkeys(fieldnames, '?')
		fields['key'] = 'Missing key input!'
	else:
		key = form['key'].value
		if key in db:
			record = db[key]
		else:
			from person import Person
			record = Person(name='?'. age='?')
		for field in fieldnames:
			setattr(record, field, eval(form[field].value))
		db[key] = record
		fields = record.__dict__
		fields['key'] = key
	return fields
	
db = shelve.open(shelvename)
action = form['action'].value if 'action' in form else None
if action == 'Fetch':
	fields = fetchRecord(db, form)
elif action == 'Update':
	fields = updateRecord(db,form)
else:
	fields = dict.fromkeys(fieldnames, '?')
	fields['key'] = 'Missing or invalid action!'
db.close()
print(replyhtml % htmlize(fields))
