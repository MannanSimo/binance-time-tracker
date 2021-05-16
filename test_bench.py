"""Naive implementation of class that performs time measurement for a given command."""

from abc import ABC


class TestBench(ABC):
    """Abstraction of test bench to perfrom time measurement test."""

    def __init__(self, config, logger):
        self._config = config
        self._logger = logger
        self._request_client = None

    def _prettify_api(self, api: str) -> str:
        """Remove underscores and capitalize the given api.

        Args:
            api (str): api input

        Returns:
            str: Remove underscores and capitalize the given api
        """
        api = api.replace("_", " ")
        return api.capitalize()
