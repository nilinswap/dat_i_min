import sortedcontainers
from sortedcontainers import SortedList, SortedDict, SortedSet
from item_set import Itemset
class Transaction(Itemset):
	'''
	This exists because I am OOP-Nazi.
	'''
	def __init__(self, seth = SortedSet([], key = lambda x: x.st), Tid = None):
		'''

		:param seth: set of Items bought together
		:param Tid: index of Transaction
		'''
		Itemset.__init__(self, seth)
		self.Tid = Tid

	def is_superset_of(self, itemset, is_proper = False):
		'''
		This method is used to see if itemset is a part of the transaction
		:param itemset: Itemset object
		:param is_proper: if proper subset comparison required
		:return: bool
		'''
		if is_proper:
			return itemset.set < self.set
		return itemset.set <= self.set


