#Define High Number multipliers
U = 1
K = 10 ** 3 #kilo
M = 10 ** 6 #million
B = 10 ** 9 #billion
T = 10 ** 12 #trillion
Q = 10 ** 15 #quadrillion

#Initial Number of Buildings
cursor_num = 0
grandma_num = 1
farm_num = 0
factory_num = 0
mine_num = 0
shipment_num = 0
alchemy_lab_num = 0
portal_num = 0
time_machine_num = 0
antimatter_condenser_num = 0
prism_num = 0

#Parameters
upgrade_multiplier = 2
r = 1.15 #Price multiplier

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
def costsManage(units_to_buy, unit_num, unit):
	if units_to_buy == 0:
		return 0
	elif (unit == "cursor"):
		price = cursor.price * (((r ** (unit_num + units_to_buy + 1)) - (r ** (unit_num))) / (r - 1))
		return price
	elif (unit == "grandma"):
		price = grandma.price * (((r ** (unit_num + units_to_buy + 1)) - (r ** (unit_num))) / (r - 1))
		return price

#Define all type of units
cursor = unit (15, cursor_num, 0.1)
grandma = unit (100, grandma_num, 0.5)
farm = unit (100, grandma_num, 0.5)
factory = unit (100, grandma_num, 0.5)
mine = unit (100, grandma_num, 0.5)
shipment = unit (100, grandma_num, 0.5)
alchemy_lab = unit (100, grandma_num, 0.5)
portal = unit (100, grandma_num, 0.5)
time_machine = unit (100, grandma_num, 0.5)
antimatter_condenser = unit (100, grandma_num, 0.5)
prism = unit (100, grandma_num, 0.5)

#Calculates cps produced by all your units
def absoluteCps():
	return cursor.total_unit_cps() + grandma.total_unit_cps()	

#################################################################
### This function calculates the time spended to buy certain #### 
### number of times the specified unit ##########################
#################################################################
def timeManage(unit, units_to_buy):
	if (unit == "cursor"):
		for unit_num in range(cursor.num, units_to_buy + 1):
			time = 0
			time += costsManage((unit_num - cursor.num), unit_num, unit) / absoluteCps()
			cursor.buy(unit_num - cursor.num)
			#print (unit_num, absoluteCps(), time/60)
	elif (unit == "grandma"):
		for unit_num in range(grandma.num, units_to_buy + 1):
			time = 0
			time += costsManage((unit_num - grandma.num), unit_num, unit) / absoluteCps()
			grandma.buy(unit_num - grandma.num)
			#print (unit_num, absoluteCps(), time/60)

#################################################################
### Faltaria interpretar el gen, convertirlo en una matriz de ### 
### comandos con el tipo de unidad y la cantidad cada vez y #####
### hacer un bucle que pase cada comando por la funcion que #####
### calcula el tiempo que tarda y los sume ######################
#################################################################

#Test
timeManage("grandma", 30)

#################################################################
######################## --MEJORAS-- ############################
### Comprobar si existe switch case en python y como se escribe #
### para cuando tengamos que hacer todos los tipos de unidades, #
### no solo abuelas y cursores ##################################
#################################################################