from stack import Stack

def recur(n:int) -> int:
	s = Stack(n)
	while True:
		# s.dump()
		# print(n)
		if n>0 :
			s.push(n) # n값을 push 
			n = n-1
			continue
		if not s.is_empty(): # stack이 비어있지 않으면
			n = s.pop() # 저장한 값을 n에 팝
			print(n)
			n = n-2
			continue
		break

x = int(input('정숫값을 입력하세요.'))

recur(x)