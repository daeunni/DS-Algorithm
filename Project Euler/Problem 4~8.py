# Problem 5 : 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 얼마입니까?  (최소공배수 문제)

for i in range(20,1000000000,20):    # 20씩 뛰면서 진행
  for a in range(1,20):
    if i%a != 0 :   # 나머지가 0이 아니면 멈추고 다음수로, 0이면 a 바꿔가면서 계속 진행
      break
    if a >= 19:
      print (i)

# Problem 6 : 1부터 100까지 "제곱의 합"과 "합의 제곱"의 차는?

num = 1
a = 0  # 합의 제곱
b = 0  # 제곱의 합
while (num<=100):
  a += num
  b+= num**2
  num += 1    # 합의제곱
print('제곱의 합과 합의 제곱의 차 : ', a**2 - b)

# Problem 7 : 10001번째의 소수 구하기

num = 1   
i = 1
# 우선 True로 설정
while (num<=10002):
    i +=1 
    result = True  # True, False 이용
    for j in range(2, i):
      if i % j ==0:
        result = False
        break
        
    if result == True:
      num+=1
      if num == 10002:
        print('10001번째 소수 : ', i)   # 51초정도 걸림

"""### cf) 에리토스테네스의 체
- 소수를 구하는 알고리즘
- 찾고자 하는 자연수를 배열로 나열하여 그 중에 소수의 배수들을 전부 지워나가면 남는 수가 소수가 됨 
- 시간복잡도를 매우 줄일 수 있음
"""

n = 104743
a = [False, False] + [True] * (n-1)   # False 두번, True가 n-1번 등장
소수 = []

for i in range(2, n+1):
  if a[i] == True:
    소수.append(i)  # 우선 소수로 추가
    
    for j in range(2*i, n+1, i):   # 소수의 배수를 지워간다 
      a[j] = False

print(소수)
print(len(소수))

# Problem 8 : 1000자리 수 안에서 이어지는 5개 숫자의 곱 중 최댓값은?
number = "73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450"

product = []

for i in range(5, len(number)+1, 5):
  a = 1
  for j in range(i-5, i):
    a *= int(number[j])
  product.append(a)

print(product)
# print('연속한 5개의 숫자 곱 중 가장 큰 수 : ', max(product))

######### 왜틀린걸까.......

example = "73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450"

maximum = 0 
for i in range(len(example)-4): 
  num = int(example[i]) * int(example[i + 1]) * int(example[i + 2]) * int(example[i + 3]) * int(example[i + 4]) 
  if num > maximum: 
    maximum = num 
print(maximum)
