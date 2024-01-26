# written by Daniel Palma (root@ucf.edu)
# python version: 3.10.6

class drive_train:
    # constructor
    def __init__(self, front_cogs, rear_cogs):
        self.front_cogs = front_cogs
        self.rear_cogs = rear_cogs
        
    # tostring method
    def __str__(self):
        return f"front cogs: {self.front_cogs}\nrear cogs:{self.rear_cogs}"
    
    # determines the gear combination providing the closest ratio that is less than or equal to the target ratio
    # we have the print_result flag to let us use this in our other methods and specify to not print the ideal cogs 
    def get_gear_combination(self, target_ratio, print_result=True):
        max_ratio = 0.0
        best_cogs = []

        for f_cog in self.front_cogs:
            for r_cog in self.rear_cogs:
                current_ratio = round(f_cog/r_cog,3)
                if current_ratio <= target_ratio:
                    if current_ratio > max_ratio:
                        max_ratio = current_ratio
                        best_cogs = [f_cog, r_cog]
                        
        ideal_gear_combination = best_cogs
        
        if print_result:
            print(f"Front: {best_cogs[0]}, Rear: {best_cogs[1]}, Ratio: {max_ratio}")
        
        return ideal_gear_combination
                
        
    # This method will return a shift sequence to traverse from the initial gear combination to a gear combination with a closest ratio that is less than or equal
    # to the target ratio. we first shift the front gear, then the rear gear.
    def get_shift_sequence(self, target_ratio, initial_gear_combination):
        
        current_ratio = round(initial_gear_combination[0] / initial_gear_combination[1], 3)
        
        # if we are already at the target ratio exit early
        if target_ratio == current_ratio:
            print("You are already at the target ratio")
        
        else: 
            
            #find ideal gears
            ideal_gears = self.get_gear_combination(target_ratio, print_result=False)
            
                    
            print(f"Shift the front gear from the {initial_gear_combination[0]} tooth cog, to the {ideal_gears[0]} tooth cog.")
            print(f"Then, shift the rear gear from the {initial_gear_combination[1]} tooth cog, to the {ideal_gears[1]} tooth cog.")

    
    # this method will produce a formatted shift sequence for a given target ratio and initial gear combination
    def formatted_shift_sequence(self, target_ratio, initial_gear_combination):
        
        current_ratio = round(initial_gear_combination[0] / initial_gear_combination[1], 3)
        
        # if we are already at the target ratio exit early
        if target_ratio == current_ratio:
            print("You are already at the target ratio")
        
        else: 
            front_cogs = self.front_cogs
            rear_cogs = self.rear_cogs
            
            #find ideal gears
            ideal_gears = self.get_gear_combination(target_ratio, print_result=False)
        
            
            front = front_cogs.index(initial_gear_combination[0])
            rear = rear_cogs.index(initial_gear_combination[1])
            
            print(f"Front: {front_cogs[front]}, Rear: {rear_cogs[rear]}, Ratio: {current_ratio}")
            
            # first shift the front gear to the target gear
            while front_cogs[front] != ideal_gears[0]:
                if front_cogs[front] < ideal_gears[0]:
                    front -= 1
                elif front_cogs[front] > ideal_gears[0]:
                    front += 1
                current_ratio = round(front_cogs[front] / rear_cogs[rear], 3)
                print(f"Front: {front_cogs[front]}, Rear: {rear_cogs[rear]}, Ratio: {current_ratio}")
                    
                    
            # then shift the rear to the target gear
            while rear_cogs[rear] != ideal_gears[1]:
                if rear_cogs[rear] < ideal_gears[1]:
                    rear -= 1
                elif rear_cogs[rear] > ideal_gears[1]:
                    rear += 1
                    
                current_ratio = round(front_cogs[front] / rear_cogs[rear], 3)
                print(f"Front: {front_cogs[front]}, Rear: {rear_cogs[rear]}, Ratio: {current_ratio}")
