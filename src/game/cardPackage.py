# -*- coding: utf-8 -*-

import random
import card,consts

class cardPackage(object):
	def __init__(self,packageName='CARDPACKAGE_NOREDDORA',seed=consts.AUTHOR):
		self.cardPool=set()
		self.seed=seed
		idCounter=0;
		for content in consts.CARDPACKAGE_DIC[packageName]:
			self.cardPool.add(card.card(content,idCounter))
			idCounter+=1

	def allCards(self):
		for c in self.cardPool:
			yield c

	def dora(self,pointer=set()):
		doraCounter=0
		for c in self.allCards:
			doraCounter+=c.dora(pointer)
		return doraCounter


	def getCardByID(self,id):
		return self.cardPool[id]

	def shuffleIter(self):
		temList=list(self.cardPool)
		indexList=range(len(self.cardPool))
		if self.seed!=None:
			random.Random(self.seed).shuffle(indexList)

		for i in indexList:
			yield temList[i]

	"""
    prefix char:
    S -> SUO    e -> EAST   h -> HAKU   R -> REDDORA
    P -> PIN    s -> SOUTH  g -> GREEN
    M -> MAN    w -> WEST   c -> CHUN
                n -> NORTH
    """
	@staticmethod
	def QToString(cardSet):
		stringBulider=list()

		hashTable=dict()
		for c in cardSet:
			h=c.content[0]
			lst=hashTable.get(h,list())
			lst.append(c)
			hashTable[h]=lst

		if consts.SUO in hashTable:
			lst=hashTable[consts.SUO]
			lst.sort()
			stringBulider.append('S')
			for c in lst:
				if c.isRedDora():
					stringBulider.append('R')
				stringBulider.append(str(c.content[1]))
		if consts.PIN in hashTable:
			lst=hashTable[consts.PIN]
			lst.sort()
			stringBulider.append('P')
			for c in lst:
				if c.isRedDora():
					stringBulider.append('R')
				stringBulider.append(str(c.content[1]))
		if consts.MAN in hashTable:
			lst=hashTable[consts.MAN]
			lst.sort()
			stringBulider.append('M')
			for c in lst:
				if c.isRedDora():
					stringBulider.append('R')
				stringBulider.append(str(c.content[1]))
		if consts.WIN in hashTable:
			lst=hashTable[consts.WIN]
			lst.sort()
			for c in lst:
				if c.isRedDora():
					stringBulider.append('R')
				if c.content[0:2]==consts.EAST:
					stringBulider.append('e')
				elif c.content[0:2]==consts.SOUTH:
					stringBulider.append('s')					
				elif c.content[0:2]==consts.WEST:
					stringBulider.append('w')
				elif c.content[0:2]==consts.NORTH:
					stringBulider.append('n')
		if consts.DRA in hashTable:
			lst=hashTable[consts.DRA]
			lst.sort()
			for c in lst:
				if c.isRedDora():
					stringBulider.append('R')
				if c.content[0:2]==consts.HAKU:
					stringBulider.append('h')
				elif c.content[0:2]==consts.GREEN:
					stringBulider.append('g')					
				elif c.content[0:2]==consts.CHUN:
					stringBulider.append('c')

		return ''.join(stringBulider)

	@staticmethod
	def QParse(QString):
		tem=list()

		TypePrefix=consts.SUO;DoraPrefix=False
		for c in QString:
			if   c == 'S':
				TypePrefix=consts.SUO
				continue
			elif c == 'P':
				TypePrefix=consts.PIN
				continue
			elif c == 'M':
				TypePrefix=consts.MAN
				continue
			elif c == 'R':
				DoraPrefix=True
				continue
			else:
				ct=None
				if c == 'e':
					ct=list(consts.EAST)
				elif c == 's' :
					ct=list(consts.SOUTH)
				elif c == 'w' :
					ct=list(consts.WEST)
				elif c == 'n' :
					ct=list(consts.NORTH)
				elif c == 'h' :
					ct=list(consts.HAKU)
				elif c == 'g' :
					ct=list(consts.GREEN)
				elif c == 'c' :
					ct=list(consts.CHUN)
				elif c.isdigit():
					n=int(c)
					if 1 <= n <= 9:
						ct=list((TypePrefix,n))

				if ct==None:
					raise Exception('Unexpected char : '+c)

				if DoraPrefix:
					ct.append(True)
					DoraPrefix=False
				tem.append(tuple(ct))

		cardSet=set()
		VCounter=0
		for c in tem:
			VCounter-=1
			cardSet.add(card.card(c,VCounter))

		return cardSet




if __name__=='__main__':
	cp=cardPackage(packageName='CARDPACKAGE_4REDDORA',seed=None)

	for c in cp.shuffleIter():
		print '%03d'%c.id,'\t',c
