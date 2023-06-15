from brownie import SimpleStorage, Coin, Ballot,  accounts, config
from brownie.network import gas_price
from brownie.network.gas.strategies import LinearScalingStrategy

gas_strategy = LinearScalingStrategy("10 gwei", "20 gwei", 1.1)

gas_price(gas_strategy)

def deploy_ballot():
    account = accounts.add(config["keys"]["private_key"])
    ballot = Ballot.deploy(
        ['A','B','C'],
        {"from": account},
        publish_source=config["networks"]["goerli"]["verify"]
    )

def main():
    deploy_ballot()