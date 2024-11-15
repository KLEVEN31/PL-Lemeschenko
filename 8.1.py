X = 3  
Y = 4  
Z = 5  
T = 6 
def a(b, h):
    return 0.5 * b * h

def c(m, n):
    return m * n

def d(X, Y, Z, T):
    area = a(X, Y)
    areaa = c(Z, T)
    total_area = area + areaa
    return total_area
total_area = d(X, Y, Z, T)
print(total_area)
