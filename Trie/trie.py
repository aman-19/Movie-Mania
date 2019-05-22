
def make_Trie(names, ratings, trie):
	for i in range(len(names)): # iterating over names of movies
		temp = trie
		for j in range(len(names[i])): # iterating over characters
			cur = names[i][j]

			if cur in temp.keys(): # cheching if node exists in trie
				temp = temp[cur]

			else:
				temp[cur] = {}  # creating new node or in this case new nested dictionary
				temp = temp[cur]

			if j == len(names[i])-1: # storing information in leaf node or innermost dictionary
				temp["id"] = i
				temp["rating"] = ratings[i]


'''names = list(input().split())
ratings = list(map(int, input().split()))

trie = {}
make_Trie(names, ratings, trie)

print(trie)'''
