

class Resturant:
    def __init__(self, id):
        self.id = id
        self.score1 = 0
        self.score2 = 0
        self.flag = 0
        self.lower_bound = 0
        self.total_score = 0
        self.upper_bound = 0

    def cal_lower_bound(self, R):
        if (self.flag == 0):
            self.lower_bound = round(R[int(self.id)] + self.score1,3)
            self.flag = 1

    def cal_total_score(self):
        if (self.flag == 1):
            self.total_score = round(self.lower_bound + self.score2,3)

    def cal_upper_bound(self, Restaurant):
        self.upper_bound = self.lower_bound + Restaurant.score2

    def printo(self):
        print("id:{}, score1:{}, score2:{}, lower_bound:{}, total_score:{}, upper_hound:{}".format(self.id,self.score1,self.score2,self.lower_bound,self.total_score,self.upper_bound))

class Line:
    def __init__(self, id1,id2):
        self.id1 = 0
        self.id2 = 0
        self.score1 = 0
        self.score2 = 0

class obj:
    def __init__(self, id):
        self.id = id
        self.score = 0
        self.flag = 0
        self.lower_bound = 1000
        self.upper_bound = 0
        self.total_score = 0
    def cal_lower_bound(self, R):
        self.lower_bound = round(R[int(self.id)] + self.score,3)
    def cal_total_score(self, obj):
        self.total_score = round(self.lower_bound + obj.score,3)
    def cal_upper_bound(self, obj):

        self.upper_bound = round(self.lower_bound + obj.score,3)
    def printo(self):
        print("id:{}, lower_bound:{}, total_score:{}, upper:{}".format(self.id,self.lower_bound,self.total_score,self.upper_bound))
