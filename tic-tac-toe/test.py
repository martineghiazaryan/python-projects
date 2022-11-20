# def solution(a):
#     height = sorted([i for i in a if i != -1])
#     for i,n in enumerate(a):
#         if n == -1:
#             height.insert(i,n)
#     return height

# print(solution([-1, 150, 190, 170, -1, -1, 160, 180]))
#---------------------------------------------------------
# def solution(s):
#     for i in range(len(s)):
#         if s[i] == '(':
#             start = i
#         if s[i] == ')':
#             end = i
#             return solution(s[:start] + s[start+1:end][::-1] + s[end+1:])
#     return s


# solution("foo(bar(baz))blim")
#----------------------------------------------------------

# A = [1,3,2,2]
# B = [2,1,2,3]

# newlist = [a!=b for a,b in zip(A,B)]
# print(newlist,sum(newlist))

#----------------------------------------------------------

# def solution(yourLeft, yourRight, friendsLeft, friendsRight):
#     return {yourLeft, yourRight} == {friendsLeft, friendsRight}


# print(solution(10,15, 15,10))

#----------------------------------------------------------
# def solution(ipv4):
#     ipv4 = ipv4.split('.')
#     if len(ipv4)== 4:
#         for item in ipv4:
#             if 0 <= int(item) <= 255:
#                 return True
#         return False
#     return False

# print(solution('172.26.250.86'))
#--------------------------------------------------------------

# def solution(m):
#     r = len(m)
#     c = len(m[0])
#     result = []
#     for i in range(1, r-1):
#         row = []
#         for j in range(1, c-1):
#             row.append(sum([m[i+k][j+l] for k in [-1,0,1] for l in [-1,0,1]])//9)
#         result.append(row)
#     return result

# print(solution([[7, 4, 0, 1], 
#                 [5, 6, 2, 2], 
#                 [6, 10, 7, 8], 
#                 [1, 4, 2, 0]]))
#---------------------------------------------------------------
# def solution(inputString):
#     return ''.join((chr(ord(i)+1) if i!="z" else "a" for i in inputString))

# print(solution('crazy'))

#---------------------------------------------------------------

# def solution(a, k):
#     sums = list()
#     for i in range(len(a)-1):
#         sums.append(sum(a[i:k]))
#         k += 1
#     return max(sums)    

# print(solution([2, 3, 5, 1, 6],2))

#----------------------------------------------------------------

# def solution(n):
#     d=0
#     while n>=10:
#         n=sum([int(i) for i in str(n)])
#         d+=1
#     return d

# print(solution(877))