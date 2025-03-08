from config import config
from eth_account import Account
from web3 import Web3
from loguru import logger

ERC1155_ABI = [
    {
        "inputs": [
            {"internalType": "address", "name": "account", "type": "address"},
            {"internalType": "uint256", "name": "id", "type": "uint256"},
        ],
        "name": "balanceOf",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "bytes32[]", "name": "proof", "type": "bytes32[]"},
            {"internalType": "uint256", "name": "limit", "type": "uint256"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
        ],
        "name": "buy",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "", "type": "address"},
            {"internalType": "uint256", "name": "", "type": "uint256"},
        ],
        "name": "mintedCountPerWallet",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
]


def run(private_key):
    w3 = Web3(Web3.HTTPProvider(config.monad_rpc))
    checksum_contract_address = Web3.to_checksum_address("0x2CDd146Aa75FFA605ff7c5Cc5f62D3B52C140f9c")
    contract = w3.eth.contract(address=checksum_contract_address, abi=ERC1155_ABI)
    
    my_account = Account.from_key(private_key)
    my_address = my_account.address
    
    mint_txn =  contract.functions.buy( [], 1000000, 1).build_transaction(
                    {
                        "from": my_address,
                        "value": w3.to_wei(0.1, "ether"),  
                        "nonce": w3.eth.get_transaction_count(my_address),
                        "maxFeePerGas": w3.eth.gas_price,
                        "maxPriorityFeePerGas": w3.eth.gas_price,
                    }
                )

    signed_txn = my_account.sign_transaction(mint_txn)
    tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
    logger.info(f"开始广播交易...{tx_hash.hex()}")
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    if receipt["status"] == 1:
        logger.success(f"demask.xyz 项目 交互成功! {my_address}")
    else:
        logger.error(f"demask.xyz 项目 交互失败! {my_address}")
