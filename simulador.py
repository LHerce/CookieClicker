#Define High Number multipliers
U = 1
K = 10 ** 3 #kilo
M = 10 ** 6 #million
B = 10 ** 9 #billion
T = 10 ** 12 #trillion
Q = 10 ** 15 #quadrillion

#Initial Number of Buildings
cursor_num = 2
grandma_num = 0
farm_num = 0
factory_num = 0
mine_num = 0
shipment_num = 0
alchemy_lab_num = 0
portal_num = 0
time_machine_num = 0
antimatter_condenser_num = 0
prism_num =0

#Parameters
upgrade_multiplier = 2
r = 1.15 #Price multiplier
time = 0
type_num = 10 #Number of types of units (there is no prisms yet)
abs_cps = 0

#################################################################
### First it has the initial parameters, the upgrade method ##### 
### changes only production speed, buy just add units and total #
### unit cps calculates the total production. To calculate the ##
### cost of the units we use costsManage function################
#################################################################
class unit:
	def __init__(self, initial_price, initial_num, unit_cps):
		self.price = initial_price
		self.num = initial_num
		self.unit_cps = unit_cps
		self.initial_num = initial_num
	def upgrade(self, upgrade_multiplier):
		self.unit_cps *= upgrade_multiplier
	def buy(self, unit_num):
		self.num += unit_num
	def total_unit_cps(self):
		return self.num * self.unit_cps

#Basic functions

#################################################################
### This function calculates the price of buying the units, #####
###  since the price follows a grometic progression #############
### the formula of the sum of n terms is used here ##############
#################################################################
def costsManage(units_to_buy, unit_num, unit_type):
	if units_to_buy == 0:
		return 0
	else:
		price = Units[unit_type].price * ((r ** (unit_num + units_to_buy)) - (r ** (unit_num))) / (r - 1)
		return price

#Define all type of units

Units = (unit (15*U, cursor_num, 0.1*U), #Cursor
	unit (100*U, grandma_num, 0.5*U), #Grandma
	unit (500*U, farm_num, 4*U), #Farm
	unit (3*K, factory_num, 10*U), #Factory
	unit (10*K, mine_num, 40*U), #Mine
	unit (40*K, shipment_num, 100*U), #Shipment
	unit (200 * K, alchemy_lab_num, 400*U), #Alchemy Lab
	unit (1*M + 666*K + 666*U, portal_num, 6*K + 666*U), #Portal
	unit (123*M + 456*K + 789*U, time_machine_num, 98*K + 765*U), #Time Machine
	unit (3*B + 999*M + 999*K + 999*U, antimatter_condenser_num, 999*K + 999*U), #Antimatter Condenser
	unit (75*B, grandma_num, 10*M)) #Prism  Hay 11 unidades

#Calculates cps produced by all your units
def absoluteCps():
	cps = 0
	for i in range(type_num):
		cps += Units[i].total_unit_cps()
	return cps

#################################################################
### This function calculates the time spended to buy certain #### 
### number of times the specified unit ##########################
#################################################################

def timeManage(unit_type, units_to_buy):
	price = costsManage(1, Units[unit_type].initial_num - 1, unit_type)
	time = 0
	for unit_num in range(Units[unit_type].num, units_to_buy + Units[unit_type].num):
		unit_num += 1
		price *= 1.15
		time += price / absoluteCps()
		Units[unit_type].buy(unit_num - Units[unit_type].num)
	return time

#################################################################		
### This function crecieves a matrix with the type of unit and ## 
### the number you want to buy and calculates the time it takes #
#################################################################

def genTime(comands, time):
	for i in range(len(comands)):
		time += timeManage (comands[i][0], comands[i][1])
	return time

#################################################################
### Faltaria interpretar el gen y convertirlo ###################
### en la matriz de comandos ####################################
#################################################################

#Test
comands = [[0, 2],[1, 2],[2,5],[5,1]]
print(genTime(comands, time))