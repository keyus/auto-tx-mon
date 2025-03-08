# 合约地址
main_address = '0x760afe86e5de5fa0ee542fc7b7b713e1c5425701'

# 合约abi
main_abi = [
    {
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "src",
                "type": "address",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "guy",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "wad",
                "type": "uint256",
            },
        ],
        "name": "Approval",
        "outputs": [],
        "stateMutability": "view",  # 添加 stateMutability
        "type": "event",
    },
    {
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "dst",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "wad",
                "type": "uint256",
            },
        ],
        "name": "Deposit",
        "outputs": [],
        "stateMutability": "view",  # 添加 stateMutability
        "type": "event",
    },
    {
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "src",
                "type": "address",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "dst",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "wad",
                "type": "uint256",
            },
        ],
        "name": "Transfer",
        "outputs": [],
        "stateMutability": "view",  # 添加 stateMutability
        "type": "event",
    },
    {
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "src",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "wad",
                "type": "uint256",
            },
        ],
        "name": "Withdrawal",
        "outputs": [],
        "stateMutability": "view",  # 添加 stateMutability
        "type": "event",
    },
    {
        "inputs": [],
        "name": "",
        "outputs": [],
        "stateMutability": "payable",
        "type": "fallback",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "", "type": "address"},
            {"internalType": "address", "name": "", "type": "address"},
        ],
        "name": "allowance",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "guy", "type": "address"},
            {"internalType": "uint256", "name": "wad", "type": "uint256"},
        ],
        "name": "approve",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "decimals",
        "outputs": [{"internalType": "uint8", "name": "", "type": "uint8"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "deposit",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "name",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "symbol",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "totalSupply",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "dst", "type": "address"},
            {"internalType": "uint256", "name": "wad", "type": "uint256"},
        ],
        "name": "transfer",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "src", "type": "address"},
            {"internalType": "address", "name": "dst", "type": "address"},
            {"internalType": "uint256", "name": "wad", "type": "uint256"},
        ],
        "name": "transferFrom",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "wad", "type": "uint256"}],
        "name": "withdraw",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
]