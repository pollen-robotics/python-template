import logging


class Celsius:
    """Manage celcius temperature and other format."""

    def __init__(self, temperature: float = 0):
        self.logger = logging.getLogger(__name__)
        self.temperature = temperature

    def to_fahrenheit(self) -> float:
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self) -> float:
        self.logger.info("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value: float) -> None:
        self.logger.info("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value
