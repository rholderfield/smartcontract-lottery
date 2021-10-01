from brownie import Lottery, accounts, config, network
from web3 import Web3

# 0.017
# 16000000000000000


def test_get_enterance_fee():
    account = accounts[0]
    lottery = Lottery.deploy(
        config["networks"][network.show_active()]["eth_usd_price_feed"],
        {"from": account},
    )
    assert lottery.getEnteranceFee() > Web3.toWei(0.014, "ether")
    assert lottery.getEnteranceFee() < Web3.toWei(0.018, "ether")
