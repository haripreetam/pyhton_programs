import time

def stopwatch():
    input("Press Enter to start the stopwatch.")
    start_time = time.time()
    #time.sleep(1)
    input("Press Enter to stop the stopwatch.")
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time} seconds")

stopwatch()