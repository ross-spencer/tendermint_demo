"""Tendermint node genesis."""

import pathlib
import shutil
import subprocess
import toml
import os

thisdir = pathlib.Path(__file__).resolve().parent
home = pathlib.Path.home()

if "CODESPACE_NAME" in os.environ:
    ENDPOINT = f"https://{os.environ['CODESPACE_NAME']}-3000.githubpreview.dev"
elif "GITPOD_WORKSPACE_URL" in os.environ:
    ENDPOINT = f"https://3000-{os.environ['GITPOD_WORKSPACE_URL']}"
else:
    ENDPOINT = "*"


def main():
    TENDERMINT_APP = "/tmp/tendermint/tendermint"
    TENDERMINT_HOME = "/tmp/tendermint/.tendermint"

    tendermint = pathlib.Path(TENDERMINT_HOME)
    if tendermint.exists():
        shutil.rmtree(tendermint)

    subprocess.Popen(
        [TENDERMINT_APP, "init", "--home", TENDERMINT_HOME, "--log_level", "info"]
    ).wait()

    config_path = tendermint.joinpath("config", "config.toml")
    config = toml.loads(config_path.read_text())
    config["rpc"]["cors_allowed_origins"] = [ENDPOINT]
    config_path.write_text(toml.dumps(config))

    subprocess.Popen(
        [TENDERMINT_APP, "node", "--home", TENDERMINT_HOME, "--log_level", "info"]
    ).wait()


if __name__ == "__main__":
    main()
