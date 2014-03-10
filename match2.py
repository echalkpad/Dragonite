#-*- encoding: utf-8 -*-
'''
Created on 2014-03-09 16:34:20

@author: quake0day
'''

import math
import Trace as Trace
import Path as Path
# Try to match two traces
# trace1 = {
#     'id' : [1,2,3],
#     'connection': {
#         1: [None,None,None,None,None,None,None,None,None,[2,None]],
#         2: [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,[3,None]],
#         3: [None,None,None,None,None,None,None,None,None,],
#     },
#     'image':{'111011.jpg': [1,1], '22.jpg': [2,2], '23.jpg': [2,3],'112j121233.jpg':[3,4]},
# }

# trace2 = {
#     'id' : [4,5,6],
#     'connection': {
#         4: [None,None,None,None,None,None,None,[5,None]],
#         5: [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,[6,None]],
#         6: [None,None,None,None,None,None,None,None,None,None,None,None]
#     },
#     'image':{'111011.jpg': [4,1],'53.jpg': [5,3],'112j121233.jpg':[5,4],'112j121233.jpg':[6,1]},
# }


def matchQuality(trace1, trace2, imageMatch):
    return 0


def comparePath(path1, path2):
    if path1.id == None and path2.id == None:
        return None
    elif path1.id == None and path2.id != None:
        return path2
    elif path1.id != None and path2.id == None:
        return path1
    elif path1.id != None and path2.id != None:
        if path1.getLength == path2.getLength:
            return path1
        else:
            # we need keep the longer path and remain the shorter path to the longer's name
            if (path1.getLength > path2.getLength):
                return path1
            else:
                return path2

