import random
from eth_account import Account
from loguru import logger
from web3 import Web3


# 读取私钥, 并随机排序
def get_private_key():
    """读取私钥文件，返回私钥列表"""
    private_keys = []
    try:
        # 修改这里，使用utf-8编码打开文件
        with open("config/private_key.txt", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()

                # 跳过空行和注释行
                if line and not line.startswith("#"):
                    # 移除可能的0x前缀
                    if line.startswith("0x"):
                        line = line[2:]

                    current_account = Account.from_key(line)
                    private_keys.append(
                        {"address": current_account.address, "private_key": line}
                    )

        # 对私钥列表进行随机排序
        if len(private_keys) > 0:
            random.shuffle(private_keys)

        return private_keys
    except Exception as e:
        logger.error(f"读取私钥文件失败: {e}")
        return []


def random_wei(min_amount=0.01, max_amount=0.2):
   
    try:
        # 生成随机金额，保留1位小数
        amount = round(random.uniform(min_amount, max_amount), 2)
        logger.info(f"生成随机交易金额: {amount}")
        return amount
    except Exception as e:
        logger.error(f"生成随机金额失败: {e}")
        # 返回默认值
        default_amount = 0.05
        return default_amount
