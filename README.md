# Kickstart-2020-round-a-Workout

We are looking for the minimum difficulty possible after k trainings

my approach for this problem was to find the max absolute value of the difference between two consecutives element of the list
so i insert at the middle the average of that two values
i do it while it is possible and create a new list of absolute value of such differences described above
and at the end i return the max of that list

PS: it works for all test cases on my pc but on the contest interpreter only the first test works and the second return a 
Time Limit error
