#!/usr/bin/python
# -*- coding: utf-8 -*-

## python db_password.py

import mysql.connector
import ldap
import codecs
import time
from datetime import datetime

from ldap import modlist as modlist
from entities import Utilisateur


conMySQL = mysql.connector.connect(host="sql.ikheiry.fr", user="root", password="root", database="ldap_db")
cursor = conMySQL.cursor()
cursor.execute("""SELECT * FROM utilisateurs WHERE isUpdate = 1""")
rows = cursor.fetchall()
users = []

if(len(rows) == 0):
	print("Le serveur ldap et la base de données sont déjà synchronisé!")
else:
	for row in rows:
		u = Utilisateur(row[3], row[2] + " " + row[1], row[1], row[2], row[7], row[5], row[6], "/home/users/" + row[3], "/bin/sh", row[4], row[8])
		users.append(u)

	# ldap
	conLDAP = ldap.initialize('ldap://ldap1.ikheiry.fr:389/')	
	conLDAP.simple_bind_s('cn=admin,dc=ikheiry,dc=fr', 'Mr$120055')

	baseDN = "ou=ou-ikheiry-ldap,dc=ikheiry,dc=fr"
	searchScope = ldap.SCOPE_SUBTREE
	retrieveAttributes = None 
	searchFilter = "cn=Ismail*"
	ldap_result_id = conLDAP.search(baseDN, searchScope, searchFilter, retrieveAttributes)
	result_set = []
	result_type, result_data = conLDAP.result(ldap_result_id, 0)
	if (result_data != []):
		for i in range(len(users)):
			dn, data = result_data[i]
			old_value = data
			d = time.mktime(datetime.strptime(str(users[i].ShadowExpire), "%Y-%m-%d").timetuple())*1000
			d = int(d/(1000*60*60*24))+1
			new_value = {
				"objectClass": ["inetOrgPerson", "posixAccount", "person", "shadowAccount", "organizationalPerson"],
				"uid": [str(users[i].Uid)],
				"sn": [str(users[i].Sn)],
				"givenName": [str(users[i].GivenName)],
				"cn": [str(users[i].Cn)],
				"uidNumber": [str(users[i].UidNumber)],
				"gidNumber": [str(users[i].UidNumber)],
				"loginShell": [str(users[i].LoginShell)],
				"homeDirectory": [str(users[i].HomeDirectory)],
				"userPassword" : [str('{MD5}' + codecs.encode(codecs.decode(users[i].UserPassword, 'hex'), 'base64').decode())],
				"mail": [str(users[i].Mail)],
				"shadowExpire": [str(d)]
			}
			modlist = modlist.modifyModlist(old_value, new_value)
			conLDAP.modify_s(dn, modlist)

		cursor.execute("""UPDATE utilisateurs SET isUpdate=0 WHERE isUpdate = 1""")
		conMySQL.commit()

		conLDAP.unbind_s()

conMySQL.close()
print("finish")


