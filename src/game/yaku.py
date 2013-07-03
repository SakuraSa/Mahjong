# -*- coding: utf-8 -*-

import consts,card,player,lockedCards

class yaku_manager:
	def __init__(self,packageName='YAKUPAKAGE_STANDER'):
		self.yakus=None
		self.load(packageName)

	def load(self,packageName):
		package=set(consts.yakuGroupDic[packageName])
		self.yakus=set()

		for y in yaku_manager.__allYaku__:
			if y.name in package:
				package.discard(y.name)
				self.yakus.add(y)

		if package:
			raise Exception('Unexcepted yaku name: ' + ','.join(package))


	__allYaku__ = set()
	@staticmethod
	def Register(yaku):
		yaku_manager.__allYaku__.add(yaku)
		return yaku


class cards_struct(object):
	"""
	cards struct base fu
	"""
	mingKe    = 2
	anKe      = 4
	mingGang  = 8
	anGang    = 16

	def __init__(self,cards):
		self.cards=cards

	def __getitem__(self,index):
		return self.cards[index]

	def __str__(self):
		tem=list()
		for c in self.cards:
			tem.append(str(c))
		return ','.join(tem)

	def __hash__(self):
		counter=0
		for c in self.cards:
			counter+=hash(c.content)+hash(c.id)
		return hash(counter)

	def __eq__(self,target):
		return self.__hash__()==target.__hash__()

	def fu(self):
		return 0

	@staticmethod
	def getCardsStructFromLockedCards(lCards):
		cards=list(lCards.allCards())
		if isinstance(cards,lockedCards.lockedCards_CHI):
			return cards_struct_seq(cards)
		elif isinstance(cards,lockedCards.lockedCards_PENG):
			return cards_struct_tri(cards,cards_struct.mingke)
		elif isinstance(cards,lockedCards.lockedCards_JIAGANG):
			return cards_struct_tri(cards,cards_struct.mingGang)
		elif isinstance(cards,lockedCards.lockedCards_MINGGANG):
			return cards_struct_tri(cards,cards_struct.mingGang)
		elif isinstance(cards,lockedCards.lockedCards_ANGANG):
			return cards_struct_tri(cards,cards_struct.anGang)
		return None

class cards_struct_pair(cards_struct):
	
	def __init__(self,pair):
		cards_struct.__init__(self,pair)

	def fu(self):
		return 2 if self.cards[0].isYao() else 0

	@staticmethod
	def getCardsStruct(cardSet):
		if len(cardSet)<2:
			return None
		pairs=dict()
		for c in cardSet:
			if c.content in pairs:
				return cards_struct_pair((pairs[c.content],c))
			else:
				pairs[c.content]=c
		return None

class cards_struct_tri(cards_struct):

	def __init__(self,tri,ming=4):
		cards_struct.__init__(self,tri)
		self.ming=ming

	def fu(self):
		return self.ming*2 if self.cards[0].isYao() else self.ming

	@staticmethod
	def getCardsStruct(cardSet):
		if len(cardSet)<3:
			return None
		pairs=dict()
		for c in cardSet:
			if c.content in pairs:
				lst=pairs[c.content]
				lst.append(c)
				if len(lst)>=3:
					return cards_struct_tri(tuple(lst))
			else:
				pairs[c.content]=list((c,))

class cards_struct_seq(cards_struct):

	def __init__(self,seq,ming=cards_struct.anKe):
		cards_struct.__init__(self,seq)

	def fu(self):
		return 0

	@staticmethod
	def getSeq(cardSet,centerCard):
		bf=None;nx=None
		for c in cardSet:
			if bf==None and c.isNextOf(centerCard):
				bf=c
			elif nx==None and c.isBeforOf(centerCard):
				nx=c
			if bf!=None!=nx:
				return cards_struct_seq((nx,centerCard,bf))
		return None

	@staticmethod
	def getCardsStruct(cardSet):
		if len(cardSet)<3:
			return None
		for c in cardSet:
			if not c.isShu():
				continue
			tem=cards_struct_seq.getSeq(cardSet,c)
			if tem!=None:
				return tem
		return None




