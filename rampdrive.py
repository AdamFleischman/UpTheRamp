from autoroutine import AutoRoutine
from wpimath.controller import PIDController


class RampDrive(AutoRoutine):
    def __init__(self, drivetrain):
        self.drivetrain = drivetrain
        self.rampState = 0
        # 0 is before ramp, 1 is on ramp, 2 is after ramp
        self.flatSpeed = .6
        self.rampSpeed = .8
        self.pid_controller = PIDController(20, 0, 0)
        self.pid_controller.setSetpoint(0)
        self.pid_controller.setTolerance(.05)
        self.gyroAngleYThreshold = 5

    def run(self):
        difference = self.drivetrain.left_encoder.getDistance() - self.drivetrain.right_encoder.getDistance()
        rotate = self.pid_controller.calculate(difference)
        if self.rampState == 0:     # before ramp
            self.drivetrain.move(self.flatSpeed, rotate)
            if self.drivetrain.getGyroAngleY() > self.gyroAngleYThreshold:
                self.rampState = 1
                self.pid_controller.setTolerance(.2)
        elif self.rampState == 1:   # on ramp
            self.drivetrain.move(self.rampSpeed, rotate)
            if self.drivetrain.getGyroAngleY() < self.gyroAngleYThreshold:
                self.rampState = 2
        else:                       # after ramp
            self.drivetrain.move(0, 0)
