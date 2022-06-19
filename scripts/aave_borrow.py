from brownie import (
    config,
    network,
    interface
)

from scripts.helper_scripts import get_account
from scripts.get_weth import get_weth

def get_lending_pool():
    lending_pool_address_provider = interface.ILendingPoolAddress(
        config["networks"][network.show_active()]["lending_pool_addresses_provider"]
        )
    lending_pool_address = lending_pool_address_provider.getLendingPool()
    lending_pool = interface.ILendingPool(lending_pool_address)
    return lending_pool

def main():
    account = get_account()
    erc20_address = config["networks"][network.show_active()]["weth_token"]
    if network.show_active() in ["mainnet-fork-dev"]:
        get_weth()
    lending_pool = get_lending_pool()
    print(lending_pool)

