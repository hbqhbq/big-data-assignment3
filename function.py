import heapq
from object import Resturant


def min_heap(res, k):

    #obj = list_obj1 + list_obj2
    obj = res
    q = []

    for i in range(len(obj)):
        heapq.heappush(q, [-obj[i].lower_bound,obj[i].id])
    big_to_small = [heapq.heappop(q) for j in range(len(q))]
    #print(big_to_small)
    for j in range(len(big_to_small)):
        big_to_small[j][0] = -big_to_small[j][0]
    wk = big_to_small[:k]
    wk.reverse()
    return wk
    """
    for i in range(len(obj)):
        heapq.heappush(q, [obj[i].lower_bound,obj[i].id])
    wk = q[:k]
    return wk
    """

def min_heap1(res, k, top):

    # obj = list_obj1 + list_obj2
    obj = res
    q = []
    for i in range(len(obj)):
        if (res[i].lower_bound > top):
            heapq.heappush(q, [-obj[i].lower_bound, obj[i].id])
            big_to_small = [heapq.heappop(q) for j in range(len(q))]
        # print(big_to_small)
            for j in range(len(big_to_small)):
                big_to_small[j][0] = -big_to_small[j][0]
            wk = big_to_small[:k]
            wk.reverse()
            return wk
    """
    for i in range(len(obj)):
        heapq.heappush(q, [obj[i].lower_bound, obj[i].id])
    wk = q[:k]
    return wk
    """





def cal_T(list_obj1, list_obj2):
    T = round(list_obj1[-1].score + list_obj2[-1].score + 5.0, 3)
    return T

#def find_id(lower_bound,restaurant,R):
    #self.lower_bound = round(R[int(self.id)] + self.score1, 3)
    #t = round(lower_bound - restaurant.score1,2)
    #for i in range(len(R)):
    #   if(float(R[i]) == t):
            #return i

def find_id(obj, list_obj):#找到listobj中出现过obj的id的行数
    for i in range(len(list_obj)):
        if(obj.id == list_obj[i].id):
            return i
