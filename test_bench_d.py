"""Time measurement toolkit for Binance Futures D API."""

from binance_d import RequestClient
from binance_d.model import *
from binance_d.constant.test import *
from binance_d.base.printobject import *
from binance_d.exception.binanceapiexception import *

from loguru import logger
from timerun import Timer

from configuration_manager import ConfigurationManager
from test_bench import TestBench


class TestBenchD(TestBench):
    """Representation for time measurement entity toolkit [Binanace Futures D API]."""

    def _run_testcase(self, api: str, command: str) -> None:
        """Perform execution of a single API with time measurements.

        Args:
            api (str): name of API
            command (str): valid Python code to be executed
        """
        with Timer() as timer:
            print(command)
            exec(command)
        self._logger.info(F"<{self._prettify_api(api)}> API duration: {timer.duration}")

    def run(self):
        """Perform execution of available test cases."""
        self._logger.info("Starting time measurements for Binance Futures D API.")
        self._run(self._config.commands_d)

    def _run(self, apis):
        """Perform execution of available test cases.

        Args:
            apis ([type]): list of available apis to be measured
        """
        for api in apis:
            command = apis[api]
            if api == 'request_client':
                # deviation should be applied for this API
                # replace credentials
                command = command.replace('XXX', f"'{self._config.api_key}'")
                command = command.replace('YYY', f"'{self._config.secret_key}'")
                # store result as it's needed for next test cases
                command = 'self._request_client = ' + command

            try:
                self._run_testcase(api, command)
            except BinanceApiException as e:
                self._logger.error(f"<{self._prettify_api(api)}> API: " + str(e))

        self._logger.info("All test cases for Binance Futures API D are done.")


def main() -> None:
    """Encapsulate the script's workflow."""
    logger.add("file_{time}.log", format="{time} {level} {message}", level='INFO')
    config = ConfigurationManager("CONFIG.INI")
    tbd = TestBenchD(config, logger)
    tbd.run()

if __name__ == "__main__":
    main()
