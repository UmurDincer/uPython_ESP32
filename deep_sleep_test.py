import machine, usys

print("Reset cause: ", machine.reset_cause())

#check if the device woke from deep sleep

if machine.reset_cause() == machine.DEEPSLEEP_RESET: # if you are testing for light sleep, use machine.SOFT_RESET
    print("Woke from a deep sleep.")
    usys.exit() #this will proframmatically break the execution of this script and return to shell
else:
    print("Going to sleep for 10 seconds..")
    machine.deepsleep(10000)
    #can be also used machine.lightsleep(1000) to place the ESP32 in light sleep(retains RAM)