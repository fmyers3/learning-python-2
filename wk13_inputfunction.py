
print("wk 13")

print("Allow the user to input how many EC2 instances they want names for and output the same amount of unique names")
print("Allow the user to input the name of their department that is used in the unique name")
print("Generate random characters and numbers that will be included in the unique name")

import random
import string


instance_amount = int(input("How mamy instances: "))

instance_department = str(input("Department name: "))

instance_characters = (string.ascii_letters + string.digits)
instance_unique_name = ''.join(random.sample(instance_characters, 5))

print(instance_unique_name)