import random
from dapp.bebop import main as bebop_main
from dapp.demask import main as demask_main

# 任务列表
task_list = [
    {"dapp": "bebop", "url": "https://bebop.xyz/trade?network=monad", "run": bebop_main.run},
    {"dapp": "demask", "url": "https://app.demask.finance/launchpad/0xee45cb2f44d1884ba3be16779411b745d8a82de3/0", "run": demask_main.run},
]

random.shuffle(task_list)

def run(private_key):
    for task in task_list:  
        task["run"](private_key)

