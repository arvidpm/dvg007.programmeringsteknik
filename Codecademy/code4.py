grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print (grade)

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    
    for i in scores:
        variance += (average - i) ** 2
    variance = variance / len(scores)
    return variance

def grades_std_deviation(variance):
    return variance ** 0.5

print_grades(grades)
print ("The sum of all grades:", grades_sum(grades))
print ("The average grade is:", grades_average(grades))
print ("The grade variance is:", grades_variance(grades))

variance = grades_variance(grades)
print ("The standard deviation is:", grades_std_deviation(variance))

