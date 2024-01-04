from odk_mailer.lib import globals, utils
import json

def validate(config):
    if not config:
        utils.abort("Config Error: Check .odk-mailer/config.json ")

    required_keys = ["odk_host", "smtp_host", "smtp_port"]

    for required_key in required_keys:
        if not required_key in config:
            utils.abort(f"Invalid config: {required_key} is required.")


def load():
    with open(globals.odk_mailer_config, "r") as f:
        config = json.load(f)

    validate(config)
    return config