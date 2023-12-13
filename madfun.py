# madfun.py project
# 11-12-2023
# by Steven D. Garcia

# import math

# drawing_rating = input(("Using a scale of 1.0 to 10.0 Please rate this drawing. "))
# user_rating = 8.9
# print("This is the absolute number: ", abs(user_rating))
# print("This is the rounded number: ", round(user_rating))
# print("This is the square root of the number: ", math.sqrt(abs(round(user_rating))))

# ***** Shorter code solution *****

import math
drawing_rating = eval(input(("Using a scale of 1.0 to 10.0 Please rate this drawing. ")))

print("This is the absolute number: ", abs(drawing_rating))
print("This is the rounded number: ", round(drawing_rating))
print("This is the square root of that number: ", math.sqrt(abs(round(drawing_rating))))

