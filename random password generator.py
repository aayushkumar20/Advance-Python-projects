import random

lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
symbols="@#$%^!~<>:;'/?"
all=lower+upper+numbers+symbols
#print("enter length of required password")
length=20
output="".join(random.sample(all,length))
print("password",output)
