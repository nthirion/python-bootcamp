from datetime import datetime
from datetime import date
from datetime import timedelta

import time

def pomodoro_counter(time_set):
    current_time = datetime.today()
    pomo_time = current_time + timedelta(seconds=int(time_set)*60)
    while datetime.today() < pomo_time:
        time.sleep(5)
        print("count down ", (pomo_time - datetime.today()).seconds)


if __name__ == '__main__':
    timer = input("Pomodoro time in minutes? ")
    pomodoro_counter(timer)
