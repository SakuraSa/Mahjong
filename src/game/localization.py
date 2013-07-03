# -*- coding: utf-8 -*-

from consts import *

"""
Localization
本地化信息
"""

CultureInfo='zh-CHS'


"""
Card Types
牌类型
"""
cardTypeStrDic={
	PIN:'饼',SUO:'索',MAN:'万',WIN:'风',DRA:'元',
	PIN1:'一饼',PIN2:'二饼',PIN3:'三饼',PIN4:'四饼',PIN5:'五饼',
	PIN6:'六饼',PIN7:'七饼',PIN8:'八饼',PIN9:'九饼',
	SUO1:'一索',SUO2:'二索',SUO3:'三索',SUO4:'四索',SUO5:'五索',
	SUO6:'六索',SUO7:'七索',SUO8:'八索',SUO9:'九索',
	MAN1:'一万',MAN2:'二万',MAN3:'三万',MAN4:'四万',MAN5:'五万',
	MAN6:'六万',MAN7:'七万',MAN8:'八万',MAN9:'九万',
	EAST:'东风',SOUTH:'南风',WEST:'西风',NORTH:'北风',
	CHUN:'红中',HAKU:'白板',GREEN:'发财',
	PIN5D:'红五饼',SUO5D:'红五索',MAN5D:'红五万'
}
cardTypeSParseDic={cardTypeStrDic[key]:key for key in cardTypeStrDic.keys()}

"""
Income Type
入手牌类型
"""
incomeCardTypeList=[
	ZIMO,      #自摸
	RIVER,     #河中
	ANGANG,    #暗杠
	JIAGANG,   #加杠
]
incomeCardTypeStrDic={
	ZIMO      : '自摸',
	RIVER     : '河中',
	ANGANG    : '暗杠',
	JIAGANG   : '加杠',
	LINGSHANG : '岭上',
}
incomeCardTypeParseDic={incomeCardTypeStrDic[key]:key for key in incomeCardTypeStrDic.keys()}

incomrCardFromTypeStrDic={
	FROM_SELF    :  '自己',
	FROM_UPPER   :  '上家',
	FROM_MIDDLE  :  '对家',
	FROM_DOWN    :  '下家',
}

"""
Locked Cards Type
锁定牌类型
"""
lockedCardsTypeStrDic={
	Locked_CHI      :  '吃',
	Locked_PENG     :  '碰',
	Locked_JIAGANG  :  '加杠',
	Locked_MINGGANG :  '明杠',
	Locked_ANGANG   :  '暗杠',
}

"""
Player Location
玩家位置
"""
playerLocationTypeStrDic={
	loc_EAST:'东',
	loc_SOUTH:'南',
	loc_WEST:'西',
	loc_NORTH:'北',
}

"""
Yaku Names
役名
"""
yakuNamesStrDic={
	
}