N = int(input())
pos = [0] * N
flag_a = [False] * N
flag_b = [False] * (N*2-1)
flag_c = [False] * (N*2-1)
cnt = [0]
def set(i:int)->None:
    for j in range(N):
        if (not flag_a[j]
           and not flag_b[i+j]
           and not flag_c[i-j+(N-1)]):
            pos[i]=j
            if i == (N-1):
                cnt[0] +=1
            else :
                flag_a[j] = flag_b[i+j] =flag_c[i-j+(N-1)] = True
                set(i+1)
                flag_a[j] = flag_b[i+j] =flag_c[i-j+(N-1)] = False

set(0)
print(cnt[0])

# todo 맞긴 맞았는데 너무 느림, 그리고 cnt를 int로 하면 왜 안되는지 ? 