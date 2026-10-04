from plyer import notification
import time

def water_reminder():
    # interval_second = interval_minutes*60

    print("Water Drinking Reminder Started")
    # print(f"You will get a notification every {interval_minutes} minutes \n")

    while True :
        # time.sleep(interval_second)
        notification.notify(
            title = "Drinking Water",
            message = "Time to drinking water and stay hydrated.",
            timeout=10
        )
        time.sleep(3)
water_reminder()