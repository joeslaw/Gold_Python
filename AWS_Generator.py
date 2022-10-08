from random import randint
import random
import string

department = input("Enter your department: ")
department = department.lower()
random_number = 0

if department == 'marketing' or department == 'accounting' or department == 'finops':
    instance_number = int(input("Enter the number of EC2 instances you need: "))
    count = 1
    
    def get_random_string(length):
        result_str = ''.join(random.choice(string.ascii_letters) for i in range(5))
        return result_str
        
    while instance_number >= count:
        random_number = randint(10000, 99999)
        print("EC2-"+department+'-'+get_random_string(5)+str(random_number))
        count += 1
else: 
    print("You should not use this name generator as the departments currently supported are: Marketing, Accounting, and FinOps.")