class yaku_struct(object):
	name='base'

	def __init__(self,player,incomeCard):
		self.player=player
		self.incomeCard=incomeCard

	def __str__(self):
		tem=list(self.player.handCards)
		tem.append(self.incomeCard.card)
		tem.sort()
		tem.append(self.name)
		return ','.join(map(str,tem))

	def __hash__(self):
		counter=hash(type(self))
		for c in self.allCards():
			counter+=hash(c.content)
		return hash(counter)

	def __eq__(self,target):
		return self.__hash__()==target.__hash__()

	def AllCards(self):
		for c in self.player.allCards():
			yield c
		yield self.incomeCard.card

	def fu(self):
		return 0

	@staticmethod
	@consts.Dec_NoneToIter
	def getAccessableSilos(player,incomeCard):
		hashtable=set()
		for i in yaku_struct_normal.getAccessableSilos(player,incomeCard):
			h=hash(i)
			if not h in hashtable:
				hashtable.add(h)
				yield i
		for i in yaku_struct_7pairs.getAccessableSilos(player,incomeCard):
			h=hash(i)
			if not h in hashtable:
				hashtable.add(h)
				yield i
		for i in yaku_struct_musou.getAccessableSilos(player,incomeCard):
			h=hash(i)
			if not h in hashtable:
				hashtable.add(h)
				yield i


class yaku_struct_normal(yaku_struct):
	name='normal'

	def __init__(self,player,incomeCard,pairs,mians):
		yaku_struct.__init__(self,player,incomeCard)
		self.pairs=pairs
		self.mians=mians

	def __str__(self):
		tem=list()
		tem.append('[%s]'%str(self.pairs))
		for s in self.mians:
			tem.append('[%s]'%str(s))
		return ''.join(tem)

	def __hash__(self):
		counter=hash(self.pairs)
		for m in self.mians:
			counter+=hash(m)
		return hash(counter)

	def fu(self):
		fuCounter=20
		fuCounter+=self.pairs.fu()
		if self.pairs.cards[0].isTypeOf(consts.DRA):
			fuCounter+=2
		else:
			if self.pairs.cards[0].isWindOf(self.player.wind_self):
				fuCounter+=2
			if self.pairs.cards[0].isWindOf(self.player.wind_game):
				fuCounter+=2
		for m in self.mians:
			fuCounter+=m.fu()
		fuCounter+=self.getIncomeFan()

		return consts.upInt(fuCounter,10)

	def getIncomeFan(self):

		fuCounter=0

		"""
		自摸
		"""
		if self.incomeCard.incomdeFrom==consts.FROM_SELF:
			fuCounter+=2

		"""
		单碰
		"""
		if self.incomeCard.card in self.pairs.cards:
			return 2+fuCounter

		m=None
		for i in self.mians:
			if not isinstance(i,cards_struct_seq):
				continue
			if self.incomeCard.card in i.cards:
				m=i
				break
		if m!=None:
			"""
			嵌张
			"""
			if m.cards[1]==self.incomeCard.card:
				return 2+fuCounter
			"""
			边张
			"""
			if m.cards[0]==self.incomeCard.card and self.incomeCard.card.content[1]==7:
				return 2+fuCounter
			if m.cards[2]==self.incomeCard.card and self.incomeCard.card.content[1]==3:
				return 2+fuCounter
			"""
			其他
			"""
		return fuCounter

	@staticmethod
	@consts.Dec_NoneToIter
	def getAccessableSilos(player,incomeCard):
		s=searcher(player,incomeCard)
		for i in s.searchAll():
			yield i

class searcher:
	def __init__(self,player,incomeCard):
		self.player=player
		self.incomeCard=incomeCard

	def init(self):
		self.cardSet=set(self.player.handCards)
		self.cardSet.add(self.incomeCard.card)
		self.pairs=None
		self.mians=set()
		for i in self.player.lockedCards:
			self.mians.append(cards_struct.getCardsStructFromLockedCards(i))

	def searchAll(self):
		resLst=list()
		self.init()

		#search deeper
		for i in xrange(3):
			self.search(i,resLst)

			print 'XXX   :',','.join(map(str,self.cardSet))

		return resLst


	def search(self,go,resLst):
		#print 'go    :',go
		#print 'pairs :',self.pairs
		#print 'mians :',';'.join(map(str,self.mians))
		#print 'cardS :',','.join(map(str,self.cardSet))

		if self.pairs!=None and len(self.mians)==4:
			resLst.append(yaku_struct_normal(self.player,self.incomeCard,self.pairs,set(self.mians)))

		p=None
		if go==0 and self.pairs==None:
			p=cards_struct_pair.getCardsStruct(self.cardSet)
			if p:
				self.pairs=p;#print 'add pair:',p
		elif len(self.mians)<4:
			if go==1:
				p=cards_struct_tri.getCardsStruct(self.cardSet)
				if p:
					self.mians.add(p);#print 'add tri:',p
			elif go==2:
				p=cards_struct_seq.getCardsStruct(self.cardSet)
				if p:
					self.mians.add(p);#print 'add seq:',p
		if p==None:
			return

		#update
		for c in p.cards:
			self.cardSet.discard(c)

		#search deeper
		for i in xrange(3):
			self.search(i,resLst)

		#redo
		for c in p.cards:
			self.cardSet.add(c)
		if go==0:
			self.pairs=None
		else:
			self.mians.discard(p)

		return



