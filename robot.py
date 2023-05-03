from drivetrain import Drivetrain
import os
import wpilib
from wpilib import TimedRobot


class MyRobot(TimedRobot):  # this is the controller
    def robotInit(self):  # something
        self.drivetrain = Drivetrain()


if __name__ == "__main__":
    os.environ["HALSIMWS_HOST"] = "10.0.0.2"
    os.environ["HALSIMWS_PORT"] = "3300"

    wpilib.run(MyRobot)
