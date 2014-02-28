#-*- encoding: utf-8 -*-
'''
Created on 2014-02-27 22:00:28

@author: quake0day
'''


import numpy as np

trace1 = {
	'id' : [1,2,3],
	'length': {1:3,2:4,3:5},
	'adjacency': {1:[None,2],2:[3,None],3:[None,None]},
	'image':[{'111011.jpg': 1},{'1202121.jpg': 2},{'112j121233.jpg':3}],

}

trace2 = {
	'id' : [4,5,6],
	'length': {4:3,5:4,6:5},
	'adjacency': {4:[5,None],5:[6,None],6:[None,None]},
	'image':[{'111011sa.jpg': 4},{'120as2121.jpg': 5},{'aa112j121233.jpg':6}],

}


def connect2MatchedTrace(trace1, trace2, match_trace1_id, match_trace2_id, reverse=False):
	adj1 = trace1['adjacency'][match_trace1_id]
	adj2 = trace2['adjacency'][match_trace2_id]

	# Scenario 1
	# if 
	adj_new=[None,None]
	if (adj1[0] == None and adj2[1] == None and adj1[1] != None and adj2[0] != None) \
	or (adj1[1] == None and adj2[0] == None and adj1[0] != None and adj2[1] != None):
		if (adj1[0] == None):
			adj_new[0] = adj2[0]
			adj_new[1] = adj1[1]
		elif (adj1[1] == None):
			adj_new[0] = adj1[0]
			adj_new[1] = adj2[1]

	adj_merge = dict(trace1['adjacency'],**trace2['adjacency'])
	merged_length = dict(trace1['length'],**trace2['length'])
	merged_id = trace1['id'] + trace2['id']
	merged_image = trace1['image'] + trace2['image']

	# pick the longest trace
	if trace1['length'][match_trace1_id] > trace2['length'][match_trace2_id]:
		adj_merge[match_trace1_id] = adj_new
		del adj_merge[match_trace2_id]
		del merged_length[match_trace2_id]
		merged_id.remove(match_trace2_id)
		for im in merged_image:
			#print im.keys()
			if im.values()[0] == match_trace2_id:
				im[im.keys()[0]] = match_trace1_id
	else:
		adj_merge[match_trace2_id] = adj_new
		del adj_merge[match_trace1_id]
		del merged_length[match_trace1_id]
		merged_id.remove(match_trace1_id)
		for im in merged_image:
			#print im.keys()
			if im.values()[0] == match_trace1_id:
				im[im.keys()[0]] = match_trace2_id
 	#print adj_merge
	#print merged_length
	#print merged_id
	#print merged_image
	merged_trace = {'id': merged_id,
					'length': merged_length,
					'adjacency': adj_merge,
					'image': merged_image}
	print merged_trace


	#merged_trace={}
	#print adj_new



	return 0
connect2MatchedTrace(trace1, trace2, 1, 5, False)