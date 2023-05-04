import configparser
import os


class Config:
    """Interact with configuration variables."""

    config_parser = configparser.ConfigParser()

    config_file_path = (os.path.join(os.getcwd(), 'config.ini'))

    @classmethod
    def initialize(cls):
        """Start config by reading config.ini."""
        cls.config_parser.read(cls.config_file_path)

    @classmethod
    def get(cls, key, fallback=None):
        """Get prod values from config.ini."""
        return cls.config_parser.get('PROD', key, fallback=fallback)
