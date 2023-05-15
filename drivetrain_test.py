import pytest
from unittest.mock import MagicMock
from drivetrain import Drivetrain
from pytest import MonkeyPatch

@pytest.fixture
def drivetrain() -> Drivetrain:
    drive = drivetrain()
    drive.left_encoder = MagicMock()
    drive.right_encoder = MagicMock()
    drive.left_motor = MagicMock()
    drive.right_motor = MagicMock()
    drive.drivetrain = MagicMock()
    drive.gyro = MagicMock()

def test_arcadeDrive(drivetrain: Drivetrain) -> None:
    # Setup
    arcadeDrive = drivetrain.drive.arcadeDrive

    # Action
    drivetrain.drive.arcadeDrive(0.2, 0.3)

    # Assert
    arcadeDrive.assert_called_once()

def test_resetencoders(drivetrain: Drivetrain) -> None:
    # Setup
    leftreset = drivetrain.left_encoder.reset
    rightreset = drivetrain.right_encoder.reset

    # Action
    drivetrain.resetEncoders()

    # Assert
    leftreset.assert_called_once()
    rightreset.assert_called_once()

# Monkeypatching

def test_averageDistanceMeter(drivetrain: Drivetrain, monkeypatch: MonkeyPatch ):
    def mock_getRightDistanceMeter(self):
        return 2.0

    def mock_getLeftDistanceMeter(self):
        return 3.0

    monkeypatch.setattr(Drivetrain, "getLeftDistance", mock_getLeftDistanceMeter)
    monkeypatch.setattr(Drivetrain, "getRightDistance", mock_getRightDistanceMeter)

    dist=drivetrain.averageDistanceMeter()

    assert dist==(2.0+3.0)/2