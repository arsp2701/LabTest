import Agilent8164B as laser

# Variables
VISA_ADDRESS = 'GPIB0::20::INSTR'

ls = laser.session_create(VISA_ADDRESS)
laser.power_measure(ls, continuous=True)







