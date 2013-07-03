# -*- coding: utf-8 -*-

AUTHOR='SakuraSa'
VERSION=(1,0,0,0)
TEMFILE='temFile.tem'

"""
card type
牌类型
"""
PIN=1;SUO=2;MAN=3;WIN=4;DRA=5

PIN1=(PIN,1);PIN2=(PIN,2);PIN3=(PIN,3);PIN4=(PIN,4)
PIN5=(PIN,5);PIN6=(PIN,6);PIN7=(PIN,7);PIN8=(PIN,8);PIN9=(PIN,9)
SUO1=(SUO,1);SUO2=(SUO,2);SUO3=(SUO,3);SUO4=(SUO,4)
SUO5=(SUO,5);SUO6=(SUO,6);SUO7=(SUO,7);SUO8=(SUO,8);SUO9=(SUO,9)
MAN1=(MAN,1);MAN2=(MAN,2);MAN3=(MAN,3);MAN4=(MAN,4)
MAN5=(MAN,5);MAN6=(MAN,6);MAN7=(MAN,7);MAN8=(MAN,8);MAN9=(MAN,9)
EAST=(WIN,1);SOUTH=(WIN,2);WEST=(WIN,3);NORTH=(WIN,4)
HAKU=(DRA,1);GREEN=(DRA,2);CHUN=(DRA,3)

PIN5D=(PIN,5,True);SUO5D=(SUO,5,True);MAN5D=(MAN,5,True)

"""
Green cards
绿色牌
"""
GREENCARDS={
	SUO2,SUO3,SUO4,SUO6,SUO7,GREEN
}

"""
card package type
牌组类型
"""
CARDPACKAGE_DIC={
	'CARDPACKAGE_NOREDDORA':[
		PIN1,PIN2,PIN3,PIN4,PIN5,PIN6,PIN7,PIN8,PIN9,
		PIN1,PIN2,PIN3,PIN4,PIN5,PIN6,PIN7,PIN8,PIN9,
		PIN1,PIN2,PIN3,PIN4,PIN5,PIN6,PIN7,PIN8,PIN9,
		PIN1,PIN2,PIN3,PIN4,PIN5,PIN6,PIN7,PIN8,PIN9,
		SUO1,SUO2,SUO3,SUO4,SUO5,SUO6,SUO7,SUO8,SUO9,
		SUO1,SUO2,SUO3,SUO4,SUO5,SUO6,SUO7,SUO8,SUO9,
		SUO1,SUO2,SUO3,SUO4,SUO5,SUO6,SUO7,SUO8,SUO9,
		SUO1,SUO2,SUO3,SUO4,SUO5,SUO6,SUO7,SUO8,SUO9,
		MAN1,MAN2,MAN3,MAN4,MAN5,MAN6,MAN7,MAN8,MAN9,
		MAN1,MAN2,MAN3,MAN4,MAN5,MAN6,MAN7,MAN8,MAN9,
		MAN1,MAN2,MAN3,MAN4,MAN5,MAN6,MAN7,MAN8,MAN9,
		MAN1,MAN2,MAN3,MAN4,MAN5,MAN6,MAN7,MAN8,MAN9,
		EAST,SOUTH,WEST,NORTH,CHUN,HAKU,GREEN,
		EAST,SOUTH,WEST,NORTH,CHUN,HAKU,GREEN,
		EAST,SOUTH,WEST,NORTH,CHUN,HAKU,GREEN,
		EAST,SOUTH,WEST,NORTH,CHUN,HAKU,GREEN,
	],
	'CARDPACKAGE_3REDDORA':[
		PIN1,PIN2,PIN3,PIN4,PIN5D,PIN6,PIN7,PIN8,PIN9,
		PIN1,PIN2,PIN3,PIN4,PIN5,PIN6,PIN7,PIN8,PIN9,
		PIN1,PIN2,PIN3,PIN4,PIN5,PIN6,PIN7,PIN8,PIN9,
		PIN1,PIN2,PIN3,PIN4,PIN5,PIN6,PIN7,PIN8,PIN9,
		SUO1,SUO2,SUO3,SUO4,SUO5D,SUO6,SUO7,SUO8,SUO9,
		SUO1,SUO2,SUO3,SUO4,SUO5,SUO6,SUO7,SUO8,SUO9,
		SUO1,SUO2,SUO3,SUO4,SUO5,SUO6,SUO7,SUO8,SUO9,
		SUO1,SUO2,SUO3,SUO4,SUO5,SUO6,SUO7,SUO8,SUO9,
		MAN1,MAN2,MAN3,MAN4,MAN5D,MAN6,MAN7,MAN8,MAN9,
		MAN1,MAN2,MAN3,MAN4,MAN5,MAN6,MAN7,MAN8,MAN9,
		MAN1,MAN2,MAN3,MAN4,MAN5,MAN6,MAN7,MAN8,MAN9,
		MAN1,MAN2,MAN3,MAN4,MAN5,MAN6,MAN7,MAN8,MAN9,
		EAST,SOUTH,WEST,NORTH,CHUN,HAKU,GREEN,
		EAST,SOUTH,WEST,NORTH,CHUN,HAKU,GREEN,
		EAST,SOUTH,WEST,NORTH,CHUN,HAKU,GREEN,
		EAST,SOUTH,WEST,NORTH,CHUN,HAKU,GREEN,
	],
	'CARDPACKAGE_4REDDORA':[
		PIN1,PIN2,PIN3,PIN4,PIN5D,PIN6,PIN7,PIN8,PIN9,
		PIN1,PIN2,PIN3,PIN4,PIN5D,PIN6,PIN7,PIN8,PIN9,
		PIN1,PIN2,PIN3,PIN4,PIN5,PIN6,PIN7,PIN8,PIN9,
		PIN1,PIN2,PIN3,PIN4,PIN5,PIN6,PIN7,PIN8,PIN9,
		SUO1,SUO2,SUO3,SUO4,SUO5D,SUO6,SUO7,SUO8,SUO9,
		SUO1,SUO2,SUO3,SUO4,SUO5,SUO6,SUO7,SUO8,SUO9,
		SUO1,SUO2,SUO3,SUO4,SUO5,SUO6,SUO7,SUO8,SUO9,
		SUO1,SUO2,SUO3,SUO4,SUO5,SUO6,SUO7,SUO8,SUO9,
		MAN1,MAN2,MAN3,MAN4,MAN5D,MAN6,MAN7,MAN8,MAN9,
		MAN1,MAN2,MAN3,MAN4,MAN5,MAN6,MAN7,MAN8,MAN9,
		MAN1,MAN2,MAN3,MAN4,MAN5,MAN6,MAN7,MAN8,MAN9,
		MAN1,MAN2,MAN3,MAN4,MAN5,MAN6,MAN7,MAN8,MAN9,
		EAST,SOUTH,WEST,NORTH,CHUN,HAKU,GREEN,
		EAST,SOUTH,WEST,NORTH,CHUN,HAKU,GREEN,
		EAST,SOUTH,WEST,NORTH,CHUN,HAKU,GREEN,
		EAST,SOUTH,WEST,NORTH,CHUN,HAKU,GREEN,
	],
}
for key in CARDPACKAGE_DIC.keys():
	CARDPACKAGE_DIC[key].sort()

