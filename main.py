from utils import util
from loguru import logger
from dapp import dapp
import time


# 获取随机排序后的私钥列表
private_keys = util.get_private_key()


for index, item in enumerate(private_keys):
    if index > 1:
        break
    logger.info(f"开始执行第{index+1}个地址: {item['address']}")
    # 执行任务
    dapp.run(item["private_key"])
    
    logger.warning(f"等待10秒...")
    time.sleep(10)
