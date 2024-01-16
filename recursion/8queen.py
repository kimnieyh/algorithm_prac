# 각 열에 퀸을 1개 배치하는 조합을 재귀적으로 나열하기 
# 각 행에 퀸을 1개 배치하는 조합을 재귀적으로 나열하기
# 대각선 방향에 퀸을 겹치지 않도록 나열 

pos = [0] * 8       # 각 열에 퀸을 배치
flag_a = [False] * 8 # 각 행에 퀸을  배치했는지
flag_b = [False] * 15 # 대각선 방향 왼쪽아래 오른쪽위 배치 했는지
flag_c = [False] * 15 #

def put() -> None:
    print(pos)
    for i in range(8):
        for j in range(8):
            print('●' if pos[i]==j else '◌',end='') 
        print()
    print()

def set(i :int) ->None :
    for j in range(8):
        if(not flag_a[j]
           and not flag_b[i+j]
           and not flag_c[i-j + 7]): # +7은 양수로 만들기 위함
            pos[i] = j #퀸을 j행에 배치
            if i == 7: # 모든 열에 퀸 배치 완료하면
                put()  
            else:
                flag_a[j] = flag_b[i+j] = flag_c[i-j + 7] = True
                set(i+1) # 다음 열에 퀸을 배치
                flag_a[j] = flag_b[i+j] = flag_c[i-j + 7] = False
            

set(0)