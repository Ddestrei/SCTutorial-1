from brownie import SimpleStorage, Coin, Ballot,convert,  accounts
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

proposals = [0,1,2]

def deploy_ballot():
    byte_proposal = [convert.to_bytes(p) for p in proposals]
    ballot = Ballot.deploy(
    ['A','B','C'],
    {
        "from": accounts[0],
        "gas_price": gas_strategy
    })
    for i in range(0,10):
        print(i)
        ballot.giveRightToVote(accounts[i],{"from": accounts[0]})
    
    for i in range(0,10):
        ballot.vote(0,{"from": accounts[i]})

    print(ballot.winningProposalFunc({"from": accounts[0]}))

def main():
    ss = deploy_simple_storage()
    c = deploy_coins()
    deploy_ballot()