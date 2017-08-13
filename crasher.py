import time

# This file will crash Python. It involves RecursionErrors and loops.
# If you have a low-capability computer, you may not want to run this file.

# --- HOW IT WORKS ---
# Usually, Python has RecursionErrors to stop it from crashing when
# a program loops too much. But this program uses exception handling to ensure that
# when it does, the whole thing simply starts again. 

timesExcept = 0

try:
	input('Press ENTER to crash Python or CTRL+C to exit.')
	print('This program should crash Python in 3 seconds. You still have time to abort (see above)')
	time.sleep(3)
except KeyboardInterrupt:
	print("Interrupted. Exiting now...")
	exit(0)
print('crashing python now')

def loop(): # causes RecursionErrors, handled by the code below
	loop()
	
def realloop(): # allows the program to just restart itself
	try:
		loop()
	except RecursionError: # stops Python from just aborting due to RecursionErrors (usually exceptions would stop a fatal error)
		print('Python tried to give an exception. This has happened ' + str(timesExcept) + ' times.')
		timesExcept = timesExcept + 1
		realloop() # program restarts itself using a function

realloop() # for the first loop of the code

# The program should never get up to this point! If it does, you have a great computer!
print('python should have crashed by now')

# The whole code above should give you a 'Fatal Python error: Cannot recover from stack overflow.'
# next update: might put the whole thing in a loop for added loopyness