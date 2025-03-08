from web3 import Web3
from eth_account import Account
from config import config
from loguru import logger


if __name__ == "__main__":
    # print(my_address)

    # val = Web3.from_wei(4839274829842984279279, 'ether')
    # to_wei = Web3.to_wei(0.1, 'ether')
    # print('val: ', val,to_wei)
    
    # 是否连接成功
    w3 = Web3(Web3.HTTPProvider(config.monad_rpc))
    # print(w3.is_connected())
    
    # 获取余额 wei    小数为18位小数
    balance = w3.eth.get_balance(my_address)
    print('balance: ', Web3.from_wei(balance, 'ether'))
    
    # 获取一个区块信息 来自58e0的交互
    # block = w3.eth.get_block(6400663)
    # print('block 6400663: ', block)

    # 获取一个区块的交易数量当前区域包含343个交易
    # transactions_count = w3.eth.get_block_transaction_count(6400663)
    # print('transactions_count: ', transactions_count)
    
    # 获取一个转账的交易详情
    # tx = w3.eth.get_transaction("0xa36c744865baad0c2831edb4023c7682c9f03d00562030df2f0bca4e9a0589e3")
    # logger.info('tx: {}', tx)
    
    # 查询该地址已经发送的交易数量
    tx_address = w3.eth.get_transaction_count("0x6cD739f83e89665187c8Cec868a8b92650E4210D")
    logger.info('tx_address: {}', tx_address)

    # 获取nonce
    nonce = w3.eth.get_transaction_count(my_address)
    logger.info('nonce: {}', nonce)

    # 获取gas price gwei  单位  1gwei = 10亿  1,000,000,000
    gas_price = w3.eth.gas_price
    logger.info('gas_price: {} gwei',gas_price/ 10**9)

    # 获取gas limit
    gas_limit = w3.eth.estimate_gas
    logger.info('gas_limit: {}', gas_limit)
