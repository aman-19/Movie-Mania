from trie import make_Trie
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
			if lc >= 2: 
				self.rec_retrieve(temp, result, limit)

		return result

	def rec_retrieve(self, dic, result, limit):
		if "id" in dic.keys(): # checking if current node is leaf node
			if len(result) < limit:
				heapq.heappush(result, (dic['rating'], dic['id']))
			elif dic['rating'] > result[0][0]:						# maintaining heap to reduce memory used and append only if rating is good enough
				heapq.heappop(result)
				heapq.heappush(result, (dic['rating'], dic['id']))

		else:
			for ed in dic.keys(): # recursive call into children of current node
				self.rec_retrieve(dic[ed], result, limit)


# scanning input
names = list(input().split())
ratings = list(map(float, input().split()))
limit = int(input())
offset = int(input())

trie = {}
make_Trie(names, ratings, trie) # trie construction

new_query = input()

query_obj = Query()

matched = query_obj.search(trie, new_query, limit+offset) # matching queried perfix with strings in trie according to limit and offset

if offset <= len(matched):  # removing movies before offset position
	for i in range(offset):
		heapq.heappop(matched)

while len(matched) > 0: # retrieved data
	print(names[matched[0][1]])
	heapq.heappop(matched)
