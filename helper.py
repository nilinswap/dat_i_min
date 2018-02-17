import sortedcontainers
from sortedcontainers import SortedList, SortedDict, SortedSet
from item_set import Itemset
from transaction import Transaction
def first_freq_itemset(Db, I, min_sup):
	'''
	This function generates the initial L ( frequent itemset set ) which is only of one
	element
	:param Db: set of Transactons
	:param I:  set of items used.
	:param min_sup: minimum support
	:return:
	'''

	L = SortedSet([], key = lambda x: (len(x.set._list),x.set._list))
	lis = []
	for trans in Db:
		lis+=list(trans.set)
	for item in I:
		print(item)
		c = lis.count(item)
		if c < min_sup:
			continue

		L.add(Itemset(SortedSet(item)))

	return L

class Non_iter:

	def __init__(self, st):
		self.st = st
def read_data(st):
	'''

	:param st:
	:return:
	'''

	fileo = open(st, 'r+')
	lis_of_lis = fileo.readlines()
	Db_lis = [set([(itemm, '0') for itemm in item.rstrip().lstrip().split(' ')]) for item in lis_of_lis]
	I_set = SortedSet([])
	for item in Db_lis:
		I_set = I_set.union(SortedSet( item ))
	I = list(I_set)
	I = [ (item, '0') for item in I]
	pass
	Db_lis = [Transaction(seth=SortedSet(item), Tid=num) for num, item in enumerate(Db_lis)]
	Db = SortedSet(Db_lis, key=lambda x: x.Tid)
	I = SortedSet([(str(i),'0') for i in range(100)])
	return Db, I
def apriori_gen(Db, L, I, min_sup):
	'''
	The task of this function is to generate next candidate set using L.
	:param Db: set of Transactons
	:param L:  frequent itemset set of a particular level
	:param I:  set of items used.
	:param min_sup: minimum support
	:return: set of Itemset objects
	'''
	C = SortedSet([], key = lambda x: (len(x.set._list),x.set._list))
	for num, itemset_1 in enumerate(L):
		for itemset_2 in L[num+1:]:
			tup = itemset_1.can_be_joined_with(itemset_2)
			if  tup is not None:
				new_set = SortedSet(itemset_1.set)
				new_set.add(tup[1])
				new_itemset = Itemset(seth = new_set)
				new_itemset.last_tup = tup
				if new_itemset.has_infrequent_subset(L):
					C.add(new_itemset)
	return C

if __name__ == '__main__':
	Db = read_data('chess.dat')
	pass