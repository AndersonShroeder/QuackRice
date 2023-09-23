from datetime import datetime, timedelta
import math
#import Predictor

def plot_schedule(prioritylist, timegraph):
    schedule = {}
    priority_counter = 1
    while prioritylist != {}:
        for task in prioritylist.keys():
            if prioritylist[task][0] == priority_counter:
                is_valid_min = False
                timecopy = timegraph.copy()
                while is_valid_min == False:
                    completion_time = min(timecopy)
                    task_time_index = timecopy.index(completion_time)
                    is_valid_min = check_valid_min(task_time_index)
                    timecopy[task_time_index] = 2880                       
                task_time = get_time(task_time_index, timegraph)
                schedule[prioritylist[task]] = task_time
                timegraph[task_time_index] = 1440
                priority_counter += 1
                del prioritylist[task]
    return schedule
                    
def get_time_step(timegraph):
    return 1440/len(timegraph)

def get_time(index, timegraph):
    return index*get_time_step(timegraph)

def interval_to_time(interval):
    base_time = datetime.strptime("00:00", "%H:%M")
    delta = timedelta(minutes=10)
    target_time = base_time + delta * interval
    return target_time.strftime("%H:%M")

def check_valid_min(task_time_index):
    for i in range(0, math.ceil(timegraph[task_time_index]/get_time_step(timegraph))):
        if timegraph[task_time_index + i] == 1440:
            return False
        else:
            return True

prioritylist = {"Stroke": [1, 2], "Goon": [2, 2], "Bust": [3, 2]}  

timegraph = [150, 150, 150, 150, 150, 150, 150, 140, 120, 120, 120, 120]

print(plot_schedule(prioritylist, timegraph))
