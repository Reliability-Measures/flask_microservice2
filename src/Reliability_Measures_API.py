import Algorithmia
from statistics import pstdev


def calculate_std(param):
    user_list = list(param['elements'])
    std_value = float(pstdev(user_list))
    return {'Std': round(std_value, 3)}


# API calls will begin at the apply() method, with the request body passed as 'input'
# For more details, see algorithmia.com/developers/algorithm-development/languages
def apply(input):
    return calculate_std(input)


# test
input = 'Farrukh'
client = Algorithmia.client('simxId1NtOQOhWCmD5Si5IchZSm1')
algo = client.algo('reliabilitymeasures/Reliability_Measures_API')
algo.set_options(timeout=300) # optional
print(algo.pipe(input).result)