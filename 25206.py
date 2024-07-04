import sys
input = sys.stdin.readline

score_tb = {'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0.0}
credit_sum = 0
score_sum = 0
for i in range(20):
    name,credit,score = input().split()
    if score == 'P':
        continue
    credit_sum += float(credit)
    score_sum += float(credit) * score_tb[score]

print(round(score_sum/credit_sum,6)) 