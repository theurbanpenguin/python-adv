import numpy as np
# Sample dataset of exam scores
exam_scores  = np.genfromtxt('data.csv', delimiter=',', usecols=(1,))

# Calculate the mean (average) score
mean_score = np.mean(exam_scores)

# Calculate the median score
median_score = np.median(exam_scores)

# Calculate the standard deviation
std_deviation = np.std(exam_scores)

# Calculate the variance
variance = np.var(exam_scores)

# Find the maximum and minimum scores
max_score = np.max(exam_scores)
min_score = np.min(exam_scores)

# Print the results
print(f"Mean Score: {mean_score:.2f}")
print(f"Median Score: {median_score:.2f}")
print(f"Standard Deviation: {std_deviation:.2f}")
print(f"Variance: {variance:.2f}")
print(f"Maximum Score: {max_score:.2f}")
print(f"Minimum Score: {min_score:.2f}")

