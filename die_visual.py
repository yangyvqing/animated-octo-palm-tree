from die import Die

# 创建一个D6
die = Die()

# 投掷几次骰子并将结果储存在一个列表
results = []
for roll_num in range(2):
    result = die.roll()
    results.append(result)

print(result)