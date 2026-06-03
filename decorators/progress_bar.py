import random

def progress_bar(task_name):
    print(f"{task_name} STARTING . . .")
    # Generate a random decimal number between given range
    delay = random.uniform(1,2)
    return delay