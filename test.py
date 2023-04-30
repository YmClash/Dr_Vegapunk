import random
import secrets
from ymc_LIB import compare_list
from ymc_LIB import output_size


# random.seed('momo')


numb1 = [random.randint(1,100) for i in range(10)]
numb2 = [secrets.randbelow(100)for e in range(10)]


print(numb1)
print(numb2)


compare_list(numb1,numb2)


def output_size(input,kernel_size,convo_n):
    input_size = input
    stride = 1
    padding = 0
    for i in range(convo_n):
        get_output_size = (input_size - kernel_size + 2 * padding ) // stride +1
        print(f'Output size afer conv Layers: {output_size}')


output_size(28,3,4)