# Call a different function from the statistics module

import statistics

data = [1, 5, 33, 12, 46, 33, 2]

print("\nThe median is ", statistics.median(data))
print("The mean is ", statistics.mean(data))
print("The mode is ", statistics.mode(data), "\n")


print("The low median is ", statistics.median_low(data))
print("The high median is ", statistics.median_high(data),"\n")

print("The population standard deviation of the data is ", statistics.pstdev(data))
print("The population variance of the data is ", statistics.pvariance(data), "\n")

print("The sample standard deviation of the data is ", statistics.stdev(data))
print("The sample variance of the data is ", statistics.variance(data), "\n")



