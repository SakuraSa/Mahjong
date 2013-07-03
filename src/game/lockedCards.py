# -*- coding: utf-8 -*-

import consts

class lockedCards_bass(object):
	def __init__(self,handCards,incomeCard):
		self.handCards=handCards
		self.incomeCard=incomeCard

	def allCards(self):
		yield self.incomeCard.card
		for c in self.handCards:
			yield c

	def dora(self,pointer=set()):
		doraCounter=0
		for c in self.allCards:
			doraCounter+=c.dora(pointer)
		return doraCounter

	def isMing(self):
		return True

	def addToPlayer(self,player):
		for c in self.handCards:
			player.handCards.discard(c)
		player.lockedCards.add(self)

	def __eq__(self,target):
		return self.handCards==target.handCards

	@staticmethod
	@consts.Dec_NoneToIter
	def getAccessableSilos(player,incomeCard):
		if len(player.handCards)<3: return

		for i in lockedCards_CHI.getAccessableSilos(player,incomeCard): yield i
		for i in lockedCards_PENG.getAccessableSilos(player,incomeCard): yield i
		for i in lockedCards_JIAGANG.getAccessableSilos(player,incomeCard): yield i
		for i in lockedCards_MINGGANG.getAccessableSilos(player,incomeCard): yield i
		for i in lockedCards_ANGANG.getAccessableSilos(player,incomeCard): yield i


class lockedCards_CHI(lockedCards_bass):
	def __init__(self,handCards,incomeCard):
		lockedCards_bass.__init__(self,handCards,incomeCard)

	def __str__(self):
		return '%s:%s->%s' % (consts.lockedCardsTypeStrDic[consts.Locked_CHI],','.join(map(str,self.handCards)),str(self.incomeCard.card))

	@staticmethod
	@consts.Dec_NoneToIter
	def getAccessableSilos(player,incomeCard):
		if player.richiTurn>=0:
			return
		if incomeCard.incomdeFrom!=consts.FROM_UPPER:
			return
		if incomeCard.incomeType!=consts.RIVER:
			return

		dic={-2:list(),-1:list(),1:list(),2:list()}
		for c in player.handCards:
			if incomeCard.card.content[0]!=c.content[0]: continue
			dis=consts.getDistance(incomeCard.card.content,c.content)
			if dis==0 or abs(dis)>2: continue
			tem.append(c)
			lst=dic[dis]
			if not c in lst:lst.append(c)

		#-2 & -1
		for i in dic[-2]:
			for j in dic[-1]:
				yield lockedCards_CHI(set([i,j]),incomeCard)
		#-1 & +1
		for i in dic[-1]:
			for j in dic[+1]:
				yield lockedCards_CHI(set([i,j]),incomeCard)
		#+1 & +2
		for i in dic[+1]:
			for j in dic[+2]:
				yield lockedCards_CHI(set([i,j]),incomeCard)


class lockedCards_PENG(lockedCards_bass):
	def __init__(self,handCards,incomeCard):
		lockedCards_bass.__init__(self,handCards,incomeCard)

	def __str__(self):
		return '%s:%s->%s' % (consts.lockedCardsTypeStrDic[consts.Locked_PENG],','.join(map(str,self.handCards)),str(self.incomeCard.card))

	@staticmethod
	@consts.Dec_NoneToIter
	def getAccessableSilos(player,incomeCard):
		if player.richiTurn>=0:
			return
		if incomeCard.incomdeFrom==consts.FROM_SELF:
			return
		if incomeCard.incomeType!=consts.RIVER:
			return

		doras=[];nondoras=[]
		for c in player.handCards:
			if c==incomeCard.card:
				if c.dora():
					doras.append(c)
				else:
					nondoras.append(c)

		if len(nondoras)>=2:
			yield lockedCards_PENG(nondoras[0:2],incomeCard)
		if len(doras)>=2:
			yield lockedCards_PENG(doras[0:2],incomeCard)
		if len(nondoras)>0 and len(doras)>0:
			yield lockedCards_PENG([doras[0],nondoras[0]],incomeCard)
			

class lockedCards_JIAGANG(lockedCards_bass):
	def __init__(self,handCards,incomeCard,pengCards):
		lockedCards_bass.__init__(self,handCards,incomeCard)
		self.pengCards=pengCards

	def __eq__(self,target):
		return self.handCards==target.handCards and self.pengCards==target.pengCards

	def __str__(self):
		return '%s:%s->%s' % (consts.lockedCardsTypeStrDic[consts.Locked_JIAGANG],','.join(map(str,self.handCards)),str(self.incomeCard.card))

	def addToPlayer(self,player):
		player.handCards.discard(self.incomeCard.card)
		player.lockedCards.discard(self.pengCards)
		player.lockedCards.add(self)

	@staticmethod
	@consts.Dec_NoneToIter
	def getAccessableSilos(player,incomes):
		if player.richiTurn>=0:
			return
		
		icl=list()
		if(incomes.incomdeFrom==consts.FROM_SELF and incomes.incomeType==consts.ZIMO):
			icl.append(incomes)
		for c in player.handCards:
			icl.append(incomeCard.incomeCard(c,consts.ZIMO,consts.FROM_SELF))

		dic=list()
		for lc in player.lockedCards:
			if isinstance(lc,lockedCards_PENG):
				for c in icl:
					if lc.incomeCard.card.content[0:2]==c.card.content[0:2]:
						jg=lockedCards_JIAGANG(set(lc.handCards+[lc.incomeCard.card]),c,lc)
						if not jg in dic:
							dic.append(jg)
							yield jg 



