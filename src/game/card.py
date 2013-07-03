# -*- coding: utf-8 -*-

import consts

class card(object):
	def __init__(self,content,id=-1):
		self.content=content
		self.id=id

	def __eq__(self,target):
		if not isinstance(target,card):
			return False
		return self.content==target.content
	def __lt__(self,target):
		return self.content<target.content
	def __gt__(self,target):
		return target.content<self.content
	def __hash__(self):
		return self.id
	def __str__(self):
		return consts.cardTypeStrDic[self.content]
	def __code__(self):
		return tuple([self.id])

	def isNextOf(self,target,circle=False):
		return consts.isBefor(self.content,target.content,circle)
	def isBeforOf(self,target,circle=False):
		return consts.isNext(self.content,target.content,circle)
	def isYao(self):
		return consts.isYao(self.content)
	def isZi(self):
		return consts.isTypeOf(self.content,consts.WIN) or consts.isTypeOf(self.content,consts.DRA)
	def isShu(self):
		return not self.isZi()
	def is19(self):
		return self.isShu() and (self.content[1]==1 or self.content[1]==9)
	def isGreen(self):
		return self.content[0:2] in consts.GREENCARDS
	def isRed(self):
		return consts.isRedDora(self.content)
	def isWindOf(self,loc):
		return consts.isWindOf(self.content,loc)
	def isTypeOf(self,type):
		return consts.isTypeOf(self.content,type)
	def isRedDora(self):
		return consts.isRedDora(self.content)

	def dora(self,pointers=set()):
		counter=1 if consts.isRedDora(self.content) else 0
		for c in pointers:
			if c.isNextOf(self,circle=True):
				counter+=1
		return counter

	@staticmethod
	def Parse(code,package):
		return package.getCardByID(code[0])