class yaku_struct_7pairs(yaku_struct):
	name='7pairs'

	def __init__(self,player,incomeCard):
		yaku_struct.__init__(self,player,incomeCard)

	def fu(self):
		return 25

	@staticmethod
	@consts.Dec_NoneToIter
	def getAccessableSilos(player,incomeCard):
		cardSet=set((incomeCard.card.content,))
		cardCounter=0
		for card in player.handCards:
			if card.content in cardSet:
				cardSet.discard(card.content)
				cardCounter+=1
			else:
				cardSet.add(card.content)

		if cardCounter==7 and len(cardSet)==0:
			yield yaku_struct_7pairs(player,incomeCard)

class yaku_struct_musou(yaku_struct):
	name='musou'

	def __init__(self,player,incomeCard):
		yaku_struct.__init__(self,player,incomeCard)

	def fu(self):
		return 25

	@staticmethod
	@consts.Dec_NoneToIter
	def getAccessableSilos(player,incomeCard):
		if not incomeCard.card.isYao():
			return
		cardSet=set(incomeCard.card.content)
		cardCounter=1
		for c in player.handCards:
			if not c.isYao():
				return
			cardSet.add(c.content)
			cardCounter+=1

		if cardCounter==14 and len(cardSet)==13:
			yield yaku_struct_musou(player,incomeCard)













class yaku(object):
	name='yaku'
	structDependency=None
	menqingDependency=False
	shixia=False
	baseFan=0

	def __init__(self,player,incomeCard,cardsStruct):
		self.player=player
		self.incomeCard=incomeCard
		self.cardsStruct=cardsStruct

	def __str__(self):
		return self.name

	def fan(self):
		if self.shixia and self.player.isMing():
			return self.baseFan-1
		else:
			return self.baseFan

	def fu(self):
		self.cardsStruct.fu()

	@staticmethod
	def isMatch(player,incomeCard,cardsStruct):
		"""
		Ming check
		"""
		if self.menqingDependency and player.isMing():
			return False
		"""
		structDependency check
		"""
		if self.structDependency:
			for t in self.structDependency:
				if not isinstance(t,cardsStruct):
					return False

		return True

"""
特殊：宝牌
"""

"""
一番：立直
"""
@yaku_manager.Register
class yaku_lizhi(yaku):
	name='yaku_lizhi'
	menqingDependency=True
	baseFan=1

	@staticmethod
	@consts.Dec_NoneToIter
	def isMatch(player,incomeCard,cardsStruct):
		if not yaku.isMatch(player,incomeCard,cardsStruct):
			return

		if player.richiTurn>0 and not player.wRichi:
			yield yaku_lizhi(player,incomeCard,cardsStruct)

"""
一番：一发
"""
@yaku_manager.Register
class yaku_yifa(yaku):
	name='yaku_yifa'
	menqingDependency=True
	baseFan=1

	@staticmethod
	@consts.Dec_NoneToIter
	def isMatch(player,incomeCard,cardsStruct):
		if not yaku.isMatch(player,incomeCard,cardsStruct):
			return

		if incomeCard.yifaTurn:
			yield yaku_yifa(player,incomeCard,cardsStruct)

"""
一番：岭上
"""
@yaku_manager.Register
class yaku_lingshang(yaku):
	name='yaku_lingshang'
	baseFan=1

	@staticmethod
	@consts.Dec_NoneToIter
	def isMatch(player,incomeCard,cardsStruct):
		if not yaku.isMatch(player,incomeCard,cardsStruct):
			return

		if incomeCard.incomeType==consts.LINGSHANG and incomeCard.incomdeFrom==FROM_SELF:
			yield yaku_lingshang(player,incomeCard,cardsStruct)


