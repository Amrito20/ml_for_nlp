import numpy as np 

sample = np.array([1,2,3,4,5,6])
for i in sample:
    print(i)
# use of enumerate(index+num)
for i,j in enumerate(sample):
    print(i,j)

#flat = 2d array, fast usecase
sample2 =np.array([[1,2,3,4,5],[6,7,8,9,10]])    

for i in sample2.flat:
    print(i)

for i,j in np.ndenumerate(sample2):
    print(i,j)

for i,j in enumerate(sample2.flat):
    print (i,j)

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

add_arr = arr1+arr2
print ("Array adding")
print(add_arr)

#mean calculating
mean= np.mean(arr1)
print("mean=", mean)

#standart deviation calculating
std= np.std(arr1)
print ("Std:", std)

#min and max value
print("Min=",np.min(arr1))
print ("Max=",np.max(arr1))

#armin & argmax function
print(np.argmin(arr1))
print(np.argmax(arr1))

arr3 = np.array([4,2,9,2,3,1])

#25th percentile (1st quartile)
perc_25th= np.percentile(arr3, 25)
print("25th Percentile: ", perc_25th)

#median 
median= np.median(arr3)
print("Median: ", median)

#75th percentile
perc_75= np.percentile(arr3, 75)
print("75th Percentile: ", perc_75)

# Generate Randon Array
arr4 =np.random.rand(8)
arr5 =np.random.rand(8)

# Calculatin the correlation coefficient
correlation_coefficient= np.corrcoef(arr4,arr5)
print(correlation_coefficient)

