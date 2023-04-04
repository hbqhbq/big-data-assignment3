from object import Resturant
from object import Line
from object import obj
from function import find_id
import function
import heapq

R=[]
fr=open('data/rnd.txt', 'r')
all_lines=fr.readlines()
for line in all_lines:
    line=line.strip().split(' ')
    temp = list(map(float,line))
    R.append(float(temp[1]))


k = 5

id1 = []
id2 = []

list_obj1 = []
list_obj2 = []
res = []
f1 = open('data/seq1.txt', 'r')
f2 = open('data/seq2.txt', 'r')

# 使用readline()读文件
for i in range(k):
    line1 = f1.readline()
    if line1:
        temp1 = line1.strip('\n').split(' ')
        id = int(temp1[0])
        id1.append(id)
        list_obj1.append(obj(id))
        list_obj1[i].score = float(temp1[1])
        if(list_obj1[i].id not in id2):
            resturant = list_obj1[i]
            resturant.cal_lower_bound(R)
            res.append(resturant)
        else:
            row = find_id(list_obj1[i],res)
            res[row].cal_total_score(list_obj1[i])
            #list_obj1[i].cal_total_score(lambda x: list_obj2[x].id == list_obj1[i].id)


        #f2 = open('data/seq2.txt', 'r')
    line2 = f2.readline()
    if line2:
        temp2 = line2.strip('\n').split(' ')
        id = int(temp2[0])
        list_obj2.append(obj(id))
        id2.append(id)
        list_obj2[i].score = float(temp2[1])
        if (list_obj2[i].id not in id1):
            resturant = list_obj2[i]
            resturant.cal_lower_bound(R)
            res.append(resturant)
        else:
            row = find_id(list_obj2[i],res)
            res[row].cal_total_score(list_obj2[i])
            #list_obj2[i].cal_total_score(lambda x: list_obj1[x].id == list_obj2[i].id)

    else:
        break
    #obj[i].printo()

for i in range(len(res)):
    res[i].printo()

wk = function.min_heap(res,k)
print(wk)

#print([x[1] for x in wk])

#f2 = open('data/seq2.txt', 'r')
T = function.cal_T(list_obj1,list_obj2)

line = []
t = k
break_out_flag = False
#while (wk[0][0] < T):
while True:
    line1 = f1.readline()
    if line1:
        temp1 = line1.strip('\n').split(' ')
        id = int(temp1[0])
        #print(id)
        list_obj1.append(obj(id))
        id1.append(id)
        list_obj1[t].score = float(temp1[1])
        list_obj1[t].cal_lower_bound(R)
        if(list_obj1[t].id not in id2):
            resturant = list_obj1[t]
            res.append(resturant)
            for i in range(len(res)):
                if(res[i] in list_obj2 and res[i].lower_bound != res[i].total_score):
                    res[i].upper_bound = round(res[i].lower_bound + list_obj1[t].score,3)

            #list_obj1[t].cal_lower_bound(R)
        else:
            row = find_id(list_obj1[t],res)
            res[row].cal_total_score(list_obj1[t])
            #res[row].upper_bound = round(res[row].lower_bound + list_obj1[t-1].score,3)
            res[row].lower_bound = res[row].total_score
            res[row].upper_bound = res[row].total_score


    line2 = f2.readline()
    if line2:
        temp2 = line2.strip('\n').split(' ')
        id = int(temp2[0])
        list_obj2.append(obj(id))
        id2.append(id)
        list_obj2[t].score = float(temp2[1])
        list_obj2[t].cal_lower_bound(R)
        print(t)
        if (list_obj2[t].id not in id1):
            resturant = list_obj2[t]
            res.append(resturant)
            for i in range(len(res)):
                if(res[i] in list_obj1 and res[i].lower_bound != res[i].total_score <15):
                    res[i].upper_bound = round(res[i].lower_bound + list_obj2[t].score,3)
        else:
            row = find_id(list_obj2[t],res)
            res[row].cal_total_score(list_obj2[t])
            #res[row].upper_bound = round(res[row].lower_bound + list_obj2[t - 1].score,3)
            res[row].lower_bound = res[row].total_score
            res[row].upper_bound = res[row].total_score

    t_temp = function.cal_T(list_obj1[:-1],list_obj2[:-1])
    #wk_temp = function.min_heap(res[:-1], k)
    T = function.cal_T(list_obj1,list_obj2)
    #if(res[t+k].lower_bound > wk[0][0]):
        #wk = function.min_heap(res, k)
        #print(wk, T)
    if (res[t + k].lower_bound > wk[0][0]):
        wk = function.min_heap(res,k)
    #print(T,wk)

    if (wk[0][0] < T):
        t += 1
        continue
    else:
        print(wk,T)
        flag = 0
        for i in range(len(res)):
            #print(res[i].upper_bound)
            if(([res[i].lower_bound, res[i].id] not in wk) and res[i].upper_bound > wk[0][0]):
                #print(wk[0][0])
                res[i].printo()
                wk=function.min_heap(res, k)
                flag = 1

        #print(flag)
        if flag == 1:
            t+=1
            continue
        if flag==0:
            for i in range(len(res)):
                res[i].printo()

            print(wk,t)
            break_out_flag = True
        if(break_out_flag==True):
            break
            #print([res[i].lower_bound, res[i].id], wk, res[i].upper_bound, wk[0][0])
            #if (([res[i].lower_bound, res[i].id] not in wk) and res[i].upper_bound > wk[0][0]):
                #print("hello")
                #print(len(res),i)
                #t += 1
                #break
            #if(i==len(res)):
                #print(wk)


"""
            #print(i)
            res[i].printo()
            if (([res[i].lower_bound, res[i].id] not in wk) and res[i].upper_bound>wk[0][0]):
                print([rewks[i].lower_bound, res[i].id])
                print(wk,res[i].upper_bound)
                continue
            else:
                wk = function.min_heap(res,k)
                print(wk)
                break
            break
"""
            #print(wk[0],T)

#print(t)






if __name__ == '__main__':
    print("hi")
