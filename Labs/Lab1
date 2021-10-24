#IMPORTS 
import numpy as np 
import random as rnd
import matplotlib.pyplot as plt

student = np.zeros((10,20),dtype = int)
student

masked_student = rnd.randint(0,10)
masked_student 
student[0,masked_student] = 1 

def update(arr,row_i): 
    for stud_i in range(len(arr[row_i])):
        
        left_student = arr[row_i-1][:][stud_i-1]
        if stud_i == range(len(arr[row_i]))[-1]: 
                right_student = arr[row_i-1][:][0]
        else: 
            right_student = arr[row_i-1][:][stud_i+1]
        #if student_yesterday and student_right_yesterday == 0 or student_yesterday
                #arr[row_i][stud_i] = 1 

classroom = np.zeros((10,10), dtype = int)
classroom[0,5] = 1 
classroom 

def n_iterate(arr):
    for row_i in range(len(arr)): 
        if row_i == 0: 
            pass 
        else: 
            update(arr,row_i)
            
n_iterate(student)

for row in range(len(classroom)): 
    for student in range(9):
        #if classroom[row][student] == 0 and sum((classroom[row][student-1]),(classroom[row][student+1]))== 1: 
        if classroom[row][student+1] + classroom[row][student-1] == 1: 
            # classroom[row][student] = 1 
            print('yes')

print(student)

def color(x,y):
    return (x*x + y*y + 2*x*y) % 5 
print (color) 

size = 200
grid = np.fromfunction(color, (10,20), dtype=int)
print(grid)

rgb = [[0,0,0],[255,0,0], [0,255,0], [0,0,255,], [255,255,255]]

#instantiate image array 
image = np.zeros((10,20,3), dtype = int)
image

for i in range(10):
    for j in range(20):
        image[i][j] = rgb[grid[i][j]]

%matplotlib inline 
import matplotlib.pyplot as plt 
plt.figure(figsize = (10,10))
plt.imshow(image, interpolation = 'none')
plt.show() 

plt.figure(figsize = (8,8))
plt.imshow(image, interpolation ='none')
plt.show() 

masked_student = rnd.randint(0,8)
masked_student 

plt.figure(figsize = (10,20))
plt.imshow(image, interpolation ='none')
plt.show() 











