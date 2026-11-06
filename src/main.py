# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       eggo67                                                       #
# 	Created:      10/31/2026, 1:09:40 PM                                       #
# 	Description:  IQ2 project                                                  #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()

brain.screen.print("Hello IQ2")

MotorL = Motor(Ports.PORT12)
MotorR = Motor(Ports.PORT3, True)

MotorArm = Motor(Ports.PORT1, True)
MotorHand = Motor(Ports.PORT4)

Switch1 = Bumper(Ports.PORT2)

dt = DriveTrain(MotorR, MotorL)

ctrl = Controller()

# def link_arm_w_drive():
#     if ctrl.axisA.position() > 75 or ctrl.axisA.position() < 10:
#         MotorArm.spin(FORWARD, 35, PERCENT)
#     else:    
#          MotorArm.stop()
    

while 1:
    if ctrl.axisA.position() > 10 or ctrl.axisA.position() < -10:
        dt.drive(FORWARD, ctrl.axisA.position(), PERCENT)
    elif ctrl.axisC.position() > 10 or ctrl.axisC.position() < -10:
            dt.turn(LEFT, ctrl.axisC.position(), PERCENT)
    else:
        dt.stop()

    if ctrl.buttonLUp.pressing():
         MotorArm.spin(FORWARD, 300, PERCENT)
    elif ctrl.buttonLDown.pressing():
         MotorArm.spin(REVERSE, 300, PERCENT)
    else:
         MotorArm.stop()

    if ctrl.buttonRUp.pressing():
         MotorHand.spin(FORWARD, 100, PERCENT)
    elif ctrl.buttonRDown.pressing():
         MotorHand.spin(REVERSE, 100, PERCENT)
    else:
         MotorHand.stop()

