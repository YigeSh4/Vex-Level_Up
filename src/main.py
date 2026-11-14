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
MotorArm2 = Motor(Ports.PORT10)
MotorHand = Motor(Ports.PORT4)
MotorGroup1 = MotorGroup(MotorArm,MotorArm2)
Switch1 = Bumper(Ports.PORT2)

dt = DriveTrain(MotorR, MotorL)

ctrl = Controller()

MotorArm.set_velocity(100,PERCENT)
MotorArm2.set_velocity(50,PERCENT)
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

    if ctrl.buttonLUp.pressing() or ctrl.buttonEUp.pressing():
         MotorGroup1.spin(FORWARD, 300, PERCENT)
    elif ctrl.buttonLDown.pressing() or ctrl.buttonEDown.pressing():
         MotorGroup1.spin(REVERSE, 300, PERCENT)
    else:
         MotorGroup1.stop(HOLD)

    if ctrl.buttonRUp.pressing() or ctrl.buttonFUp.pressing():
         MotorHand.spin(FORWARD, 100, PERCENT)
    elif ctrl.buttonRDown.pressing() or ctrl.buttonFDown.pressing():
         MotorHand.spin(REVERSE, 100, PERCENT)
    else:
         MotorHand.stop()

