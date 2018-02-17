import sortedcontainers
from sortedcontainers import SortedList, SortedDict, SortedSet

class Itemset:

	'''
	This class exists because it is necessary. Set of Set is not possible( i.e. set is non-hashables because
															they are mutables)
	So a class was made with set as attribute
	'''
	last_tup = None # this is useful to reduce complexity in has_infrequent_subset method
	def __init__(self, seth = SortedSet([])):
		'''
		:param seth: set of items( string typically)
		'''
		self.set = seth
	def can_be_joined_with(self, itemset):
		'''
		This function compares first len(self.set) - 1 items [ remember we are dealing with sorted sets]
			of both self and itemset  and if they are respectively same, if yes then returns a (two-)tuple of the non-common
			elements otherwise None
		:param itemset: other Itemset object
		:return: tuple of two items, namely non-common items or None
		'''
		print(self.set, itemset.set)
		assert( len(self.set) == len(itemset.set))
		tup = self.set[-1], itemset.set[-1]
		if self.set[:-1] == []:
			return tup
		for item1, item2 in zip(self.set[:-1], itemset.set[:-1]):
			if item1 != item2:
				return None
		return tup
	def has_infrequent_subset(self, L):
		'''
		This function sees if self's all len(self.set) - 1 itemsets are frequent by seeing there
		their presence in L( which is itself having only len(self.set) - 1 itemsets)
		It does it smartly by considering L's sets' cardinality and the equivalence relationship
		of enclosure. See speacial case of L's sets' cardinality being 1 was taken care seperately.
		:param L: frequent Itemset
		:return: bool, True if even one subset of L is found infrequent else False
		'''
		assert(self.last_tup is not None)
		last_tup_set = SortedSet(self.last_tup)
		common_set =self.set - last_tup_set
		flago = False
		if len(common_set) == 0:
			return True
		for num, item in enumerate(common_set):
			reduced_set = common_set - SortedSet([item])
			reduced_set = reduced_set.union(last_tup_set)
			flago = False
			for itemset in L:
				if reduced_set == itemset.set:
					flago = True
					break
			if not flago:
				return flago
		return flago