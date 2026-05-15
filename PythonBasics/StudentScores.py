# A School’s Student Performance
# Data
# You are tasked with analyzing the performance of students in different
# subjects. The school has conducted exams for three subjects: Math,
# Science, and English.
# Each student has scored a mark between 0 and 100
# in each subject.

# You are given a dataset in the form of a 2D NumPy array, where each
# row represents a student, and each column represents a subject. Your
# task is to:


# Create a NumPy array representing the students' scores for Math, Science, and English.
# Calculate the total score for each student by adding their scores across all subjects.
# Find the average score of all students for each subject (i.e., the mean score for Math, Science, and English).
# Identify the student with the highest score in Math, Science, and English individually.
# Find the number of students who scored above 75 in all three subjects.

import numpy as np

# 1. Create a NumPy array (rows = students, columns = subjects)
# Columns: Math, Science, English
scores = np.array([
    [85, 78, 90],
    [72, 88, 65],
    [95, 92, 89],
    [60, 70, 75],
    [80, 85, 88]
])

print("Student Scores (Math, Science, English):\n", scores)

# 2. Total score for each student
total_scores = np.sum(scores, axis=1)
print("\nTotal score of each student:\n", total_scores)

# 3. Average score for each subject
average_scores = np.mean(scores, axis=0)
print("\nAverage scores (Math, Science, English):\n", average_scores)

# 4. Student with highest score in each subject
highest_math = np.argmax(scores[:, 0])
highest_science = np.argmax(scores[:, 1])
highest_english = np.argmax(scores[:, 2])

print("\nStudent with highest Math score: Student", highest_math + 1)
print("Student with highest Science score: Student", highest_science + 1)
print("Student with highest English score: Student", highest_english + 1)

# 5. Number of students scoring above 75 in all three subjects
above_75_all = np.sum(np.all(scores > 75, axis=1))
print("\nNumber of students scoring above 75 in all subjects:", above_75_all)