"""
一番：自摸
"""
@yaku_manager.Register
class yaku_zimo(yaku):
	name='yaku_zimo'
	menqingDependency=True
	baseFan=1

	@staticmethod
	@consts.Dec_NoneToIter
	def isMatch(player,incomeCard,cardsStruct):
		if not yaku.isMatch(player,incomeCard,cardsStruct):
			return

		if not incomeCard.incomdeFrom==FROM_SELF:
			return
		if incomeCard.incomeType==consts.ZIMO or incomeCard.incomeType==consts.LINGSHANG:
			yield yaku_zimo(player,incomeCard,cardsStruct)

"""
一番：抢杠
"""
@yaku_manager.Register
class yaku_qianggang(yaku):
	name='yaku_qianggang'
	baseFan=1

	@staticmethod
	@consts.Dec_NoneToIter
	def isMatch(player,incomeCard,cardsStruct):
		if not yaku.isMatch(player,incomeCard,cardsStruct):
			return

		if incomeCard.incomdeFrom==FROM_SELF:
			return
		if isinstance(cardsStruct,yaku_struct_musou):
			if not( incomeCard.incomeType==consts.ANGANG or incomeCard.incomeType==consts.JIAGANG ):
				return
		else:
			if not incomeCard.incomeType==consts.JIAGANG:
				return

		yield yaku_qianggang(player,incomeCard,cardsStruct)

"""
一番：海底&河底
"""
@yaku_manager.Register
class yaku_haidi(yaku):
	name='yaku_haidi'
	baseFan=1

	def __str__(self):
		if incomeCard.incomdeFrom==consts.FROM_SELF:
			return 'yaku_haidi'
		else:
			return 'yaku_hedi'

	@staticmethod
	@consts.Dec_NoneToIter
	def isMatch(player,incomeCard,cardsStruct):
		if not yaku.isMatch(player,incomeCard,cardsStruct):
			return

		if incomeCard.haidiTurn:
			yield yaku_haidi(player,incomeCard,cardsStruct)

"""
一番：平和
"""
@yaku_manager.Register
class yaku_pinghu(yaku):
	name='yaku_pinghu'
	structDependency=[yaku_struct_normal]
	menqingDependency=True
	baseFan=1

	def fu(self):
		return 20

	@staticmethod
	@consts.Dec_NoneToIter
	def isMatch(player,incomeCard,cardsStruct):
		if not yaku.isMatch(player,incomeCard,cardsStruct):
			return

		for m in cardsStruct.mians:
			if not isinstance(m,cards_struct_seq):
				return

		f=cardsStruct.getIncomeFan()
		if incomeCard.incomdeFrom==consts.FROM_SELF:
			f-=2

		if f==0:
			yield yaku_pinghu(player,incomeCard,cardsStruct)



"""
一番：断幺
"""
@yaku_manager.Register
class yaku_duanyao(yaku):
	name='yaku_duanyao'
	baseFan=1

	@staticmethod
	@consts.Dec_NoneToIter
	def isMatch(player,incomeCard,cardsStruct):
		if not yaku.isMatch(player,incomeCard,cardsStruct):
			return

		if incomeCard.card.isYao():
			return
		for c in player.allCards():
			if c.isYao():
				return

		yield yaku_duanyao(player,incomeCard,cardsStruct)

"""
一番：一杯口
"""
@yaku_manager.Register
class yaku_yibei(yaku):
	name='yaku_yibei'
	structDependency=[yaku_struct_normal]
	menqingDependency=True
	baseFan=1

	@staticmethod
	@consts.Dec_NoneToIter
	def isMatch(player,incomeCard,cardsStruct):
		if not yaku.isMatch(player,incomeCard,cardsStruct):
			return

		hashtable=dict()
		for m in cardsStruct.mians:
			if not isinstance(m,cards_struct_seq):
				continue
			h=hash(m.cards[0].content[0:2])
			hashtable[h]=hashtable.get(h,0)+1

		getPair=0
		for i in hashtable.values():
			if i==2:
				getPair+=1

		if getPair==1:
			yield yaku_yibei(player,incomeCard,cardsStruct)

