
def make_Trie(obj_list, trie):
	for i in range(len(obj_list)): # iterating over names of movies
		temp = trie
		for j in range(len(obj_list[i].movie_name)): # iterating over characters
			cur = obj_list[i].movie_name[j].lower()

			if cur.isalnum() == False:
				continue

			if cur in temp.keys(): # cheching if node exists in trie
				temp = temp[cur]

			else:
				temp[cur] = {}  # creating new node or in this case new nested dictionary
				temp = temp[cur]

			if j == len((obj_list[i].movie_name))-1: # storing information in leaf node or innermost dictionary
				temp["data"] = obj_list[i]


'''names = list(input().split())
ratings = list(map(int, input().split()))

trie = {}
make_Trie(names, ratings, trie)

print(trie)'''