def match2Trace(trace1, trace2, imageMatch):
    changeID = []
    image1 = imageMatch[0][0]
    image2 = imageMatch[0][1]
    position1 = trace1.getImagePos(image1)
    position2 = trace2.getImagePos(image2)
    match_trace_1 = trace1.getPath(position1[0])
    match_trace_2 = trace2.getPath(position2[0])

    match_and_back_1 = match_trace_1[position1[1]:]
    match_and_back_2 = match_trace_2[position2[1]:]

    # Merge back
    merged_trace_back = []
    trace1_mb_length = len(match_and_back_1)
    trace2_mb_length = len(match_and_back_2)

    if trace1_mb_length > trace2_mb_length:
        diff_trace_back = match_and_back_1[trace1_mb_length - trace2_mb_length:]
    elif trace1_mb_length < trace2_mb_length:
        diff_trace_back = match_and_back_2[trace2_mb_length - trace1_mb_length:]
    else:
        diff_trace_back = None

    for item in zip(match_and_back_1, match_and_back_2):
        if item[0] == item[1] == None:
            merged_trace_back.append(None)
        elif item[0] == None or item[1] == None:
            if item[0] is None:
                merged_trace_back.append(item[1])
            else:
                merged_trace_back.append(item[0])
        else:
            try:
                longer_path = [None, None]
                # Compare left Path
                if item[0][0] != None and item[1][0] != None:
                    if trace1.getLength(item[0][0]) >= trace2.getLength(item[1][0]):
                        changeID.append([item[0][0],item[1][0]])
                        longer_path[0] = item[0][0]
                    else:
                        changeID.append([item[1][0],item[0][0]])
                        longer_path[0] = item[1][0]
                elif item[0][0] == item[1][0] == None:
                    longer_path[0] = None
                elif item[0][0] == None or item[1][0] == None:
                    if item[0][0] is None:
                        longer_path[0] = item[1][0]
                    else:
                        longer_path[0] = item[0][0]

                # Compare right Path
                if item[0][1] != None and item[1][1] != None:
                    if trace1.getLength(item[0][1]) >= trace2.getLength(item[1][1]):
                        changeID.append([item[0][1],item[1][1]])
                        longer_path[1] = item[0][1]
                    else:
                        changeID.append([item[1][1],item[0][1]])
                        longer_path[1] = item[1][1]
                elif item[0][1] == item[1][1] == None:
                    longer_path[1] = None
                elif item[0][1] == None or item[1][1] == None:
                    if item[0][1] is None:
                        longer_path[1] = item[1][1]
                    else:
                        longer_path[1] = item[0][1]
            except:
                print "MATCH2 COMPARISION ERROR "
            merged_trace_back.append(longer_path)
    #print merged_trace_back
    # print match_trace_1,match_trace_2
    if position1[1] >= 1:
        remaining_trace_1_front = match_trace_1[0:position1[1]]
    else:
        remaining_trace_1_front = []
    if position2[1] >= 1:
        remaining_trace_2_front = match_trace_2[0:position2[1]]
    else: 
        remaining_trace_2_front = []
    #print match_and_back_1,match_and_back_2
    #print remaining_trace_1_front
    #print remaining_trace_2_front


    merged_trace = []

    # Merge the front part
    trace1_front_len = len(remaining_trace_1_front)
    trace2_front_len = len(remaining_trace_2_front)
    #print remaining_trace_1_front
    #print remaining_trace_2_front
    if trace1_front_len > trace2_front_len:
        diff_trace_front = remaining_trace_1_front[0:trace1_front_len - trace2_front_len]
    elif trace1_front_len < trace2_front_len:
        diff_trace_front = remaining_trace_2_front[0:trace2_front_len - trace1_front_len]
    else:
        diff_trace_front = None

    # Reverse two trace's front part for easy compare
    remaining_trace_1_front.reverse()
    remaining_trace_2_front.reverse()
    for item in zip(remaining_trace_1_front, remaining_trace_2_front):
        if item[0] == item[1] == None:
            merged_trace.append(None)
        elif item[0] == None or item[1] == None:
            if item[0] is None:
                merged_trace.append(item[1])
            else:
                merged_trace.append(item[0])
        else:
            longer_path = [None,None]
            try:
                # Compare left Path
                if item[0][0] != None and item[1][0] != None:
                    if trace1.getLength(item[0][0]) >= trace2.getLength(item[1][0]):
                        changeID.append([item[0][0],item[1][0]])
                        longer_path[0] = item[0][0]
                    else:
                        changeID.append([item[1][0],item[0][0]])
                        longer_path[0] = item[1][0]
                elif item[0][0] == item[1][0] == None:
                    longer_path[0] = None
                elif item[0][0] == None or item[1][0] == None:
                    if item[0][0] is None:
                        longer_path[0] = item[1][0]
                    else:
                        longer_path[0] = item[0][0]

                # Compare right Path
                if item[0][1] != None and item[1][1] != None:
                    if trace1.getLength(item[0][1]) >= trace2.getLength(item[1][1]):
                        changeID.append([item[0][1],item[1][1]])
                        longer_path[1] = item[0][1]
                    else:
                        changeID.append([item[1][1],item[0][1]])
                        longer_path[1] = item[1][1]
                elif item[0][1] == item[1][1] == None:
                    longer_path[1] = None
                elif item[0][1] == None or item[1][1] == None:
                    if item[0][1] is None:
                        longer_path[1] = item[1][1]
                    else:
                        longer_path[1] = item[0][1]
            except:
                print "MATCH2 COMPARISION ERROR "
            merged_trace.append(longer_path)
    diff_trace_front.reverse()
    if diff_trace_front != None:
        merged_trace += diff_trace_front
    merged_trace.reverse()
    merged_trace += merged_trace_back
    if diff_trace_back != None:
        merged_trace += diff_trace_back
    #print diff_trace_back
    print merged_trace
    print changeID
    #print merged_trace

    # Merge Image and ID
    trace1.changeID(changeID)
    trace2.changeID(changeID)
    print trace1.id
    print trace2.id
    print trace1.image
    print trace2.image


    # if trace1_front_len == 0 and trace2_front_len == 0:
    #     pass
    # elif trace1_front_len == 0 and trace2_front_len != 0:
    #     merged_trace = remaining_trace_2_front
    # elif trace1_front_len != 0 and trace2_front_len == 0:
    #     merged_trace = remaining_trace_1_front
    # else:
    #     pass
       # try:
            #remaining_trace_1_front
    return merged_trace



    # remaining_trace_1_back = match_trace_1[position1[1]:]
    # remaining_trace_2_back = match_trace_2[position2[1]:]

    # situation 1 
    # ________________a_____________
    #        _________________________b____________________

    # situation 2
    # ________________a_____________
    #        _____________b_______

    # situation 3
    #               _____a_______
    #        _____________b_______
    # if len(remaining_trace_1_back) >= len(remaining_trace_2_back):
    #     diff_trace_back = remaining_trace_1_back[len(remaining_trace_1_back)-len(remaining_trace_2_back):]
    # else:
    #     diff_trace_back = remaining_trace_2_back[len(remaining_trace_2_back)-len(remaining_trace_1_back):]

    # if len(remaining_trace_1_front) >= len(remaining_trace_2_back):
    #     diff_trace_front = remaining_trace_1_front[len(remaining_trace_1_front)-len(remaining_trace_2_front):]
    # else:
    #     diff_trace_front = remaining_trace_2_front[len(remaining_trace_2_front)-len(remaining_trace_1_front):]


    # for path_points in zip(remaining_trace_1_back, remaining_trace_2_back):
    #     merge_points = []
    #     if path_points[0] != path_points[1]:
    #         if path_points[0] == None:
    #             merge_points.append(path_points[1])
    #         elif path_points[1] == None:
    #             merge_points.append(path_points[0])
    #         else:
    #             pass # Need add new func
    #     else:
    #         merge_points.append(path_points[0])
    




if __name__=="__main__":
    path1 = Path.Path(1, [None,None,None,None,None,None,None,None,None,[2,None]],[{'111sd011.jpg': 1},{'111f011.jpg': 2}])
    path2 = Path.Path(2, [[3,None],None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,[3,None]],[{'23.jpg': 3},{'22.jpg': 2}])
    path3 = Path.Path(3, [None,None,None,None,None,None,None,None,None],[{'11dsf1011.jpg': 1},{'11sdf1011.jpg': 2}])
    path4 = Path.Path(4, [None,None,None,None,None,None,None,[5,None]],[{'11101a1.jpg': 1},{'111011s.jpg': 2}])
    path5 = Path.Path(5, [None,[4,6],None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,[6,None]],[{'112j121233.jpg': 4},{'53.jpg': 3}])
    path6 = Path.Path(6, [None,None,None,None,None,None,None,None,None,None,None,None],[{'111sf011.jpg': 1},{'1110sdsa11.jpg': 2}])
    #print path3.getLength()
    trace1 = Trace.Trace([path1,path2,path3])
    trace2 = Trace.Trace([path4,path5,path6])
    match2Trace(trace1, trace2, [['22.jpg','53.jpg'],['23.jpg','112j121233.jpg']])