class lockedCards_MINGGANG(lockedCards_bass):
	def __init__(self,handCards,incomeCard):
		lockedCards_bass.__init__(self,handCards,incomeCard)

	def __str__(self):
		return '%s:%s->%s' % (consts.lockedCardsTypeStrDic[consts.Locked_MINGGANG],','.join(map(str,self.handCards)),str(self.incomeCard.card))

	@staticmethod
	@consts.Dec_NoneToIter
	def getAccessableSilos(player,incomeCard):
		if player.richiTurn>=0:
			return
		if incomeCard.incomeType!=consts.RIVER or incomeCard.incomdeFrom==consts.FROM_SELF:
			return

		doras=list();nondoras=list()
		for c in player.handCards:
			if c.content[0:2]==incomeCard.card.content[0:2]:
				if c.dora(): doras.append(c)
				else: nondoras.append(c)
		if len(doras)+len(nondoras)<3:
			return

		for i in xrange(min(len(nondoras)+1,4)):
			j=3-i
			if j>len(doras): continue
			yield lockedCards_MINGGANG(doras[0:j]+nondoras[0:i],incomeCard)



class lockedCards_ANGANG(lockedCards_bass):
	def __init__(self,handCards,incomeCard):
		lockedCards_bass.__init__(self,handCards,incomeCard)

	def __str__(self):
		return '%s:%s' % (consts.lockedCardsTypeStrDic[consts.Locked_ANGANG],','.join(map(str,self.handCards)))

	def isMing(self):
		return False

	@staticmethod
	@consts.Dec_NoneToIter
	def getAccessableSilos(player,incomeCard):
		cs=set(player.handCards)
		if incomeCard.incomeType==consts.ZIMO and incomeCard.incomdeFrom==consts.FROM_SELF:
			cs.add(incomeCard.card)

		dic={}
		for c in cs:
			co=c.content
			lst=dic.get(c.content,list())
			lst.append(c)
			dic[c.content]=lst

		for lst in dic.values():
			if len(lst)>=4:
				doras=list();nondoras=list()
				for c in lst:
					if c.dora(): doras.append(c)
					else: nondoras.append(c)
				for i in xrange(min(len(nondoras)+1,5)):
					j=4-i
					if j>len(doras): continue
					yield lockedCards_ANGANG(doras[0:j]+nondoras[0:i],incomeCard)









if __name__=='__main__':
	import cardPackage,player,incomeCard

	cp=cardPackage.cardPackage(seed=None)
	p=player.player()

	cardList=list(cp.shuffleIter())
	indexList=[83,84,55,54,17,18,19,108,109,110,111]
	indexList.sort()
	for i in indexList: p.handCards.add(cardList[i])

	tem=list(p.handCards)
	tem.sort()
	print p

	ic=incomeCard.incomeCard(cardList[91],consts.RIVER,consts.FROM_UPPER)
	print 'Test <income %s>:' % ic
	lc=list(lockedCards_bass.getAccessableSilos(p,ic))
	for i in lc: print i
	lc[0].addToPlayer(p)
	print p
	
	ic=incomeCard.incomeCard(cardList[53],consts.RIVER,consts.FROM_DOWN)
	print 'Test <income %s>:' % ic
	lc=list(lockedCards_bass.getAccessableSilos(p,ic))
	for i in lc: print i
	lc[0].addToPlayer(p)
	print p

	ic=incomeCard.incomeCard(cardList[52],consts.ZIMO,consts.FROM_SELF)
	print 'Test <income %s>:' % ic
	lc=list(lockedCards_bass.getAccessableSilos(p,ic))
	for i in lc: print i
	lc[0].addToPlayer(p)
	print p

	ic=incomeCard.incomeCard(cardList[16],consts.RIVER,consts.FROM_MIDDLE)
	print 'Test <income %s>:' % ic
	lc=list(lockedCards_bass.getAccessableSilos(p,ic))
	for i in lc: print i
	lc[1].addToPlayer(p)
	print p

	ic=incomeCard.incomeCard(cardList[0],consts.ZIMO,consts.FROM_SELF)
	print 'Test <income %s>:' % ic
	p.handCards.add(ic.card)
	print p

	lc=list(lockedCards_bass.getAccessableSilos(p,ic))
	for i in lc: print i
	lc[0].addToPlayer(p)

	ic=incomeCard.incomeCard(cardList[1],consts.ZIMO,consts.FROM_SELF)
	print 'Test <income %s>:' % ic
	p.handCards.add(ic.card)
	print p
	