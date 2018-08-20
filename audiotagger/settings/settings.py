import os
import configparser

cp = configparser.ConfigParser()
settings_directory_path = os.path.dirname(os.path.realpath(__file__))
config_file_path = os.path.realpath(
    os.path.join(settings_directory_path, "config.txt"))
cp.read(config_file_path)

LOG_DIRECTORY = eval(cp.get("general", "LOG_DIRECTORY"))
