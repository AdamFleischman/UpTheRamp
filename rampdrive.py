from autoroutine import AutoRoutine
from wpimath.controller import PIDController


class RampDrive(AutoRoutine):
    def __init__(self, drivetrain):
        self.drivetrain = drivetrain
        self.rampState = 0
        # 0 is before ramp, 1 is on ramp, 2 is after ramp
        self.flatSpeed = .6
        self.rampSpeed = 1
        self.pid_controller = PIDController(20, 0, 0)
        self.pid_controller.setSetpoint(0)
        self.pid_controller.setTolerance(.05)
        self.gyroAngleYThreshold = 5

    def run(self):
        if self.rampState == 0:     # before ramp
            self.drivetrain.move(self.flatSpeed, self.rotate)
            if self.drivetrain.getGyroAngleY() > self.gyroAngleYThreshold:
                self.rampState = 1
        elif self.rampState == 1:   # on ramp
            self.drivetrain.move(self.rampSpeed, self.rotate)
            if self.drivetrain.getGyroAngleY() < self.gyroAngleYThreshold:
                self.rampState = 2
        else:                       # after ramp
            self.drivetrain.move(0, 0)
