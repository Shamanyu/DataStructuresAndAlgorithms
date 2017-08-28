# http://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/

class CoinChange(object):
	
	def __init__(self):
		self.set_coins([])

	def set_coins(self, coins):
		self.coins = coins
		if len(coins) > 0:
			self.lowest_denomination = min(coins)
		else:
			self.lowest_denomination = 0
		self.change_for = dict()

	def get_number_of_ways_to_change(self, money):
		# import pdb; pdb.set_trace()
		if money < 0:
			return -1
		elif money == 0:
			return 0
		elif money in self.change_for:
			return self.change_for[money]
		else:
			combinations = self.get_number_of_ways_to_change(money-self.lowest_denomination) + 1
			self.change_for[money] = combinations
			return self.change_for[money]

coin_change = CoinChange()

coin_change.set_coins([1, 2])
print (coin_change.get_number_of_ways_to_change(0))
print (coin_change.get_number_of_ways_to_change(1))
print (coin_change.get_number_of_ways_to_change(2))

coin_change.set_coins([1, 2, 3])
print (coin_change.get_number_of_ways_to_change(4))

coin_change.set_coins([2, 5, 3, 6])
print (coin_change.get_number_of_ways_to_change(10))