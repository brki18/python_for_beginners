# import common
import common as c
from common import num_sum, num_power
from new_package import num_operations
# from new_package.num_operations import num_multiply
import new_package.num_operations as num

# from common import num_power

sum = num_sum(10, 23)

power = num_power(6)

multiply = num.num_multiply(34, 22)

print(sum)
print(power)
print(multiply)
