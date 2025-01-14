import json

WETH_ADDRESS = '0x5300000000000000000000000000000000000004'
HYPERLANE_NFT_ADDRESS = '0x7daC480d20f322D2ef108A59A465CCb5749371c4'

ZRO_ClAIM_ADDRESS = {
    'Arbitrum': "0xB09F16F625B363875e39ADa56C03682088471523"
}

STARGATE_DST_ID = {
    'Arbitrum One': 30110,
    'OP Mainnet': 30111
}
STARGATE_TOKEN = ["ETH","USDC"]

STARGATE_CONTRACTS = {
    'Arbitrum One': {
        'pool_eth': "0xA45B5130f36CDcA45667738e2a258AB09f4A5f7F",
        "pool_usdc": "0xe8CDF27AcD73a434D661C84887215F7598e7d0d3",
                },
    'OP Mainnet': {
        'pool_eth': "0xe8CDF27AcD73a434D661C84887215F7598e7d0d3",
        "pool_usdc": "0xcE8CcA271Ebc0533920C83d39F417ED6A0abB7D0"
                }
        }

AAVE_CONTRACTS = {
    'Arbitrum': {
        'native': "0xecD4bd3121F9FD604ffaC631bF6d41ec12f1fafb",
        'pool': "0x794a61358D6845594F94dc1DB02A252b5b4814aD",
        'aArbWETH': "0xe50fA9b3c56FfB159cB0FCA61F5c9D750e8128c8"
    }
}

SYNCSWAP_CONTRACTS = {
    'zkSync': {
        'pool_factory': '0xf2DAd89f2788a8CD54625C60b55cD3d2D0ACa7Cb',
        'paymaster': '0x0c08f298A75A090DC4C0BB4CaA4204B8B9D156c1',
        'router_v2': '0x9B5def958d0f3b6955cBEa4D5B7809b2fb26b059'
    }
}

UNISWAP_CONTRACTS = {
    'Arbitrum': {
        'quoter': '0xb27308f9F90D607463bb33eA1BeBb41C27CE5AB6',
        'router': '0xE592427A0AEce92De3Edee1F18E0157C05861564'
    }
}

LAYERBANK_CONTRACTS = {
    'Scroll': {
        'USDC': '0x0D8F8e271DD3f2fC58e5716d3Ff7041dBe3F0688',
        'Core': "0xEC53c830f4444a8A56455c6836b5D2aA794289Aa",
    }
}
ZEROLEND_CONTRACTS = {
    'Linea': {
        'USDC': '0x176211869cA2b568f2A7D4EE941E073a821EE1ff',
        'pool': "0x2f9bB73a8e98793e26Cb2F6C4ad037BDf1C6B269",
    }
}

ETH_MASK = "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE"
ZERO_ADDRESS = "0x0000000000000000000000000000000000000000"

TOKENS_PER_CHAIN = {
    'Arbitrum One': {
        "ETH": "0x82aF49447D8a07e3bd95BD0d56f35241523fBab1",
        "WETH": "0x82aF49447D8a07e3bd95BD0d56f35241523fBab1",
        "USDC.e": "0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8",
        "USDT": "0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9",
        "ZRO": "0x6985884C4392D348587B19cb9eAAf157F13271cd",
        "USDC": "0xaf88d065e77c8cC2239327C5EDb3A432268e5831"
    },
    'OP Mainnet': {
        "ETH": "0x82aF49447D8a07e3bd95BD0d56f35241523fBab1",
        "USDC": "0x0b2C639c533813f4Aa9D7837CAf62653d097Ff85"

    },
    'Ethereum': {
        "ETH": "0x82aF49447D8a07e3bd95BD0d56f35241523fBab1",
    },
    'zkSync': {
        "ETH": "0x5AEa5775959fBC2557Cc8789bC1bf90A239D9a91",
        "WETH": "0x5AEa5775959fBC2557Cc8789bC1bf90A239D9a91",
        "USDT": "0x493257fD37EDB34451f62EDf8D2a0C418852bA4C",
        "USDC.e": "0x3355df6D4c9C3035724Fd0e3914dE96A5a83aaf4"
    },

    'Scroll': {
        "ETH": "0x5AEa5775959fBC2557Cc8789bC1bf90A239D9a91",
        "USDC": "0x06eFdBFf2a14a7c8E15944D1F4A48F9F95F663A4",
    },

    'Linea': {
        "ETH": "0xe5D7C2a44FfDDf6b295A15c148167daaAf5Cf34f",
        "USDC": "0x176211869cA2b568f2A7D4EE941E073a821EE1ff",
    }
}
CHAIN_ID_BY_NAME = {
    'Arbitrum One': 42161,
    'OP Mainnet': 10,
    'Ethereum': 1
}
DROP_MANAGER_CONTRACT= "0x060e7c1bc320C9e7C1760e06A5455c343D16603B"

#
# with open('abis/stargate_pool_eth.json') as file:
#      STARGATE_ETH_ABI = json.load(file)
#
# with open('abis/stargate_pool_usdc.json') as file:
#     STARGATE_USDC_ABI = json.load(file)
#
# # with open('abis/orbiter_router_abi.json') as file:
# #      ORBITER_ABI = json.load(file)
# #
with open('abis/erc20_abi.json') as file:
    ERC20_ABI = json.load(file)

with open('abis/drop_abi.json') as file:
    DROP_ABI = json.load(file)
# with open('abis/all_chains_data.json') as file:
#     ALL_CHAINS_DATA = json.load(file)
# #
# with open('abis/layerbank_lUSDC.json') as file:
#     LAYERBANK_lUSDC= json.load(file)
#
# with open('abis/layerbank_core.json') as file:
#     LAYERBANK_CORE= json.load(file)

# with open('abis/hnft_abi.json') as file:
#     HNFT_ABI = json.load(file)
#
# with open('abis/syncswap_pool_factory.json') as file:
#     SYNCSWAP_POOL_FACTORY_ABI = json.load(file)
#
# with open('abis/syncswap_pool.json') as file:
#     SYNCSWAP_POOL_ABI = json.load(file)
#
# with open('abis/syncswap_router.json') as file:
#     SYNCSWAP_ROUTER_ABI = json.load(file)
#
# with open('abis/uniswapV3_quoter.json') as file:
#     UNISWAP_QUOTER_ABI = json.load(file)
#
# with open('abis/uniswapV3_router.json') as file:
#     UNISWAP_ROUTER_ABI = json.load(file)
#
# with open('abis/aave_native.json') as file:
#     AAVE_NATIVE_ABI = json.load(file)
#
# with open('abis/aave_pool.json') as file:
#     AAVE_POOL_ABI = json.load(file)
#
# with open('abis/stargate_router.json') as file:
#     STARGATE_ROUTER_ABI = json.load(file)
#
# with open('abis/zro_claim_abi.json') as file:
#     ZRO_CLAIM_ABI = json.load(file)
#
# with open('abis/paymaster_abi.json') as file:
#     SYNCSWAP_PAYMASTER_ABI = json.load(file)

