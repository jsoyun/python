
# 답지
# n = int(input())
n = 10
print('n',n)
 
#계산한 횟수를 저장하는 용이래!!!
d = [0] * (n+1) 
print("d",d)

for i in range(2, n+1):  #2부터하는이유는0,1은 나누어떨어지지 않아서 횟수가 걍 0이라서!
    d[i] = d[i-1] +1 #더하기 1을 하는 이유는 기존횟수느 = 이전 횟수에 + 1 식 늘어나니까. 
   #i가 3으로 나눠지는 값이면 
    if i %3 == 0:
        #숫자 3의 횟수는 = 이전 횟수에 하나더한 횟수거나, 3으로 나눈 값의 횟수에 하나 더한 횟수! 둘중에 더 작은 값!
        d[i] = min(d[i], d[i//3]+1)
        print("3d[i]:", d[i])
    if i%2 == 0:
        d[i] = min(d[i], d[i//2]+1)

    #헷갈리고 어려웠던 이유: 피보나치는 더한 값들을 정렬에 기록해서 간단했는데
    #얘는 횟수를 기록해서 인덱스가 "주어진 숫자" 역할을 했다. 그게 잘 안와닿았다.
    # 즉 인덱스 3은 숫자 3이고 숫자 3이 몇 번의 횟수를 거쳐 1이 되냐. 를 구하는 것. 
    #횟수를 기준으로 하니, 현재 횟수가 이전횟수 + 1이다라는게 겨우 이해되었다. 
    # 숫자가 2나 3으로 나눠지는 경우 : 예) 숫자가 6이면 이전5의 횟수+ 1을 하면 4가 되는데, 숫자 6은 2로 나눠지기때문에
    # 최솟값으로 비교를 한다. "이전5의 횟수+ 1"  과 "d[6//3] 즉 d[2] 숫자2의 횟수에 1을 더한 값"을 비교.
    #나는 하나하나 값 넣어서 적어보면서 이해했다 ㅎㅎㅎ
print(d[n])
