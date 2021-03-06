#-*- encoding: utf-8 -*-
'''
Created on 2014-02-27 22:00:28

@author: quake0day
'''


import numpy as np
import Trace as tr
import PlotTrace as pt

# trace1 = {
#     'id' : [1,2,3],
#     'length': {1:3,2:4,3:5},
#     'adjacency': {1:[None,2],2:[3,None],3:[None,None]},
#     'image':[{'111011.jpg': 1},{'1202121.jpg': 2},{'112j121233.jpg':3}],

# }

# trace2 = {
#     'id' : [4,5,6],
#     'length': {4:3,5:4,6:5},
#     'adjacency': {4:[5,None],5:[6,None],6:[None,None]},
#     'image':[{'111011sa.jpg': 4},{'120as2121.jpg': 5},{'aa112j121233.jpg':6}],

# }

# trace3 = {
#     'id' : [7,8,9],
#     'length': {7:3,8:4,9:5},
#     'adjacency': {7:[8,None],8:[9,None],9:[None,None]},
#     'image':[{'111011sa.jpg': 7},{'120as2121.jpg': 8},{'aa112j121233.jpg':9}],

# }

# trace4 = {
#     'id' : [10,11,12],
#     'length': {10:3,11:4,12:5},
#     'adjacency': {10:[None,11],11:[12,None],12:[None,None]},
#     'image':[{'111011sa.jpg': 10},{'120as2121.jpg': 11},{'aa112j121233.jpg':12}],

# }
# trace5 = {
#     'id' : [11,12,13],
#     'length': {11:4,12:5,13:3},
#     'adjacency': {11:[12,None],12:[13,None],13:[None,None]},
#     'image':[{'111011sasd.jpg': 13},{'120as2121.jpg': 11},{'aa112j121233.jpg':12}],

# }
# trace6 = {
#     'id' : [12,13,14],
#     'length': {14:4,12:5,13:3},
#     'adjacency': {12:[13,None],13:[None,14],14:[None,None]},
#     'image':[{'111011sasd.jpg': 13},{'120as212s1.jpg': 14},{'aa112j121233.jpg':12}],

# }

trace1 = {
    'id' : [1,2,3],
    'length': {1:5, 2:10, 3: 5},
    'adjacency': {1:[2,None], 2:[3, None], 3:[None, None]},
    'image':[{'111011sasd.jpg': 1},{'120as212s1.jpg': 2},{'aa112j121233.jpg':3}]
}

trace1 = {
    'id' : [1,2,3],
    'length': {1:5, 2:10, 3: 4.5},
    'connection':{
                    1:[None,None,None,None,None,None,None,None,None,[2,None]],
                    2:[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,[3,None]],
                    3:[None,None,None,None,None,None,None,None,None],
                  },
    'image':[{'111011sasd.jpg': [1,1]},{'111011sasd.jpg': [1,3]},{'111011sasd.jpg': [1,4]},{'120as212s1.jpg': [2,1]},{'aa112j121233.jpg':[2,2]}]
}