"""
Income Type
入手牌类型
"""
ZIMO        = 1       #自摸
RIVER       = 2       #河中
ANGANG      = 3       #暗杠
JIAGANG     = 4       #加杠
LINGSHANG   = 5       #岭上

FROM_SELF   = 1       #自己
FROM_UPPER  = 2       #上家
FROM_MIDDLE = 3       #对家
FROM_DOWN   = 4       #下家

"""
Locked Cards Type
锁定牌类型
"""
Locked_CHI=0
Locked_PENG=1
Locked_JIAGANG=2
Locked_MINGGANG=3
Locked_ANGANG=4

"""
Table sits
玩家位置
"""
loc_EAST=1;loc_SOUTH=2;loc_WEST=3;loc_NORTH=4

"""
Yaku Groups
役组合
"""
yakuGroupDic={
	'YAKUPAKAGE_STANDER':[
		'yaku_lizhi',
		'yaku_ren',
		'yaku_lingshang',
		'yaku_shuanglizhi',
		'yaku_sangangzi',
		'yaku_yiqi',
		'yaku_qingyi',
		'yaku_sigangzi',
		'yaku_duanyao',
		'yaku_qianggang',
		'yaku_qinglaotou',
		'yaku_sanseke',
		'yaku_chunquan',
		'yaku_hundai',
		'yaku_yibei',
		'yaku_ziyise',
		'yaku_sianke',
		'yaku_zimo',
		'yaku_haidi',
		'yaku_hunlaotou',
		'yaku_dasanyuan',
		'yaku_qidui',
		'yaku_yifa',
		'yaku_yipai',
		'yaku_tian',
		'yaku_guoshi',
		'yaku_di',
		'yaku_jiulian',
		'yaku_xiaosixi',
		'yaku_xiaosanyuan',
		'yaku_sanseshun',
		'yaku_pinghu',
		'yaku_hunyi',
		'yaku_sanseshun',
		'yaku_lvyise',
		'yaku_erbei',
	],
}

"""
Localization
本地化信息
"""

from localization import *


"""
Helper Function
帮助函数
"""

def isTypeOf(card,type):
	return card[0]==type
def isSameType(cardA,cardB):
	return cardA[0]==cardB[0]
def isYao(card):
	return isTypeOf(card,WIN) or isTypeOf(card,DRA) or card[1]==1 or card[1]==9
def isNext(cardA,cardB,circle=False):
	if cardA[0]!=cardB[0]: return False
	if cardB[1]-cardA[1]==1: return True
	if circle:
		cl=8 if 1<=cardA[0]<=3 else 3 if cardA[1]==WIN else 2
		return abs(cardA[1]-cardB[1])==cl
	else:
		return False
def isBefor(cardA,cardB,circle=False):
	return isNext(cardB,cardA,circle)
def isRedDora(card):
	return len(card)>2 and card[2]
def getDistance(cardA,cardB):
	return cardA[1]-cardB[1]
def isWindOf(card,loc):
	return isTypeOf(card,WIN) and card[1]==loc
def upInt(num,mod):
	m=num%mod
	if m>0:
		return num-m+mod
	else:
		return num


def Dec_NoneToIter(func):
	def dec_func(*arg):
		tem=func(*arg)
		if tem==None:
			return list()
		else:
			return tem
	return dec_func




if __name__=='__main__':
	print isBefor(SUO2,SUO3);exit(0)

	for key in cardTypeStrDic:
		print key,':',cardTypeStrDic[key]