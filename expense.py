print("***************Expenses Tracker******************")
d={}
ExpenseType=input("enter your expense type=")
m=int(input("expenditure on it="))
d[ExpenseType]=m
while True:
    z=input("select Add if you want to add new items=[Add/finish]")
    if z=="Add":
        ExpenseType=input("enter your expense type=")
        m=int(input("expenditure on it="))
        d[ExpenseType]=m
    elif z=="finish":
        break
print("your expenditure type and expense is as follows:")
k=list(d.keys())
v=list(d.values())
print(k)
print(v)
print("\n\n -----Daily Analysis***")
for i in range(len(k)):
    print("daily expenditure on type",k[i],"is",v[i])
print("total Daily Expenditure=",sum(d.values()))
print("\n\n -----monthly expenses analysis***")
for j in range(len(k)):
    print("mothly expenditure on type",k[j],"is",30*(v[j]))
print("monthly expenditure=",sum(30*v))
print("\n\n -----yearly expenditure analysis****")
for lm in range(len(k)):    
    print("yearly expenditure on type",k[lm],"is",365*(v[lm]))
print("yearly expenditure=",sum(365*v))
print("************THANK YOU********************")

    



 
