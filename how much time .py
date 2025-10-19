# A program that calculate how much time I spent on a course
total_sec = int (input ("Enter the total time of the course in seconds: \n"))
print (f"the time yo spent on the course is {total_sec // 3600} hours {total_sec % 3600 // 60} minutes and {total_sec % 60} seconds.")