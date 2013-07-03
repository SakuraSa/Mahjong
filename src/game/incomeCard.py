# -*- coding: utf-8 -*-

import card,consts

class incomeCard(object):
	def __init__(self,card,incomeType,incomdeFrom,yifaTurn=False,haidiTurn=False,WLichi=False):
		self.card=card
		self.incomeType=incomeType
		self.incomdeFrom=incomdeFrom
		self.yifaTurn=yifaTurn
		self.haidiTurn=haidiTurn
		self.WLichi=WLichi

	def __eq__(self,target):
		return self.card==target.card and self.incomeType==target.incomeType and self.incomdeFrom==target.incomdeFrom

	def __str__(self):
		return '%s:%s:%s' % (str(self.card),consts.incomeCardTypeStrDic[self.incomeType],consts.incomrCardFromTypeStrDic[self.incomdeFrom])

	def __code__(self):
		return tuple([self.card.id,self.incomeType,self.incomdeFrom])

	@staticmethod
	def Parse(code,package):
		return incomeCard(package.getCardByID(code[0]),code[1],code[2])


if __name__=='__main__':
	import cardPackage

	cp=cardPackage.cardPackage('CARDPACKAGE_4REDDORA')
	lst=list(cp.shuffleIter())

	print incomeCard(lst[0],consts.ZIMO,consts.FROM_SELF)
	print incomeCard(lst[1],consts.RIVER,consts.FROM_UPPER)
	print incomeCard(lst[2],consts.JIAGANG,consts.FROM_MIDDLE)
	print incomeCard(lst[3],consts.ANGANG,consts.FROM_DOWN)
	print incomeCard(lst[4],consts.LINGSHANG,consts.FROM_SELF)