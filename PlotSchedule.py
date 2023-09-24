from datetime import datetime, timedelta
import math
#import Predictor

def plot_schedule(prioritylist, timegraph):
    schedule = {}
    priority_counter = 1
    priority_copy = prioritylist.copy()
    while prioritylist != {}:
        for task in priority_copy.keys():
            if priority_copy[task] == priority_counter:
                is_valid_min = False
                timecopy = timegraph.copy()
                while is_valid_min == False:
                    completion_time = min(timecopy)
                    if completion_time == 1440:
                        return schedule
                    task_time_index = timecopy.index(completion_time)
                    is_valid_min = check_valid_min(task_time_index, timecopy)
                    timecopy[task_time_index] = 2880                       
                start_time = get_time(task_time_index, timegraph)
                end_time = start_time + timegraph[task_time_index]
                schedule[task] = (start_time, end_time)
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

def check_valid_min(task_time_index, timegraph):
    for i in range(0, min([math.ceil(timegraph[task_time_index]/get_time_step(timegraph)), len(timegraph)-task_time_index-1])):
        if timegraph[task_time_index + i] == 1440:
            return False
    return True