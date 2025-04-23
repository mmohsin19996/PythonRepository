from datetime import datetime

def show_time():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

print("Current time is:", show_time())