trace2 = {
    'id' : [4,5,6],
    'length': {4:4, 5:9, 6: 8},
    'connection':{
                    4:[None,None,None,None,None,None,None,[5,None]],
                    5:[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,[6,None]],
                    6:[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
                  },
    'image':[{'111011sasd.jpg': [4,1]},{'111011sasd.jpg': [4,3]},{'111011sasd.jpg': [4,4]},{'120as212s1.jpg': [5,1]},{'aa112j121233.jpg':[5,2]}]
}

trace_merged = {
    'id' : [4,5,6],
    'length': {1:5,3: 4.5, 4:4, 5:13, 6: 8},
    'connection':{
                    1:[None,None,None,None,None,None,None,None,None,[2,None]],
                    3:[None,None,None,None,None,None,None,None,None],
                    4:[None,None,None,None,None,None,None,[5,None]],
                    5:[None,None,None,None,None,None,None,None,None,None,None,None,\
                        None,None,None,None,None,None,None,[3,None],None,None,None,None,None,[6,None]],
                    6:[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
                  },
    'image':[{'111011sasd.jpg': [4,1]},{'111011sasd.jpg': [4,3]},{'111011sasd.jpg': [4,4]},{'120as212s1.jpg': [5,1]},{'aa112j121233.jpg':[5,2]}]
}
print trace_merged


trace2 = {
    'id' : [4,5,6],
    'length': {4:5, 5:15, 6: 7},
    'adjacency': {4:[5,None], 5:[6, None], 6:[None, None]},
    'image':[{'111011sasd.jpg': 4},{'120as212s1.jpg': 5},{'aa112j121233.jpg':6}],
}

trace3 = {
    'id' : [7,8,9],
    'length': {7:15, 8:5, 9:15},
    'adjacency': {7:[None,8], 8:[None, 9], 9:[None, None]},
    'image':[{'111011sasd.jpg': 7},{'120as212s1.jpg': 8},{'aa112j121233.jpg':9}],
}

trace4 = {
    'id' : [10,11,12],
    'length': {10:8, 11:10, 12:7},
    'adjacency': {10:[11,None], 11:[12, None], 12:[None, None]},
    'image':[{'111011sasd.jpg': 12},{'120as212s1.jpg': 10},{'aa112j121233.jpg':11}],
}



def connect2MatchedTrace(trace1, trace2, match_trace1_id, match_trace2_id, reverse=False):
    match_done = False
    contniue_match = []
    adj1 = trace1['adjacency'][match_trace1_id]
    adj2 = trace2['adjacency'][match_trace2_id]


    # change the merged path one step before the merged line

    #if any(match_trace1_id in s for s in trace1['adjacency'].values()):
    pre_match1_key = None
    pre_match2_key = None
    pre_match_key = None
    pre_match_key_del = None

    pre_match1 = []
    pre_match2 = []


    # find path that connect to the target merged path
    for x,s in zip(trace1['adjacency'].keys(),trace1['adjacency'].values()):
        if match_trace1_id in s:
            pre_match1 = s
            pre_match1_key = x

    for y,t in zip(trace2['adjacency'].keys(),trace2['adjacency'].values()):
        if match_trace2_id in t:
            pre_match2 = t
            pre_match2_key = y

    # If two (pre)paths needs to merge, find the one that shall be delete
    try:
        if trace1['length'][pre_match1[0]] > trace2['length'][pre_match2[0]]:
            pre_match_key = pre_match2_key
            pre_match_key_del = pre_match1_key
        else:
            pre_match_key = pre_match1_key
            pre_match_key_del = pre_match2_key
        print pre_match1_key,pre_match2_key,pre_match_key
    except:
        print "No Pre_match"
        pass


    # change the merged path one step after the merged line
    print adj1
    print adj2
    adj_new=[None,None]
    # Scenario 1
    # if 
    if (adj1[0] == None and adj2[1] == None and adj1[1] != None and adj2[0] != None) \
    or (adj1[1] == None and adj2[0] == None and adj1[0] != None and adj2[1] != None):
        print "scenario 1"
        if (adj1[0] == None):
            adj_new[0] = adj2[0]
            adj_new[1] = adj1[1]
        elif (adj1[1] == None):
            adj_new[0] = adj1[0]
            adj_new[1] = adj2[1]

    # Scenario 2
    if (adj1[0] == None and adj1[1] == None)\
    or (adj2[0] == None and adj2[1] == None):
        print "scenario 2"
        if (adj1[0] == None and adj1[1] == None):
            print adj2
            adj_new[0] = adj2[0]
            adj_new[1] = adj2[1]
        else:
            adj_new[0] = adj1[0]
            adj_new[1] = adj1[1]

    # Scenario 3
    print adj1,adj2
    if (adj1[0] == None and adj2[0] == None and adj1[1] != None and adj2[1] != None) \
    or (adj1[1] == None and adj2[1] == None and adj1[0] != None and adj2[0] != None):
        print "scenario 3"
        trim_path = None
        preserved_path = None
        if (adj1[0] == None):
            if trace1['length'][adj1[1]] > trace2['length'][adj2[1]]:
                trim_path = adj2[1]
                preserved_path = adj1[1]
                adj_new[0] = None
                adj_new[1] = adj1[1]
            else:
                trim_path = adj1[1]
                preserved_path = adj2[1]
                adj_new[0] = None
                adj_new[1] = adj2[1]
        elif (adj1[1] == None):
            if trace1['length'][adj1[0]] > trace2['length'][adj2[0]]:
                trim_path = adj2[0]
                preserved_path = adj1[0]
                adj_new[0] = adj1[0]
                adj_new[1] = None
            else:
                trim_path = adj1[0]
                preserved_path = adj2[0]
                adj_new[0] = adj2[0]
                adj_new[1] = None
    print "NEW ADJ"
    print adj_new
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
        for key,value in zip(adj_merge.keys(),adj_merge.values()):
            if match_trace2_id in value:
                i = 0
                while i < len(value):
                    print value[i]
                    if value[i] == match_trace2_id:
                        value[i] = match_trace1_id
                    i += 1
        for im in merged_image:
            #print im.keys()
            if im.values()[0] == match_trace2_id:
                im[im.keys()[0]] = match_trace1_id
        print adj_merge
    else:
        adj_merge[match_trace2_id] = adj_new
        del adj_merge[match_trace1_id]
        del merged_length[match_trace1_id]
        merged_id.remove(match_trace1_id)
        print "There"
        print match_trace1_id
        for key,value in zip(adj_merge.keys(),adj_merge.values()):
            if match_trace1_id in value:
                i = 0
                while i < len(value):
                    print value[i]
                    if value[i] == match_trace1_id:
                        value[i] = match_trace2_id
                    i += 1

        print adj_merge
        for im in merged_image:
            #print im.keys()
            if im.values()[0] == match_trace1_id:
                im[im.keys()[0]] = match_trace2_id
    try:
        if (pre_match_key != None):
            print "HELLOW"
            print pre_match1_key
            print pre_match2_key

            i = 0
            j = 0
            while i < len(adj_merge):
                while j < len(adj_merge.values()[i]):
                    if adj_merge.values()[i][j] == pre_match_key:
                        adj_merge.values()[i][j] = pre_match_key_del
                    j += 1
                i += 1
            #del adj_merge[pre_match_key]

        if (trim_path != None):
            print trim_path
            print adj_merge[preserved_path]
            print adj_merge[trim_path]
            # Make sure two lists are in the same length
            assert(len(adj_merge[preserved_path]) == len(adj_merge[trim_path]))
            i = 0
            # with different situation apply different func
            # try to perserve the "next path" info when trimming certain path
            while i < len(adj_merge[preserved_path]):
                if adj_merge[preserved_path][i] == None and adj_merge[trim_path][i] != None:
                    adj_merge[preserved_path][i] = adj_merge[trim_path][i]
                elif adj_merge[preserved_path][i] == None and adj_merge[trim_path][i] == None:
                    pass
                elif adj_merge[preserved_path][i] != None and adj_merge[preserved_path] != None:
                    contniue_match.append([trim_path,preserved_path])
                i += 1
            del adj_merge[trim_path]
    except:
        pass

    #print adj_merge
    #print merged_length
    #print merged_id
    #print merged_image
    merged_trace = {'id': merged_id,
                    'length': merged_length,
                    'adjacency': adj_merge,
                    'image': merged_image}
    #merged_trace = tr.Trace(merged_id, merged_length, adj_merge, merged_image)
    print merged_trace
    print contniue_match


    #merged_trace={}
    #print adj_new
    return merged_trace

merged_trace = connect2MatchedTrace(trace1, trace2, 2, 5, False)
merged_trace = connect2MatchedTrace(merged_trace, trace3, 5, 8, False)
merged_trace = connect2MatchedTrace(merged_trace, trace4, 5, 10, False)
#merged_trace = connect2MatchedTrace(merged_trace, trace5, 12, 12, False)
#merged_trace = connect2MatchedTrace(merged_trace, trace6, 12, 12, False)
pt.plotTraceMatch(merged_trace)