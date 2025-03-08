from web3 import Web3
from eth_account import Account
from config import config
from utils import util
import dapp.bebop.contract as task_contract
from loguru import logger

def run(private_key):
    my_account = Account.from_key(private_key)
    my_address = my_account.address

    w3 = Web3(Web3.HTTPProvider(config.monad_rpc))
    checksum_contract_address = Web3.to_checksum_address(task_contract.main_address)
    contract = w3.eth.contract(address=checksum_contract_address, abi=task_contract.main_abi)

    # 交互金额
    money = util.random_wei()
    money_wei = w3.to_wei(money, 'ether')

    # 构建交易 id
    tx = contract.functions.deposit().build_transaction(
        {
            "nonce": w3.eth.get_transaction_count(my_address),
            "gas": 2000000,  # 调整 gas limit
            "gasPrice": w3.eth.gas_price,
            "from": my_address,
            "value": money_wei,  
        }
    )
    # 签名和发送交易
    signed_tx = my_account.sign_transaction(tx)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
    logger.info(f"开始广播交易...{tx_hash.hex()}")
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    if tx_receipt["status"] == 1:
        logger.success("bebop.xyz 项目 交互成功!")
    else:
        logger.error("bebop.xyz 项目 交互失败!")

