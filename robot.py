from drivetrain import Drivetrain
import os
import wpilib
from wpilib import TimedRobot
from robotcontainer import RobotContainer


class MyRobot(TimedRobot):  # this is the controller
    def robotInit(self):  # something
        #self.drivetrain = Drivetrain()
        self.container = RobotContainer()

    def teleopPeriodic(self):
        forward = self.container.controller.getRawAxis(0)
        rotate = self.container.controller.getRawAxis(1)
        self.container.drivetrain.move(rotate, forward)
        print(self.container.drivetrain.getGyroAngleY())

    def autonomousInit(self):
        self.auto = self.container.get_autonomous()

    def autonomousExit(self):
        self.container.drivetrain.resetEncoders()
        self.container.drivetrain.resetGyro()


if __name__ == "__main__":
    os.environ["HALSIMWS_HOST"] = "10.0.0.2"
    os.environ["HALSIMWS_PORT"] = "3300"

    wpilib.run(MyRobot)
