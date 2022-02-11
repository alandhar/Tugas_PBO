def is_a_triangle (a, b, c):
    return a + b > c and b + c > a and c

def heron (a, b, c):
    P = (a + b + c) / 2
    return (P*(P - a) * (P - b) * (P - c) ** 0.5)
    
def area_of_triangle (a, b, c):
    if not is_a_triangle (a, b, c) :
        return None
    return heron(a, b, c)

print(area_of_triangle(1.0, 1.0, 2.0)** 0.5)