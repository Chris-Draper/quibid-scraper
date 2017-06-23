import random
import time

input("Testing timer functionality. Press enter to continue")
end_wait = random.randint(1, 60)
start_wait = time.time()
duration_wait = 0
print("Random wait time is {} seconds".format(end_wait))
while end_wait > duration_wait:
	duration_wait = time.time() - start_wait
print("Waited exactly {} seconds".format(duration_wait))
print("Now preform action after timer expires")