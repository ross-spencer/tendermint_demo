#! /usr/bin/bash

wget https://github.com/tendermint/tendermint/releases/download/v0.34.11/tendermint_0.34.11_linux_amd64.tar.gz
mkdir -p /tmp/tendermint
tar -xzf tendermint_0.34.11_linux_amd64.tar.gz --directory /tmp/tendermint/