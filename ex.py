import statistics
data = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10]
mean_value = statistics.mean(data)
median_value = statistics.median(data)
mode_value = statistics.mode(data)
stdev_value = statistics.stdev(data)
variance_value = statistics.variance(data)

print("Mean:", mean_value)
print("Median:", median_value)
print("Mode:", mode_value)
print("Standard Deviation:", stdev_value)
print("Variance:", variance_value)

print(statistics.mean([1, 3, 5, 7, 9, 11, 13])) 
print(statistics.mean([1, 3, 5, 7, 9, 11])) 
print(statistics.mean([-11, 5.5, 3.4, 7.1, -9, 22])) 


print(statistics.median ([1, 3, 5, 7, 9, 11, 13])) 
print(statistics.median ([1, 3, 5, 7, 9, 11])) 
print(statistics.median([-11, 5.5, -3.4, 7.1, 9, 22])) 

# Calculate the mode 
print(statistics.mode ([1, 3, 3, 3, 5, 7, 7, 9, 11])) 
print(statistics.mode ([1, 1, 3, 5, 7, 9, 11])) 
print(statistics.mode(['red', 'green', 'blue', 'red']))

print(statistics.stdev ([1, 3, 5, 7, 9, 11])) 
print(statistics.stdev ([2, 2.5, 1.25, 3.1, 1.75, 2.8])) 
print(statistics.stdev ([-11, 5.5, 3.4, 7.1])) 
print(statistics.stdev([1, 30, 50, 100])) 
                      