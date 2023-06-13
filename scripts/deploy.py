from brownie import SimpleStorage, Coin,  accounts
from brownie.network import gas_price
from brownie.network.gas.strategies import LinearScalingStrategy

gas_strategy = LinearScalingStrategy("10 gwei", "20 gwei", 1.1)

gas_price(gas_strategy)

def deploy_coins() :
    account = accounts[0]
    coin = Coin.deploy({
        "from": account,
        "gas_price": gas_strategy
        })
    print(coin)
    return coin

def deploy_simple_storage():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({
        "from": account,
        "gas_price": gas_strategy
        })
    print(simple_storage)
    return simple_storage

def main():
    ss = deploy_simple_storage()
    c = deploy_coins()
    c.mint(accounts[0], 100,{"from": accounts[0]})
    print(c.checkAmount({"from": accounts[0]}))
    print(c.display())