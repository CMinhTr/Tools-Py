from eth_account import Account
from web3 import Web3
Account.enable_unaudited_hdwallet_features()
acct = Account.from_mnemonic("radar cry salmon pitch hill clap usual blame only tribe page stone")
address = acct.address
print(address)
