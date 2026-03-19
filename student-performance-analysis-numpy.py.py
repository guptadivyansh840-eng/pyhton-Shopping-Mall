import numpy as np
studentmarks=np.array([[1,45,34,45,23],[2,43,54,32,56],[3,45,23,67,44],[4,34,65,53,67],[5,65,43,45,67],[6,54,54,45,56],[7,56,23,54,45],[8,45,55,53,56],[9,76,45,77,56],[10,67,90,45,34]])
"""#here first element of every array represent roll number of student
""the rest element represent the marks of for subjects in order maths,english
hindi,science"""
#calculating marks of each student
count=0
for x in studentmarks:
    total=sum(x[1:5])
    percent=(total/400)*100
    count+=1
    if percent>90:
        g="A"
    elif 60<percent<90:
        g="B"
    else:
        g="c"
    z=np.array([(x[0]),total,int(percent),g])
    print(z)#you will get array in the format
            #[rollnumber,total marks,percent,grade]

          

