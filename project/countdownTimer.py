import time


def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeFormat = '{:02d}:{:02d}'.format(mins, secs)
        print("Countdown Time : ", timeFormat)
        time.sleep(1)
        time_sec -= 1
    print("Time Out")


countdown(1200)
