


def left_aligned_star(n):
    for i in range(1,n+1):
        print(' '*(n-i)+'*'*i)

def right_aligned_star(n):
    for i in range(1,n+1):
        print('*'*i+' '*(n-i))

def pyramid_star(n):
    for i in range(0,n):
       # print(' '*(n-i-1)+ '*'*(2*i + 1) +' '*(n-i-1))
       print(' ' * (n - i - 1) + '*' * (2 * i + 1))

def inv_pyramid_star(n):
    for i in range(0,n):
        #Stars at line i=(2n−1)+  i⋅(−2)  =2n−1−2i=2(n−i)−1
        print(' '*i + '*'*(2*(n-i)-1))


def diamond_star(n):
    n = 5
    # Upper part
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))
    # Lower part
    for i in range(n - 2, -1, -1):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))

def inc_no_rt_Tringle(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=' ')
        print()

def continous_no_tri(n):
    count =1
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(count,end=' ')
            count +=1
        print()

def continous_no_rt_aligned_tri(n):
    count = 1
    for i in range(1, n + 1):
        print(' ' * (n - i + 1), end='')
        for j in range(1, i + 1):
            print(count, end=' ')
            count += 1
        print()

def continous_no_rt_aligned_tri_spaced(n):
    count = 1
    width = len(str(n * (n + 1) // 2))  # Width based on largest number
    for i in range(1, n + 1):
        print('   ' * (n - i), end='')  # 3 spaces per missing number for alignment
        for j in range(1, i + 1):
            print(f"{count:0{width}}", end=' ')
            count += 1
        print()

def no_pyramid(n):
    count=1

def inverted_number_triangle(n):
    for n in range(n,0,-1):
        for j in range(1,n+1):
            print(j,end=' ')
        print()

#pascal triangle is the tringale with binominal cofficient C(n, k) = n! / (k! * (n - k)!)
def factroial(n):
    memo ={}
    if n in memo: return memo[n]
    if n==0:
        return 1
    else:
        fact=n*factroial(n-1)
        memo[n] = fact
        return fact

# def factroial(n):
#     return 1 if n == 0 else n * factroial(n - 1)

def pascal_triangle(n):
    for i in range (n):
        print(' '*(n-i),end='')
        for j in range(i+1):
            val = factroial(i)//(factroial(i-j)*factroial(j))
            print(val,end= ' ')
        print()

def diamond(n):
    for i in range(1, n + 1):
        print(' ' * (n - i), end='')
        print(str(i) * (2 * i - 1))
    for i in range(n - 1, 0, -1):
        print(' ' * (n - i), end='')
        print(str(i) * (2 * i - 1))

right_aligned_star(5)
#left_aligned_star(5)
#pyramid_star(5)
#inv_pyramid_star(5)
#diamond_star(5)
#inc_no_rt_Tringle(5)
#continous_no_tri(5)
#continous_no_rt_aligned_tri(5)
#continous_no_rt_aligned_tri_spaced(5)
#inverted_number_triangle(5)
#pascal_triangle(5)
#diamond(5)