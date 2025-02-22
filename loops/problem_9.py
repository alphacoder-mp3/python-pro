import time

#Implement an exponential backoff strategy that doubles the delay with each retry, up to a maximum of 60 seconds, but stops after 5 retries.
#
def exponential_backoff(max_retries=5, max_delay=60):
    delay = 1
    for retry in range(max_retries):
        try:
            # Attempt the operation that may fail
            # If successful, break out of the loop
            print(f"Attempt {retry + 1}",f"Delay: {delay}")
            # Simulate operation
            if retry == max_retries - 1:
                print("Operation succeeded")
                break
            raise Exception("Operation failed")
        except Exception as e:
            print(e)
            if retry < max_retries - 1:
                time.sleep(delay)
                delay = min(delay * 2, max_delay)
            else:
                print("Max retries reached. Operation failed.")

exponential_backoff()


wait_time = 1
max_tries = 5
attempts = 0

while attempts < max_tries:
    print(f"Attempt {attempts + 1}", f"Wait time: {wait_time}")
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1
