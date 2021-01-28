def round_iter_element(nums_list):
    #result = [round(el) for el in nums_list]
    result = list(map(lambda x: round(x), nums_list))
    return result


#nums = [float(el) for el in input().split()]
nums = map(lambda el: float(el), input().split())
print(round_iter_element(nums))