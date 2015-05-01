import matplotlib.pyplot as plt

#Define High Number multipliers
K=10**3 #kilo
M=10**6 #million
B=10**9 #billion
T=10**12 #trillion
Q=10**15 #quadrillion

#Define parameters
#Cps=Cookies per second
initial_price = 75 * B
r = 1.15 #price multiplier, common ratio of the geometric progression
upgrade_price = 3.75 * Q
initial_cps = 28.635 * B #'billions'
time = 0
times = []
upgrade_multiplier = 2
initial_num = 50
final_num = 100
initial_cps_unitA = 465.333 * M #'millions'
initial_level = 1
numbers = []

###################################################################
####### The class Units represent de units you want to upgrade ####
####### num: number of units, u_cps: cps per unit, level: #########
####### number of upgrades you've already bought ##################
###################################################################

class Units(object):
	def __init__(self, name, num, u_cps, level):
		self.type = name
		self.num = num
		self.u_cps = u_cps * level * upgrade_multiplier
		self.tu_cps = u_cps * num
		self.level = level
	def upgrade(self):
		self.u_cps *= upgrade_multiplier
		self.tu_cps *= upgrade_multiplier
	def buy(self, u_num):
		self.num += u_num
		self.tu_cps = self.u_cps * self.num


UnitsA = Units("unitsA", initial_num, initial_cps_unitA, initial_level)

###################################################################
####### This function calculates the price of buying the units, ###
#######  since the price follows a grometic progression ###########
####### the formula of the sum of n terms is used here ############
###################################################################
def costsManage(num_units_buy, unit_num):
	if num_units_buy == 0:
		return 0
	price = initial_price * (((r ** (unit_num + num_units_buy + 1)) - (r ** (unit_num))) / (r - 1))
	#print(str(price) + "\tprice\n")
	return price



for unit_num in range(initial_num, 75):#final_num + 1):
	time = 0
	cps = initial_cps
	#time to buy n units
	time += costsManage((unit_num - initial_num), unit_num) / cps
	#print(str(time/3600) + "\ts\n")
	UnitsA.buy(unit_num - initial_num)
	cps += UnitsA.tu_cps
	#time to buy the upgrade
	time += upgrade_price / cps
	UnitsA.upgrade()
	cps = initial_cps + UnitsA.tu_cps
	#time to buy n units
	time += costsManage(final_num - unit_num, unit_num) / cps
	#times.append(str(time) + "\t" + str(unit_num))	
	times.append(time)
	numbers.append(unit_num)


#times.sort()
plt.scatter(numbers, times)
plt.grid(True)
plt.show()

#print(times)
































