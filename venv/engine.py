import time


def run(step_rate=0.0):
    # refresh rate
    try:
        set_rate = float(step_rate)
    except ValueError as e:
        print("Error while converting step rate to float.\n{}".format(str(e)))
        exit()
    # this will be for the position of the objects
    while True:
        
        time.sleep(step_rate)
