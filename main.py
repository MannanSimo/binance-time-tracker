from loguru import logger

from configuration_manager import ConfigurationManager
from test_bench_f import TestBenchF
from test_bench_d import TestBenchD

def main():
    logger.add("file_{time}.log", format="{time} {level} {message}", level='INFO')
    config = ConfigurationManager("CONFIG.INI")

    testbenches = []
    testbenches.append(TestBenchF(config, logger))
    testbenches.append(TestBenchD(config, logger))

    for testbench in testbenches:
        testbench.run()


if __name__ == "__main__":
    main()

