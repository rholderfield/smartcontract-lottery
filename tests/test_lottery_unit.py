from brownie import Lottery, config, network
from scripts.deploy_lottery import deploy_lottery
from web3 import Web3


# 0.017
# 16000000000000000
# 16646081013147100


def test_get_entrance_fee():
    # Arrange
    lottery = deploy_lottery()
    # Act
    # 2,000 eth / usd
    # usdEntryFee is 50
    # 2000/1 == 50/x == 0.025
    expected_entrance_fee = Web3.toWei(0.025, "ether")
    entrance_fee = lottery.getEntranceFee()
    # Assert
    assert expected_entrance_fee == entrance_fee
