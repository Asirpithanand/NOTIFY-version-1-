# importing all module's
from plyer import battery, notification
import time

while True:
    batteryinfo = battery.status   #this will get the current battery percentage  and  whether battery is charging or not

    # storing the information in separate variable
    info1 = batteryinfo.get("percentage") 
    info2 = batteryinfo.get("isCharging") 

    if info2 == False:
        notification.notify(
                    title='NOTIFY',
                    message= f"{info1}% REMAINING | STATUS UNPLUGGED",
                    app_name='NOTIFY',
                    timeout=15, # the notification will stay on screen for 10 sec
                    app_icon = " "  # copy and paste the path of the image attached with this repo
                )
        print('Program Finished')
        break    # breaking the loop once the condition becomes true

    elif info1 >= 90 and info2 == True: 
        notification.notify(
                    title='NOTIFY',
                    message= f" BATTERY AT {info1}% | DISCONNECT CHARGER",
                    app_name='NOTIFY',
                    timeout=15, # the notification will stay on screen for 10 sec
                    app_icon = " "  # copy and paste the path of the image attached with this repo
                )
        print('Program Finished')
        break    # breaking the loop once the condition becomes true
    time.sleep(60) # programe will run every min
