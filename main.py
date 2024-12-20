import json
import time
from datetime import datetime, timedelta
from termcolor import cprint
import random


def load_tasks():
    with open('/Users/sachinnaik/Desktop/AlgoTrading/TimeManagement/tasks.json','r') as f:
        tasks = json.load(f)
    return tasks


def get_tasks_schedule(tasks):
    task_start_time = datetime.now()
    schedule = []
    for task, minutes in tasks.items():
        end_time = task_start_time + timedelta(minutes=minutes)
        schedule.append((task,task_start_time,end_time))
        task_start_time = end_time
    return schedule

def main():
    tasks = load_tasks()
    schedule = get_tasks_schedule(tasks)
    cur_index= 0

    while 1:
        now = datetime.now()
        cur_task , start_time , end_time = schedule[cur_index]
        rem_time = end_time - now 
        rem_minutes = int(rem_time.total_seconds()// 60)

        print('')

        for index , (task,s_time,e_time) in enumerate(schedule):
            if index < cur_index :
                print(f'{task} done: {e_time.strftime("%H:%M")}')
            elif index == cur_index:
                if rem_minutes < 2:
                    cprint('{task} <2m left!!  ','white','on_red',attrs=['blink'])
                elif rem_minutes < 5:
                    cprint(f'{task} - {rem_minutes} mins','white','on_red')
                else :
                    cprint(f'{task} - {rem_minutes} mins','white','on_blue')
            else:
                print(f'{task} @ {s_time.strftime("%H:%M")}')

        
        if now >= end_time:
            cur_index += 1
            if cur_index >= len(schedule):
                cprint("All Tasks are completed", 'white', 'on_green')
                break

        time.sleep(15)
    
main()

        
