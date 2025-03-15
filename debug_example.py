def calculate_sum(numbers):
    total = 0
    for num in numbers:
        # 方法1：使用 breakpoint()
        total += num
    return total

def calculate_average(numbers):
    import pdb
    
    # 方法2：使用 pdb.set_trace()
    pdb.set_trace()
    
    if not numbers:
        return 0
    total = calculate_sum(numbers)
    return total / len(numbers)

# 测试数据
numbers = [1, 2, 3, 4, 5]
average = calculate_average(numbers)
print(f"Average is: {average}") 