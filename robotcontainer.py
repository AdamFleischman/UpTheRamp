import wpilib

from drivetrain import Drivetrain
from autoroutine import AutoRoutine
from rampdrive import RampDrive


class RobotContainer:

    def __init__(self):
        self.controller = wpilib.Joystick(0)
        self.drivetrain = Drivetrain()
        self.chooser = wpilib.SendableChooser()
        self._configure()

    def _configure(self):
        self.chooser.addOption("Ramp Drive", RampDrive(self.drivetrain))
        wpilib.SmartDashboard.putData(self.chooser)

    def get_autonomous(self) -> AutoRoutine:
        return self.chooser.getSelected()
