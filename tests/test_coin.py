from brownie import Coin, accounts, reverts
from brownie.network import gas_price
from brownie.network.gas.strategies import LinearScalingStrategy
from brownie import network
import pytest

gas_strategy = LinearScalingStrategy("10 gwei", "20 gwei", 1.1)
network.connect('development')
gas_price(gas_strategy)

@pytest.fixture
def coin():
    account = accounts[0]
    coin = Coin.deploy({
        "from": account,
        "gas_price": gas_strategy
        })
    print(coin)
    return coin

@pytest.fixture
def distribute_coins(coin):
    for i in range(0,10):
        coin.mint(accounts[i],100,{"from": accounts[0]})
    return coin

def test_creator_getter(coin):
    print("HELLO WORLD") 
    assert coin.creator() == accounts[0]

def test_balances_getter(coin):
    assert coin.balances(accounts[0]) == 0

def test_mint_set_balance(distribute_coins):
    for  i in range(0,10):
        assert distribute_coins.checkAmount({"from":accounts[i]}) == 100

def test_mint_not_creator(coin):
    with reverts():
        coin.mint(accounts[1],100,{"from": accounts[1]})

def test_sent_set_balance(distribute_coins):
    distribute_coins.send(accounts[1],10,{"from":accounts[0]})
    
    assert distribute_coins.checkAmount({"from":accounts[1]}) == 110
    assert distribute_coins.checkAmount({"from":accounts[0]}) == 90

def test_sent_fali_revert(distribute_coins):
    with reverts():
        distribute_coins.send(accounts[9],101,{"from":accounts[8]})

def test_sent_event_emitted(coin):
    txM = coin.mint(accounts[0],100,{"from": accounts[0]})
    txS = coin.send(accounts[1],100,{"from":accounts[0]})

    assert txS.events.count("SendCoins") == 1 
    assert txM.events.count("MintCoins") == 1 