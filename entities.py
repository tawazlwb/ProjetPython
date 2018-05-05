#!/usr/bin/python
# -*- coding: utf-8 -*-

class Utilisateur:
    
	def __init__(self, uid, cn, sn, givenName, mail, uidNumber, gidNumber, homeDirectory, loginShell, userPassword, shadowExpire):
		self.__uid = uid
		self.__cn = cn
		self.__sn = sn
		self.__givenName = givenName
		self.__mail = mail
		self.__uidNumber = uidNumber
		self.__gidNumber = gidNumber
		self.__homeDirectory = homeDirectory
		self.__loginShell = loginShell
		self.__userPassword = userPassword
		self.__shadowExpire = shadowExpire
            
	@property
	def Uid(self):
		return self.__uid
    
	@Uid.setter
	def Uid(self, uid):
		self.__uid = uid
    
	@property
	def Cn(self):
		return self.__cn
    
	@Cn.setter
	def Cn(self, cn):
		self.__cn = cn

	@property
	def Sn(self):
		return self.__sn
    
	@Sn.setter
	def Sn(self, sn):
		self.__sn = sn
    
	@property
	def GivenName(self):
		return self.__givenName
    
	@GivenName.setter
	def GivenName(self, givenName):
		self.__givenName = givenName

	@property
	def Mail(self):
		return self.__mail
    
	@Mail.setter
	def Mail(self, mail):
		self.__mail = mail

	@property
	def UidNumber(self):
		return self.__uidNumber
    
	@UidNumber.setter
	def UidNumber(self, uidNumber):
		self.__uidNumber = uidNumber

	@property
	def GidNumber(self):
		return self.__gidNumber
    
	@GidNumber.setter
	def GidNumber(self, gidNumber):
		self.__gidNumber = gidNumber

	@property
	def HomeDirectory(self):
		return self.__homeDirectory
    
	@HomeDirectory.setter
	def HomeDirectory(self, homeDirectory):
		self.__homeDirectory = homeDirectory

	@property
	def LoginShell(self):
		return self.__loginShell
    
	@LoginShell.setter
	def LoginShell(self, loginShell):
		self.__loginShell = loginShell

	@property
	def UserPassword(self):
		return self.__userPassword
    
	@UserPassword.setter
	def UserPassword(self, userPassword):
		self.__userPassword = userPassword

	@property
	def ShadowExpire(self):
		return self.__shadowExpire
    
	@ShadowExpire.setter
	def ShadowExpire(self, shadowExpire):
		self.__shadowExpire = shadowExpire
        
	def __str__(self):
		return "uid : %s, cn : %s, sn : %s, givenName : %s, gidNumber : %s." %(self.__uid, self.__cn, self.__sn, self.__givenName, self.__gidNumber)
	
	def __repr__(self):
		return "uid : %s, cn : %s, sn : %s, givenName : %s, gidNumber : %s." %(self.__uid, self.__cn, self.__sn, self.__givenName, self.__gidNumber)
    

class Groupe:
    
	def __init__(self, cn, gidNumber, description, memberUid):
		self.__cn = cn
		self.__gidNumber = gidNumber
		self.__description = description
		self.__memberUid = memberUid
            
	@property
	def Cn(self):
		return self.__cn
    
	@Cn.setter
	def Cn(self, cn):
		self.__cn = cn

	@property
	def GidNumber(self):
		return self.__gidNumber
    
	@GidNumber.setter
	def GidNumber(self, gidNumber):
		self.__gidNumber = gidNumber

	@property
	def Description(self):
		return self.__description
    
	@Description.setter
	def Description(self, description):
		self.__description = description

	@property
	def MemberUid(self):
		return self.__memberUid
    
	@MemberUid.setter
	def MemberUid(self, memberUid):
		self.__memberUid = memberUid

	def __str__(self):
		return "cn : %s, gidNumber : %s, description : %s, memberUid : %s." %(self.__cn, self.__gidNumber, self.__description, self.__memberUid)

	def __repr__(self):
		return "cn : %s, gidNumber : %s, description : %s, memberUid : %s." %(self.__cn, self.__gidNumber, self.__description, self.__memberUid)