"""
一番：自风&场风&役牌
"""
@yaku_manager.Register
class yaku_yipai(yaku):
	name='yaku_yipai'
	structDependency=[yaku_struct_normal]
	baseFan=1

	def __init__(self,player,incomeCard,cardsStruct,criticalCard):
		yaku.__init__(self,player,incomeCard,cardsStruct)
		self.criticalCard=criticalCard

	def __str__(self):
			if c.isWindOf(player.wind_self):
				return 'yaku_zifeng'
			elif c.isWindOf(player.wind_game):
				return 'yaku_changfeng'
			elif c.isTypeOf(consts.DRA):
				t=c.content[0:2]
				if t==consts.HAKU:
					return 'yaku_fanpai_HAKU'
				elif t==consts.GREEN:
					return 'yaku_fanpai_GREEN'
				elif t==consts.CHUN:
					return 'yaku_fanpai_CHUN'

	@staticmethod
	@consts.Dec_NoneToIter
	def isMatch(player,incomeCard,cardsStruct):
		if not yaku.isMatch(player,incomeCard,cardsStruct):
			return

		for m in cardsStruct.mians:
			if not isinstance(m,cards_struct_tri):
				continue
			c=m.cards[0]
			if c.isWindOf(player.wind_self):
				yield yaku_yipai(player,incomeCard,cardsStruct,c)
			elif c.isWindOf(player.wind_game):
				yield yaku_yipai(player,incomeCard,cardsStruct,c)
			elif c.isTypeOf(consts.DRA):
				yield yaku_yipai(player,incomeCard,cardsStruct,c)



"""
二番：三色同顺
"""
@yaku_manager.Register
class yaku_sanseshun(yaku):
	name='yaku_sanseshun'
	structDependency=[yaku_struct_normal]
	shixia=True
	baseFan=2

	@staticmethod
	@consts.Dec_NoneToIter
	def isMatch(player,incomeCard,cardsStruct):
		if not yaku.isMatch(player,incomeCard,cardsStruct):
			return

		hashtable=dict()
		for m in cardsStruct.mians:
			if not isinstance(m,cards_struct_seq):
				continue
			h=hash(m.cards[0].content[1])
			hashtable.get(h,list()).append(m)

		for lst in hashtable.values():
			if len(lst)<3:
				continue

			typeSet=set()
			for m in lst:
				typeSet.add(m.cards[0].content[0])

			if len(typeSet)>=3:
				yield yaku_sanseshun(player,incomeCard,cardsStruct) 

"""
二番：一气
"""
@yaku_manager.Register
class yaku_yiqi(yaku):
	name='yaku_yiqi'
	structDependency=[yaku_struct_normal]
	shixia=True
	baseFan=2

	@staticmethod
	@consts.Dec_NoneToIter
	def isMatch(player,incomeCard,cardsStruct):
		if not yaku.isMatch(player,incomeCard,cardsStruct):
			return

		hashtable=dict()
		for m in cardsStruct.mians:
			if not isinstance(m,cards_struct_seq):
				continue
			h=hash(m.cards[0].content[0])
			hashtable.get(h,list()).append(m)

		for lst in hashtable.values():
			if len(lst)<3:
				continue

			typeSet=set((1,3,7))
			for m in lst:
				typeSet.discard(m.cards[0].content[1])

			if len(typeSet)==0:
				yield yaku_yiqi(player,incomeCard,cardsStruct) 

"""
二番：混全带幺
"""
@yaku_manager.Register
class yaku_hundai(yaku):
	name='yaku_hundai'
	structDependency=[yaku_struct_normal]
	shixia=True
	baseFan=2

"""
二番：七对子
"""
@yaku_manager.Register
class yaku_qidui(yaku):
	name='yaku_qidui'
	structDependency=[yaku_struct_7pairs]
	baseFan=2

"""
二番：三暗刻
"""
@yaku_manager.Register
class yaku_sanseshun(yaku):
	name='yaku_sanseshun'
	structDependency=[yaku_struct_normal]
	baseFan=2

"""
二番：三杠子
"""
@yaku_manager.Register
class yaku_sangangzi(yaku):
	name='yaku_sangangzi'
	structDependency=[yaku_struct_normal]
	baseFan=2

"""
二番：三色同刻
"""
@yaku_manager.Register
class yaku_sanseke(yaku):
	name='yaku_sanseke'
	structDependency=[yaku_struct_normal]
	baseFan=2

