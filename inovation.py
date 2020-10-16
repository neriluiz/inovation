#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  innovation.py
#  
#  Copyright 2014 Neri Luiz von Holleben <neri_luiz@yahoo.com.br>
#  12/2014

""" 
	"Inovação implica sempre a geração de valor."(José Paulo)
	Uma emprese deve ganhar mais do que ganharia se mantivesse o dinheiro 
	aplicado a juros num banco. No Brasil o empresário banca apenas um 
	quinto da pesquisa brasileira, os outro quatro quintos são bancados 
	pelo Estado. Na Coreia do Sul (2,2% da economia mundial), o empresá-rio
	banca 80% da produção científica. Com menos habitantes e uma economia
	menor, fica à frente do Brasil em todas as listas de produção científica
	e inovação. Na internet existe um 'manual de inovação", que é conhe-
	cido como Manual de Oslo (2005 por OCDE).
"""

def lucro_inov(a,b,R,D):
	# Lucro devido a inovação:
	# L: lucro (gain/profit), D: despesa (expenditure/cost), R: receita (revenue)
	# a e b are factors that increase when there is innovation
	L = a*R - D/b
	if 0 < a < 1 and b > 1:
		return 'Both revenue and expenditure must decrease. '\
		+'The profit in case of revenue of '+str(R)+' and expenditure of '\
		+str(D) + ' is ' + str(L)  
	elif a == 1 and b > 1:
		return 'Tne revenues stay the same and expenditure decrease. Good!'\
		+'The profit in case of revenue of '+str(R)+' and expenditure of '\
		+str(D) + ' is ' + str(L) 
	elif a > 1 and b > 1:
		return 'The revenues increase and expenditure decrease. Great!'\
		+'The profit in case of revenue of '+str(R)+' and expenditure of '\
		+str(D) + ' is ' + str(L)
	elif a > 1 and b == 1:
		return 'The revenues increase and expenditure stay the same.'\
		+'The profit in case of revenue of '+str(R)+' and expenditure of '\
		+str(D) + ' is ' + str(L)
	elif a > 1 and 0 < b <1:
		return 'The revenues increase but expenditure increase too.'+"\n"
		+'This is a common type of innovation.'\
		+'The profit in case of revenue of '+str(R)+' and expenditure of '\
		+str(D) + ' is ' + str(L)
	elif 0 < a < 1 and 0 < b < 1:
		return 'The revenue decrease and the expenditures increase. \
		This is not a innovation, but a desaster.'\
		+'The profit in case of revenue of '+str(R)+' and expenditure of '\
		+str(D) + ' is ' + str(L)

print lucro_inov(0.5,2  ,4,4)
print lucro_inov(1  ,2  ,4,4)
print lucro_inov(2  ,2  ,4,4)
print lucro_inov(2  ,1  ,4,4)
print lucro_inov(2  ,0.5,4,4)
print lucro_inov(0.5,0.5,4,4)
