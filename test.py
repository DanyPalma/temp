# written by Daniel Palma (root@ucf.edu)
# python version: 3.10.6

from drive_train import drive_train


front_cogs = [38, 30]
rear_cogs = [28, 23, 19, 16]
initial_gear_combination = [38, 28]
target_ratio = 1.6
test_drive_train = drive_train(front_cogs, rear_cogs)

result = test_drive_train.get_gear_combination(target_ratio)

if result[0] != 30 or result[1] != 19 or len(result) !=2:
    print("get_gear_combination test failed")
else:
    print("get_gear_combination test passed")
    


test_drive_train.get_shift_sequence(target_ratio, initial_gear_combination)
'''
The output should be as follows:

Shift the front gear from the 38 tooth cog, to the 30 tooth cog.     
Then, shift the rear gear from the 28 tooth cog, to the 19 tooth cog.

'''

test_drive_train.formatted_shift_sequence(target_ratio, initial_gear_combination)

'''
The output should be as follows:

Front: 38, Rear: 28, Ratio: 1.357
Front: 30, Rear: 28, Ratio: 1.071
Front: 30, Rear: 23, Ratio: 1.304
Front: 30, Rear: 19, Ratio: 1.579
'''