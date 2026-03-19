```python
print("*************** Expenses Tracker ******************")

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

print("\nYour expenditure type and expense is as follows:")

k=list(d.keys())
v=list(d.values())

print(k)
print(v)

print("\n\n -----Daily Analysis-----")

for i in range(len(k)):
    print("daily expenditure on type",k[i],"is",v[i])

print("total Daily Expenditure=",sum(d.values()))

print("\n\n -----Monthly Expenses Analysis-----")

for j in range(len(k)):
    print("monthly expenditure on type",k[j],"is",30*(v[j]))

print("monthly expenditure=",sum(v)*30)

print("\n\n -----Yearly Expenditure Analysis-----")

for lm in range(len(k)):    
    print("yearly expenditure on type",k[lm],"is",365*(v[lm]))

print("yearly expenditure=",sum(v)*365)

# Highest expense category
max_expense=max(d.values())
for key,value in d.items():
    if value==max_expense:
        print("\nhighest daily expense category is",key,"=",value)

# Lowest expense category
min_expense=min(d.values())
for key,value in d.items():
    if value==min_expense:
        print("lowest daily expense category is",key,"=",value)

print("************ THANK YOU ********************")
```
