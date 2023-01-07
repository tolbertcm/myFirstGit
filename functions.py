def hello(S):
    name_p = S
    print('Hello World '+ name_p)

hello('Cindy')

#return string

def square_n(n):
    s_n=n**2
    return s_n

x = square_n(2)
print(x)

def kg_pd(kg):
    pd_r =(2.2*kg)
    return(pd_r)
weight_j=kg_pd(105)
print(weight_j)

#pounds to kilograms


#Celsius to Fahrenheit
def c_f(c):
    c_deg =(c*1.8+32)
    return(c_deg)
lagos_deg =c_f(20)
print(lagos_deg)

#Fahrenheit to Celsius

def f_c(f):
    f_deg=((f-32)*5/9)
    return(f_deg)
atlanta_deg =f_c(70)
print(atlanta_deg)

#John's test
x1 =5
x2 =10
def add_2_n(x1,x2):
    x =x1*x2
    return x

sum_n= add_2_n(x1,x2)
print (sum_n)


