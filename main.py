import Agilent8164B as laser
import queue as Q
import time
import random as rand
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style


# Variables
# VISA_ADDRESS = 'GPIB0::20::INSTR'

# ls = laser.session_create(VISA_ADDRESS)
# laser.power_measure(ls, continuous=True)
q1 = Q.Queue(50)
while True:
    random_number = rand.randint(0,25)

    q1.put(random_number)




