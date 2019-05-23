from .trie import make_Trie
import heapq

class Query():

	def search(self, trie, prefix, limit):
		temp = trie
		result = [] # to store matched strings

		lc = 0
		for i in range(len(prefix)):
			if prefix[i] in temp.keys():
				temp = temp[prefix[i]]
				lc = i
				if i < len(prefix)-1:
					continue
			# returning strings only if more than 2 characters are matched
			if lc >= 0:
				self.rec_retrieve(temp, result, limit)
				break
		return result

	def rec_retrieve(self, dic, result, limit):
		if "data" in dic.keys(): # checking if current node is leaf node
			
			if len(result) < limit:
				heapq.heappush(result, (dic['data'].rating, dic['data'].id,dic['data'].movie_name))
			elif dic['data'].rating > result[0][0]:						# maintaining heap to reduce memory used and append only if rating is good enough
				heapq.heappop(result)
				heapq.heappush(result, (dic['data'].rating, dic['data'].id, dic['data'].movie_name))

		else:
			for ed in dic.keys(): # recursive call into children of current node
				self.rec_retrieve(dic[ed], result, limit)


# new_query = input()
#
# query_obj = Query()
#
# matched = query_obj.search(trie, new_query, limit+offset) # matching queried perfix with strings in trie according to limit and offset
#
# if offset <= len(matched):  # removing movies before offset position
# 	for i in range(offset):
# 		heapq.heappop(matched)
#
# while len(matched) > 0: # retrieved data
# 	print(names[matched[0][1]])
# 	heapq.heappop(matched)
