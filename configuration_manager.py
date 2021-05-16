"""Provide abstraction for application's configuration."""

from configparser import ConfigParser, SectionProxy


# TODO: it's not safe to read any credentials from text file,
# TODO: consider to user OS environmental variables
class ConfigurationManager:
    """Representation of entity which represents application settings."""

    def __init__(self, path: str):
        """Provide object of ConfigurationManager with preloaded configuration."""
        self._path: str = path
        self._config: ConfigParser = ConfigParser()
        self._config.read(self._path)

    @property
    def api_key(self) -> str:
        """Provide api key of binance futures api.

        Returns:
            str: api key of binance futures api
        """
        return self._config["GENERAL"]["API_KEY"]

    @property
    def secret_key(self) -> str:
        """Provide secret key of binance futures api.

        Returns:
            str: secret key of binance futures api
        """
        return self._config["GENERAL"]["SECRET_KEY"]

    @property
    def commands_f(self) -> SectionProxy:
        """Provide set of api from commands_f section.

        Returns:
            SectionProxy: object which represents api collection
        """
        return self._config['COMMANDS_F']

    @property
    def commands_d(self) -> SectionProxy:
        """[Provide set of api from commands_d section.

        Returns:
            SectionProxy: object which represents api collection
        """
        return self._config['COMMANDS_D']


if __name__ == "__main__":
    # self check
    cfg = ConfigurationManager("CONFIG.INI")
    print(cfg.api_key, cfg.secret_key)