"""
二番：混老头
"""
@yaku_manager.Register
class yaku_hunlaotou(yaku):
	name='yaku_hunlaotou'
	structDependency=[yaku_struct_normal]
	baseFan=2

"""
二番：小三元
"""
@yaku_manager.Register
class yaku_xiaosanyuan(yaku):
	name='yaku_xiaosanyuan'
	structDependency=[yaku_struct_normal]
	baseFan=2

"""
二番：双立直
"""
@yaku_manager.Register
class yaku_shuanglizhi(yaku):
	name='yaku_shuanglizhi'
	menqingDependency=True
	baseFan=2

"""
三番：混一色
"""
@yaku_manager.Register
class yaku_hunyi(yaku):
	name='yaku_hunyi'
	shixia=True
	baseFan=3

"""
三番：纯全带幺
"""
@yaku_manager.Register
class yaku_chunquan(yaku):
	name='yaku_chunquan'
	structDependency=[yaku_struct_normal]
	shixia=True
	baseFan=3

"""
三番：二杯口
"""
@yaku_manager.Register
class yaku_erbei(yaku):
	name='yaku_erbei'
	structDependency=[yaku_struct_normal]
	menqingDependency=True
	baseFan=3

"""
六番：清一色
"""
@yaku_manager.Register
class yaku_qingyi(yaku):
	name='yaku_qingyi'
	shixia=True
	baseFan=6

"""
役满：国士无双
"""
@yaku_manager.Register
class yaku_guoshi(yaku):
	name='yaku_guoshi'
	structDependency=[yaku_struct_musou]
	menqingDependency=True
	baseFan=13

"""
役满：四暗刻
"""
@yaku_manager.Register
class yaku_sianke(yaku):
	name='yaku_sianke'
	structDependency=[yaku_struct_normal]
	menqingDependency=True
	baseFan=13

"""
役满：大三元
"""
@yaku_manager.Register
class yaku_dasanyuan(yaku):
	name='yaku_dasanyuan'
	structDependency=[yaku_struct_normal]
	baseFan=13

"""
役满：小四喜
"""
@yaku_manager.Register
class yaku_xiaosixi(yaku):
	name='yaku_xiaosixi'
	structDependency=[yaku_struct_normal]
	baseFan=13

"""
役满：字一色
"""
@yaku_manager.Register
class yaku_ziyise(yaku):
	name='yaku_ziyise'
	baseFan=13

"""
役满：绿一色
"""
@yaku_manager.Register
class yaku_lvyise(yaku):
	name='yaku_lvyise'
	baseFan=13

"""
役满：清老头
"""
@yaku_manager.Register
class yaku_qinglaotou(yaku):
	name='yaku_qinglaotou'
	structDependency=[yaku_struct_normal]
	baseFan=13

"""
役满：九莲宝灯
"""
@yaku_manager.Register
class yaku_jiulian(yaku):
	name='yaku_jiulian'
	structDependency=[yaku_struct_normal]
	menqingDependency=True

"""
役满：四杠子
"""
@yaku_manager.Register
class yaku_sigangzi(yaku):
	name='yaku_sigangzi'
	structDependency=[yaku_struct_normal]
	baseFan=13

"""
役满：天和
"""
@yaku_manager.Register
class yaku_tian(yaku):
	name='yaku_tian'
	menqingDependency=True
	baseFan=13

"""
役满：地和
"""
@yaku_manager.Register
class yaku_di(yaku):
	name='yaku_di'
	menqingDependency=True
	baseFan=13

"""
役满：人和
"""
@yaku_manager.Register
class yaku_ren(yaku):
	name='yaku_ren'
	menqingDependency=True
	baseFan=13



if __name__ == '__main__':
	from cardPackage import *
	from incomeCard import *
	from time import time

	ym=yaku_manager(packageName='YAKUPAKAGE_STANDER')
	pl=player.player()
	pl.handCards=cardPackage.QParse('S1234564567899')

	im=incomeCard(cardPackage.QParse('S9').pop(),consts.ZIMO,consts.FROM_SELF)
	lst=list(yaku_struct.getAccessableSilos(pl,im))

	print pl,im

	if lst:
		for i in lst:
			print i,i.fu(),i.getIncomeFan()
			print cardPackage.QToString(i.AllCards())