"""Example class."""

import logging
from typing import Any, overload


class Foo:
    """This is a template class"""

    def __init__(self) -> None:
        """Set up empty slots."""
        self._logger = logging.getLogger(__name__)
        self._logger.info("Constructor")
        self._private_variable = "private"
        self.public_variable = "public"

    @property
    def private_variable(self) -> str:
        return self._private_variable

    @private_variable.setter
    def private_variable(self, value: str) -> None:
        self._private_variable = value

    def __del__(self) -> None:
        self._logger.info("Destructor")

    @overload
    def doingstuffs(self, var: int, var2: float) -> None: ...

    @overload
    def doingstuffs(self, var: int) -> None: ...

    def doingstuffs(self, var: Any = None, var2: Any = None) -> None:
        if var is not None:
            self._logger.info(f"{var} {type(var)} ")
        if var2 is not None:
            self._logger.info(f"{var2} {type(var2)} ")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    f = Foo()
    f.doingstuffs(3)
    f.doingstuffs(3, 5.6)
