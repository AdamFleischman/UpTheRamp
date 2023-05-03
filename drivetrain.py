from wpilib import Spark, Encoder
from wpilib.drive import DifferentialDrive
import math
import romi


class Drivetrain:
    def __init__(self):
        self.left_encoder = Encoder(4, 5)
        self.right_encoder = Encoder(6, 7)
        self.left_motor = Spark(0)
        self.right_motor = Spark(1)
        self.drivetrain = DifferentialDrive(self.left_motor, self.right_motor)
        self.left_encoder.setDistancePerPulse(0.07 * math.pi / (12 * 120))
        self.right_encoder.setDistancePerPulse(0.07 * math.pi / (12 * 120))
        self.gyro = romi.RomiGyro()

    def move(self, forward, rotate):
        self.drivetrain.arcadeDrive(forward, rotate)

    def getGyroAngleY(self):
        """
        Give the twist of the robot
        :return: the current twist angle in degrees
        """

        return self.gyro.getAngleY()

    def resetGyro(self):
        """Resets the angles to all be 0."""

        self.gyro.reset()
