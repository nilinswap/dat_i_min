import sortedcontainers
from sortedcontainers import SortedList, SortedDict, SortedSet
from helper import *
from transaction import Transaction
from item_set import Itemset

def Apriori(Db,I, min_sup):
	'''
	This is the main Apriori function that calclates all frequent itemsets from Db( set of Transactons).
	:param Db: set of Transactons
	:param I:  set of items used.
	:param min_sup: minimum support
	:return: The set of Itemset objects
	'''

	min_sup = len(Db)*min_sup

	L = first_freq_itemset(Db, I, min_sup)
	i = 2

	final_L = SortedSet(L, key= lambda x: (len(x.set._list),x.set._list))
	while len(L)!= 0:
		C = apriori_gen(Db, L, I, min_sup)
		L = SortedSet([], key = lambda x: (len(x.set._list),x.set._list))
		for itemset_c in C:
			coun = 0
			for trans_d in Db:
				if trans_d.is_superset_of(itemset_c, is_proper=False):
					coun+=1
			if coun >= min_sup:
				L.add(itemset_c)



		i+=1
		final_L = final_L.union(L)

	return final_L





def Test():
	'''
	Rest is Test
	:return: None
	'''
	I = SortedSet([str(i) for i in range(1,6)])
	Db_lis = [{'1', '2', '5'}, {'2', '4'}, {'2', '3'}, {'1', '2', '4'}, {'1', '3'}, {'2', '3'}, {'1', '3'}, {'1', '2', '3', '5'}, {'1', '2', '3'}]
	Db_lis = [Transaction(seth = SortedSet(item), Tid = num) for num, item in enumerate(Db_lis)]
	Db = SortedSet(Db_lis, key = lambda x: x.Tid)
	min_sup = 0.5
	#q = first_freq_itemset(Db, I, min_sup)
	p = Apriori(Db, I, min_sup )
	print(p)
def main_test():
	min_sup = 0.9
	Db, I = read_data('chess.dat')
	p = Apriori(Db, I, min_sup)
	for itemset in p:
		print(itemset.set._list)
	print(p)
if __name__ == '__main__':
	main_test()