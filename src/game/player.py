# -*- coding: utf-8 -*-

import consts,card

class player(object):
	def __init__(self):
		self.richiTurn=-1
		self.wRichi=False
		self.lockedCards=set()
		self.handCards=set()
		self.point=0
		self.wind_self=consts.loc_EAST
		self.wind_game=consts.loc_EAST

	def __str__(self):
		tem=list(self.handCards)
		tem.sort()
		return '%s:%s %s' % (consts.playerLocationTypeStrDic[self.wind_self],','.join(map(str,tem)),' '.join(map(str,self.lockedCards)))

	def allCards(self):
		for c in self.handCards:
			yield c
		for lc in self.lockedCards:
			for c in lc.allCards:
				yield c

	def dora(self,pointers=[]):
		doraCounter=0
		for c in self.allCards():
			c+=c.dora(pointers)
		return doraCounter

	def hasYao(self):
		for c in self.allCards():
			if c.isYao(): return True
		return False

	def hasMing(self):
		for i in self.lockedCards:
			if i.isMing():
				return True
		return False

	def contain(self,cards):
		if isinstance(cards,card.card):
			return cards in self.handCards
		for c in cards:
			if not c in self.handCards:
				return False
		return True

	def remove(self,cards):
		if isinstance(cards,card.card):
			self.handCards.remove(cards)
		else:
			for c in cards:
				self.handCards.remove(c)

