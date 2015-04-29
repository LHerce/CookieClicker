#Define High Number multipliers
U = 1
K = 10 ** 3 #kilo
M = 10 ** 6 #million
B = 10 ** 9 #billion
T = 10 ** 12 #trillion
Q = 10 ** 15 #quadrillion

#Initial Number of Buildings
cursor_num = 0
grandma_num = 0
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
#################################################################
### First it has the initial parameters, the upgrade method ##### 
### changes only production speed, buy just add units and total #
### unit cps calculates the total production. To calculate the ##
### cost of the units we use costsManage function################
#################################################################
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
def costsManage(units_to_buy, unit_num):
	if units_to_buy == 0:
		return 0
	price = initial_price * (((r ** (unit_num + units_to_buy + 1)) - (r ** (unit_num))) / (r - 1))
	return price

cursor = unit (15, cursor_num, 0.1)
grandma = unit (100, grandma_num, 0.5)

#Test
print(cursor1.__dict__)
