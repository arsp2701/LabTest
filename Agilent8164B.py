import pyvisa as visa
import sys
import time
import keyboard


def session_create(visa_address):
    try:
        # Create a connection (session) to the instrument
        resourceManager = visa.ResourceManager()
        session = resourceManager.open_resource(visa_address)
        return session
    except visa.Error as ex:
        print('Couldn\'t connect to \'%s\', exiting now...' % visa_address)
        sys.exit()


def session_close(session):
    session.call_close()


def identification(session):
    # Send *IDN? and read the response
    session.write('*IDN?')
    time.sleep(0.001)
    idn = session.read()
    session.write('*RST')
    print('*IDN? returned: %s' % idn.rstrip('\n'))


def laser_on(session):
    # Send sour0:pow:stat 1
    session.write('sour0:pow:stat 1')


def laser_off(session):
    # Send sour0:pow:stat 0
    session.write('sour0:pow:stat 0')


def get_measure(session):
    # Send fetc1:pow?qq
    session.write('fetc1:pow?')
    time.sleep(0.001)
    measure = session.read()
    print('Mesure')
    print(measure)
    time.sleep(0.1)


def power_measure(session, continuous=True, *args):
    if (continuous):
        print(' Mesure en continu')
        while True :
            laser_on(session)
            if keyboard.is_pressed('space'):
                laser_off(session)
                print('Mesures en pause')
                while True :
                    if keyboard.is_pressed('r'):
                        print('Reprise des mesures')
                        power_measure(session)
                    if keyboard.is_pressed('q'):
                        laser_off(session)
                        print('Quitter les mesures')
                        break
            if keyboard.is_pressed('q'):
                laser_off(session)
                print('Quitter les mesures')
                break
            get_measure(session)
    else :
        laser_on(session)
        get_measure(session)
        laser_off(session)












