import gc

import requests
from web3 import Web3
import time
from time import sleep
from typing import cast
from web3.providers import JSONBaseProvider
from web3.types import RPCResponse
# import pycurl
# import certifi
# from io import BytesIO
import ujson





# # Creating a local file for logging
# logging.basicConfig(filename="C:\\Users\\RetailAdmin\\PycharmProjects\\pythonProject1\\canli_logs.txt", encoding='utf-8', level=logging.INFO)
# logging.info("Logging Works")

#w3 = Web3(Web3.HTTPProvider("https://api.avax.network/ext/bc/C/rpc"))
#w3 = Web3(Web3.HTTPProvider("https://speedy-nodes-nyc.moralis.io/b71d8a61e27edf2d34b86e72/avalanche/mainnet"))
w3 = Web3(Web3.WebsocketProvider("wss://speedy-nodes-nyc.moralis.io/b71d8a61e27edf2d34b86e72/avalanche/mainnet/ws", websocket_timeout=1))
# Server Wallet Info
private_key = ""  # Enter your private Key
wallet_addr = w3.toChecksumAddress("")  # Enter your wallet address


def _fast_decode_rpc_response(raw_response: bytes) -> RPCResponse:
    decoded = ujson.loads(raw_response)
    return cast(RPCResponse, decoded)


def patch_provider(provider: JSONBaseProvider):
    """Monkey-patch web3.py provider for faster JSON decoding.

    Call this on your provider after construction.
I c
    This greatly improves JSON-RPC API access speeds, when fetching
    multiple and large responses.
    """
    provider.decode_rpc_response = _fast_decode_rpc_response
patch_provider(w3)
patch_provider(w3.provider)
# CONTRACTS


# SpookySwap EXCHANGE
spooky_router_addr = w3.toChecksumAddress('0x60aE616a2155Ee3d9A68541Ba4544862310933d4')
spooky_router_abi = '[{"type":"constructor","stateMutability":"nonpayable","inputs":[{"type":"address","name":"_factory","internalType":"address"},{"type":"address","name":"_WAVAX","internalType":"address"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"address","name":"","internalType":"address"}],"name":"WAVAX","inputs":[]},{"type":"function","stateMutability":"nonpayable","outputs":[{"type":"uint256","name":"amountA","internalType":"uint256"},{"type":"uint256","name":"amountB","internalType":"uint256"},{"type":"uint256","name":"liquidity","internalType":"uint256"}],"name":"addLiquidity","inputs":[{"type":"address","name":"tokenA","internalType":"address"},{"type":"address","name":"tokenB","internalType":"address"},{"type":"uint256","name":"amountADesired","internalType":"uint256"},{"type":"uint256","name":"amountBDesired","internalType":"uint256"},{"type":"uint256","name":"amountAMin","internalType":"uint256"},{"type":"uint256","name":"amountBMin","internalType":"uint256"},{"type":"address","name":"to","internalType":"address"},{"type":"uint256","name":"deadline","internalType":"uint256"}]},{"type":"function","stateMutability":"payable","outputs":[{"type":"uint256","name":"amountToken","internalType":"uint256"},{"type":"uint256","name":"amountAVAX","internalType":"uint256"},{"type":"uint256","name":"liquidity","internalType":"uint256"}],"name":"addLiquidityAVAX","inputs":[{"type":"address","name":"token","internalType":"address"},{"type":"uint256","name":"amountTokenDesired","internalType":"uint256"},{"type":"uint256","name":"amountTokenMin","internalType":"uint256"},{"type":"uint256","name":"amountAVAXMin","internalType":"uint256"},{"type":"address","name":"to","internalType":"address"},{"type":"uint256","name":"deadline","internalType":"uint256"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"address","name":"","internalType":"address"}],"name":"factory","inputs":[]},{"type":"function","stateMutability":"pure","outputs":[{"type":"uint256","name":"amountIn","internalType":"uint256"}],"name":"getAmountIn","inputs":[{"type":"uint256","name":"amountOut","internalType":"uint256"},{"type":"uint256","name":"reserveIn","internalType":"uint256"},{"type":"uint256","name":"reserveOut","internalType":"uint256"}]},{"type":"function","stateMutability":"pure","outputs":[{"type":"uint256","name":"amountOut","internalType":"uint256"}],"name":"getAmountOut","inputs":[{"type":"uint256","name":"amountIn","internalType":"uint256"},{"type":"uint256","name":"reserveIn","internalType":"uint256"},{"type":"uint256","name":"reserveOut","internalType":"uint256"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256[]","name":"amounts","internalType":"uint256[]"}],"name":"getAmountsIn","inputs":[{"type":"uint256","name":"amountOut","internalType":"uint256"},{"type":"address[]","name":"path","internalType":"address[]"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256[]","name":"amounts","internalType":"uint256[]"}],"name":"getAmountsOut","inputs":[{"type":"uint256","name":"amountIn","internalType":"uint256"},{"type":"address[]","name":"path","internalType":"address[]"}]},{"type":"function","stateMutability":"pure","outputs":[{"type":"uint256","name":"amountB","internalType":"uint256"}],"name":"quote","inputs":[{"type":"uint256","name":"amountA","internalType":"uint256"},{"type":"uint256","name":"reserveA","internalType":"uint256"},{"type":"uint256","name":"reserveB","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[{"type":"uint256","name":"amountA","internalType":"uint256"},{"type":"uint256","name":"amountB","internalType":"uint256"}],"name":"removeLiquidity","inputs":[{"type":"address","name":"tokenA","internalType":"address"},{"type":"address","name":"tokenB","internalType":"address"},{"type":"uint256","name":"liquidity","internalType":"uint256"},{"type":"uint256","name":"amountAMin","internalType":"uint256"},{"type":"uint256","name":"amountBMin","internalType":"uint256"},{"type":"address","name":"to","internalType":"address"},{"type":"uint256","name":"deadline","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[{"type":"uint256","name":"amountToken","internalType":"uint256"},{"type":"uint256","name":"amountAVAX","internalType":"uint256"}],"name":"removeLiquidityAVAX","inputs":[{"type":"address","name":"token","internalType":"address"},{"type":"uint256","name":"liquidity","internalType":"uint256"},{"type":"uint256","name":"amountTokenMin","internalType":"uint256"},{"type":"uint256","name":"amountAVAXMin","internalType":"uint256"},{"type":"address","name":"to","internalType":"address"},{"type":"uint256","name":"deadline","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[{"type":"uint256","name":"amountAVAX","internalType":"uint256"}],"name":"removeLiquidityAVAXSupportingFeeOnTransferTokens","inputs":[{"type":"address","name":"token","internalType":"address"},{"type":"uint256","name":"liquidity","internalType":"uint256"},{"type":"uint256","name":"amountTokenMin","internalType":"uint256"},{"type":"uint256","name":"amountAVAXMin","internalType":"uint256"},{"type":"address","name":"to","internalType":"address"},{"type":"uint256","name":"deadline","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[{"type":"uint256","name":"amountToken","internalType":"uint256"},{"type":"uint256","name":"amountAVAX","internalType":"uint256"}],"name":"removeLiquidityAVAXWithPermit","inputs":[{"type":"address","name":"token","internalType":"address"},{"type":"uint256","name":"liquidity","internalType":"uint256"},{"type":"uint256","name":"amountTokenMin","internalType":"uint256"},{"type":"uint256","name":"amountAVAXMin","internalType":"uint256"},{"type":"address","name":"to","internalType":"address"},{"type":"uint256","name":"deadline","internalType":"uint256"},{"type":"bool","name":"approveMax","internalType":"bool"},{"type":"uint8","name":"v","internalType":"uint8"},{"type":"bytes32","name":"r","internalType":"bytes32"},{"type":"bytes32","name":"s","internalType":"bytes32"}]},{"type":"function","stateMutability":"nonpayable","outputs":[{"type":"uint256","name":"amountAVAX","internalType":"uint256"}],"name":"removeLiquidityAVAXWithPermitSupportingFeeOnTransferTokens","inputs":[{"type":"address","name":"token","internalType":"address"},{"type":"uint256","name":"liquidity","internalType":"uint256"},{"type":"uint256","name":"amountTokenMin","internalType":"uint256"},{"type":"uint256","name":"amountAVAXMin","internalType":"uint256"},{"type":"address","name":"to","internalType":"address"},{"type":"uint256","name":"deadline","internalType":"uint256"},{"type":"bool","name":"approveMax","internalType":"bool"},{"type":"uint8","name":"v","internalType":"uint8"},{"type":"bytes32","name":"r","internalType":"bytes32"},{"type":"bytes32","name":"s","internalType":"bytes32"}]},{"type":"function","stateMutability":"nonpayable","outputs":[{"type":"uint256","name":"amountA","internalType":"uint256"},{"type":"uint256","name":"amountB","internalType":"uint256"}],"name":"removeLiquidityWithPermit","inputs":[{"type":"address","name":"tokenA","internalType":"address"},{"type":"address","name":"tokenB","internalType":"address"},{"type":"uint256","name":"liquidity","internalType":"uint256"},{"type":"uint256","name":"amountAMin","internalType":"uint256"},{"type":"uint256","name":"amountBMin","internalType":"uint256"},{"type":"address","name":"to","internalType":"address"},{"type":"uint256","name":"deadline","internalType":"uint256"},{"type":"bool","name":"approveMax","internalType":"bool"},{"type":"uint8","name":"v","internalType":"uint8"},{"type":"bytes32","name":"r","internalType":"bytes32"},{"type":"bytes32","name":"s","internalType":"bytes32"}]},{"type":"function","stateMutability":"payable","outputs":[{"type":"uint256[]","name":"amounts","internalType":"uint256[]"}],"name":"swapAVAXForExactTokens","inputs":[{"type":"uint256","name":"amountOut","internalType":"uint256"},{"type":"address[]","name":"path","internalType":"address[]"},{"type":"address","name":"to","internalType":"address"},{"type":"uint256","name":"deadline","internalType":"uint256"}]},{"type":"function","stateMutability":"payable","outputs":[{"type":"uint256[]","name":"amounts","internalType":"uint256[]"}],"name":"swapExactAVAXForTokens","inputs":[{"type":"uint256","name":"amountOutMin","internalType":"uint256"},{"type":"address[]","name":"path","internalType":"address[]"},{"type":"address","name":"to","internalType":"address"},{"type":"uint256","name":"deadline","internalType":"uint256"}]},{"type":"function","stateMutability":"payable","outputs":[],"name":"swapExactAVAXForTokensSupportingFeeOnTransferTokens","inputs":[{"type":"uint256","name":"amountOutMin","internalType":"uint256"},{"type":"address[]","name":"path","internalType":"address[]"},{"type":"address","name":"to","internalType":"address"},{"type":"uint256","name":"deadline","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[{"type":"uint256[]","name":"amounts","internalType":"uint256[]"}],"name":"swapExactTokensForAVAX","inputs":[{"type":"uint256","name":"amountIn","internalType":"uint256"},{"type":"uint256","name":"amountOutMin","internalType":"uint256"},{"type":"address[]","name":"path","internalType":"address[]"},{"type":"address","name":"to","internalType":"address"},{"type":"uint256","name":"deadline","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"swapExactTokensForAVAXSupportingFeeOnTransferTokens","inputs":[{"type":"uint256","name":"amountIn","internalType":"uint256"},{"type":"uint256","name":"amountOutMin","internalType":"uint256"},{"type":"address[]","name":"path","internalType":"address[]"},{"type":"address","name":"to","internalType":"address"},{"type":"uint256","name":"deadline","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[{"type":"uint256[]","name":"amounts","internalType":"uint256[]"}],"name":"swapExactTokensForTokens","inputs":[{"type":"uint256","name":"amountIn","internalType":"uint256"},{"type":"uint256","name":"amountOutMin","internalType":"uint256"},{"type":"address[]","name":"path","internalType":"address[]"},{"type":"address","name":"to","internalType":"address"},{"type":"uint256","name":"deadline","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"swapExactTokensForTokensSupportingFeeOnTransferTokens","inputs":[{"type":"uint256","name":"amountIn","internalType":"uint256"},{"type":"uint256","name":"amountOutMin","internalType":"uint256"},{"type":"address[]","name":"path","internalType":"address[]"},{"type":"address","name":"to","internalType":"address"},{"type":"uint256","name":"deadline","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[{"type":"uint256[]","name":"amounts","internalType":"uint256[]"}],"name":"swapTokensForExactAVAX","inputs":[{"type":"uint256","name":"amountOut","internalType":"uint256"},{"type":"uint256","name":"amountInMax","internalType":"uint256"},{"type":"address[]","name":"path","internalType":"address[]"},{"type":"address","name":"to","internalType":"address"},{"type":"uint256","name":"deadline","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[{"type":"uint256[]","name":"amounts","internalType":"uint256[]"}],"name":"swapTokensForExactTokens","inputs":[{"type":"uint256","name":"amountOut","internalType":"uint256"},{"type":"uint256","name":"amountInMax","internalType":"uint256"},{"type":"address[]","name":"path","internalType":"address[]"},{"type":"address","name":"to","internalType":"address"},{"type":"uint256","name":"deadline","internalType":"uint256"}]},{"type":"receive","stateMutability":"payable"}]'
spooky_router_contract = w3.eth.contract(spooky_router_addr, abi=spooky_router_abi)

joe_factory_addr = w3.toChecksumAddress('0x9Ad6C38BE94206cA50bb0d90783181662f0Cfa10')
joe_factory_abi = '[{"type":"constructor","stateMutability":"nonpayable","inputs":[{"type":"address","name":"_feeToSetter","internalType":"address"}]},{"type":"event","name":"PairCreated","inputs":[{"type":"address","name":"token0","internalType":"address","indexed":true},{"type":"address","name":"token1","internalType":"address","indexed":true},{"type":"address","name":"pair","internalType":"address","indexed":false},{"type":"uint256","name":"","internalType":"uint256","indexed":false}],"anonymous":false},{"type":"function","stateMutability":"view","outputs":[{"type":"address","name":"","internalType":"address"}],"name":"allPairs","inputs":[{"type":"uint256","name":"","internalType":"uint256"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"allPairsLength","inputs":[]},{"type":"function","stateMutability":"nonpayable","outputs":[{"type":"address","name":"pair","internalType":"address"}],"name":"createPair","inputs":[{"type":"address","name":"tokenA","internalType":"address"},{"type":"address","name":"tokenB","internalType":"address"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"address","name":"","internalType":"address"}],"name":"feeTo","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"address","name":"","internalType":"address"}],"name":"feeToSetter","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"address","name":"","internalType":"address"}],"name":"getPair","inputs":[{"type":"address","name":"","internalType":"address"},{"type":"address","name":"","internalType":"address"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"address","name":"","internalType":"address"}],"name":"migrator","inputs":[]},{"type":"function","stateMutability":"pure","outputs":[{"type":"bytes32","name":"","internalType":"bytes32"}],"name":"pairCodeHash","inputs":[]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"setFeeTo","inputs":[{"type":"address","name":"_feeTo","internalType":"address"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"setFeeToSetter","inputs":[{"type":"address","name":"_feeToSetter","internalType":"address"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"setMigrator","inputs":[{"type":"address","name":"_migrator","internalType":"address"}]}]'
joe_factory_contract = w3.eth.contract(joe_factory_addr, abi=joe_factory_abi)

# blzz/AVAX PAIR POOL ON TRADERJOE
blzz_avax_pool_joe_addr = w3.toChecksumAddress('0xac3f978714c613e768272c502a8912bc03dcf624')
blzz_avax_pool_joe_abi = '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Burn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount0Out","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1Out","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Swap","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint112","name":"reserve0","type":"uint112"},{"indexed":false,"internalType":"uint112","name":"reserve1","type":"uint112"}],"name":"Sync","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MINIMUM_LIQUIDITY","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"PERMIT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"burn","outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getReserves","outputs":[{"internalType":"uint112","name":"_reserve0","type":"uint112"},{"internalType":"uint112","name":"_reserve1","type":"uint112"},{"internalType":"uint32","name":"_blockTimestampLast","type":"uint32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_token0","type":"address"},{"internalType":"address","name":"_token1","type":"address"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"kLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"mint","outputs":[{"internalType":"uint256","name":"liquidity","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"price0CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"price1CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"skim","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount0Out","type":"uint256"},{"internalType":"uint256","name":"amount1Out","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"swap","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"sync","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"token0","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"token1","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]'
blzz_avax_pool_joe_contract = w3.eth.contract(blzz_avax_pool_joe_addr, abi=blzz_avax_pool_joe_abi)

# blzz PODL
blzz_arb_addr = w3.toChecksumAddress('0x8d426bfe128b171d8fd38a58dfea257f01206f34')
blzz_arb_abi = '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"buyer","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"SoldAVAX","type":"event"},{"inputs":[],"name":"availableAVAX","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"bAVAX","outputs":[{"internalType":"contract IERC20","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"buyAVAX","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"lpToken","outputs":[{"internalType":"contract IJoePair","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"lpTokensPerOneAVAX","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"protocolOwnedReserves","outputs":[{"internalType":"uint256","name":"blizz","type":"uint256"},{"internalType":"uint256","name":"wavax","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSoldAVAX","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"treasury","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"}]'
blzz_arb_contract = w3.eth.contract(blzz_arb_addr, abi=blzz_arb_abi)

blzz_weth_addr = w3.toChecksumAddress('0x56D0fEd06d2e0B5AC80d7a9ed0387694bDf90C33')
blzz_weth_abi = '[{"inputs":[{"internalType":"address","name":"weth","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"stateMutability":"payable","type":"fallback"},{"inputs":[{"internalType":"address","name":"lendingPool","type":"address"}],"name":"authorizeLendingPool","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"lendingPool","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"interesRateMode","type":"uint256"},{"internalType":"uint16","name":"referralCode","type":"uint16"}],"name":"borrowETH","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"lendingPool","type":"address"},{"internalType":"address","name":"onBehalfOf","type":"address"},{"internalType":"uint16","name":"referralCode","type":"uint16"}],"name":"depositETH","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"emergencyEtherTransfer","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"emergencyTokenTransfer","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getWETHAddress","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"lendingPool","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"rateMode","type":"uint256"},{"internalType":"address","name":"onBehalfOf","type":"address"}],"name":"repayETH","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"lendingPool","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"address","name":"to","type":"address"}],"name":"withdrawETH","outputs":[],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]'
blzz_weth_contract = w3.eth.contract(blzz_weth_addr, abi=blzz_weth_abi)
# FUNCTIONS
bAVAX_addr = w3.toChecksumAddress('0xb2ac04b71888e17aa2c5102cf3d0215467d74100')
bAVAX_abi = '[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"index","type":"uint256"}],"name":"BalanceTransfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"target","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"index","type":"uint256"}],"name":"Burn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"underlyingAsset","type":"address"},{"indexed":true,"internalType":"address","name":"pool","type":"address"},{"indexed":false,"internalType":"address","name":"treasury","type":"address"},{"indexed":false,"internalType":"address","name":"incentivesController","type":"address"},{"indexed":false,"internalType":"uint8","name":"aTokenDecimals","type":"uint8"},{"indexed":false,"internalType":"string","name":"aTokenName","type":"string"},{"indexed":false,"internalType":"string","name":"aTokenSymbol","type":"string"},{"indexed":false,"internalType":"bytes","name":"params","type":"bytes"}],"name":"Initialized","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"index","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[],"name":"ATOKEN_REVISION","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"EIP712_REVISION","outputs":[{"internalType":"bytes","name":"","type":"bytes"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"PERMIT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"POOL","outputs":[{"internalType":"contract ILendingPool","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"RESERVE_TREASURY_ADDRESS","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"UNDERLYING_ASSET_ADDRESS","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"_nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"},{"internalType":"address","name":"receiverOfUnderlying","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getAssetPrice","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getIncentivesController","outputs":[{"internalType":"contract IAaveIncentivesController","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"getScaledUserBalanceAndSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"handleRepayment","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract ILendingPool","name":"pool","type":"address"},{"internalType":"address","name":"treasury","type":"address"},{"internalType":"address","name":"underlyingAsset","type":"address"},{"internalType":"contract IAaveIncentivesController","name":"incentivesController","type":"address"},{"internalType":"uint8","name":"aTokenDecimals","type":"uint8"},{"internalType":"string","name":"aTokenName","type":"string"},{"internalType":"string","name":"aTokenSymbol","type":"string"},{"internalType":"bytes","name":"params","type":"bytes"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"mint","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"mintToTreasury","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"scaledBalanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"scaledTotalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferOnLiquidation","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"target","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferUnderlyingTo","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"}]'
bAVAX_contract = w3.eth.contract(bAVAX_addr, abi=bAVAX_abi)

blzz_addr = w3.toChecksumAddress('0x0f34919404a290e71fc6A510cB4a6aCb8D764b24')
blzz_abi = '[{"inputs":[{"internalType":"uint256","name":"_maxTotalSupply","type":"uint256"},{"internalType":"uint256","name":"_maxTreasuryMintable","type":"uint256"},{"internalType":"uint256","name":"_startTime","type":"uint256"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_spender","type":"address"},{"internalType":"uint256","name":"_value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxTotalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxTreasuryMintable","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_value","type":"uint256"}],"name":"mint","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"minter","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_minter","type":"address"}],"name":"setMinter","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_treasury","type":"address"}],"name":"setTreasury","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"startTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_from","type":"address"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"treasury","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"treasuryMintedTokens","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]'
blzz_contract = w3.eth.contract(blzz_addr, abi=blzz_abi)



lend_pool_addr = w3.toChecksumAddress('0x70BbE4A294878a14CB3CDD9315f5EB490e346163')

# DAI/AVAX PAIR POOL ON TRADERJOE
dai_avax_pool_joe_addr = w3.toChecksumAddress('0xac3f978714c613e768272c502a8912bc03dcf624')
dai_avax_pool_joe_abi = '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Burn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount0Out","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1Out","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Swap","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint112","name":"reserve0","type":"uint112"},{"indexed":false,"internalType":"uint112","name":"reserve1","type":"uint112"}],"name":"Sync","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MINIMUM_LIQUIDITY","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"PERMIT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"burn","outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getReserves","outputs":[{"internalType":"uint112","name":"_reserve0","type":"uint112"},{"internalType":"uint112","name":"_reserve1","type":"uint112"},{"internalType":"uint32","name":"_blockTimestampLast","type":"uint32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_token0","type":"address"},{"internalType":"address","name":"_token1","type":"address"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"kLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"mint","outputs":[{"internalType":"uint256","name":"liquidity","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"price0CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"price1CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"skim","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount0Out","type":"uint256"},{"internalType":"uint256","name":"amount1Out","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"swap","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"sync","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"token0","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"token1","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]'
dai_avax_pool_joe_contract = w3.eth.contract(dai_avax_pool_joe_addr, abi=dai_avax_pool_joe_abi)
#
wavax_addr = w3.toChecksumAddress("0xB31f66AA3C1e785363F0875A1B74E27b85FD66c7")

def get_bal():
    return bAVAX_contract.functions.balanceOf(blzz_arb_addr).call()
#     buffer = BytesIO()
#
#     c.setopt(c.URL,
#              'https://deep-index.moralis.io/api/v2/0x8d426bfe128b171d8fd38a58dfea257f01206f34/erc20?chain=0xa86a')
#     c.setopt(pycurl.HTTPHEADER, ['Accept: application/json',
#                                  'X-API-Key: Snf79KoB1gTJb2WexTlojgWQJCA7eflmCNR4jqG2PiATzT7D8c08Wl4I8cAHDSx2'])
#     c.setopt(c.WRITEDATA, buffer)
#     c.setopt(c.CAINFO, certifi.where())
#     c.perform()
#     # c.close()
#
#     return int(ujson.loads(buffer.getvalue())[1]['balance'])
# # def send_arb(bal, last):
#     number = w3.eth.block_number
#     block = requests.get(
#         f"https://api.snowtrace.io/api?module=account&action=tokentx&address=0x8d426bfe128b171d8fd38a58dfea257f01206f34&startblock={number}&endblock={number}&sort=desc&apikey=C61VPEA18VV5YF2WK13MFYYJ487YBICSP3").json()
#     print(f"current bal: {bal}, block: {block}")
#     for i in block['result']:
#         if i['from'] == '0x0000000000000000000000000000000000000000':
#             if (int(i['value']) != last):
#                 last = int(i['value'])
#                 return (bal + last, last)
#     return bal, last
# import time
# start = time.time()
# x=0
# bAVAX_contract.functions.approve(blzz_arb_addr,
#                                              115792089237316195423570985008687907853269984665640564039457584007913129639935).call()


while True:
    # time.sleep(0.00000000000000000000000000001)

    # blzz_lp_balance_wei = blzz_avax_pool_joe_contract.functions.balanceOf(wallet_addr).call()
    # blzz_lp_balance = w3.fromWei(blzz_lp_balance_wei, 'ether')
    #
    # blzz_arb_bal_wei = blzz_arb_contract.functions.availableAVAX().call()
    # blzz_arb_bal = w3.fromWei(blzz_arb_bal_wei, 'ether')
    #
    # lp_per_AVAX_wei = blzz_arb_contract.functions.lpTokensPerOneAVAX().call()
    # lp_per_AVAX= w3.fromWei(lp_per_AVAX_wei, 'ether')
    blzz_lp_balance_wei = blzz_avax_pool_joe_contract.functions.balanceOf(wallet_addr).call()
    blzz_lp_balance = w3.fromWei(blzz_lp_balance_wei, 'ether')
    lp_per_AVAX_wei = blzz_arb_contract.functions.lpTokensPerOneAVAX().call()
    lp_per_AVAX = w3.fromWei(lp_per_AVAX_wei, 'ether')

    if (blzz_lp_balance_wei < 3*lp_per_AVAX_wei) and (w3.fromWei(w3.eth.gas_price, 'ether') < 250):
        avax_balance_wei = w3.eth.get_balance(wallet_addr)
        avax_balance = w3.fromWei(avax_balance_wei, 'ether')

        blzz_balance_wei = blzz_contract.functions.balanceOf(wallet_addr).call()
        blzz_balance = w3.fromWei(blzz_balance_wei, 'ether')

        bAVAX_balance_wei = bAVAX_contract.functions.balanceOf(wallet_addr).call()
        bAVAX_balance = w3.fromWei(bAVAX_balance_wei, 'ether')
        if bAVAX_balance > 5:
            withdraw_tx = blzz_weth_contract.functions.withdrawETH(lend_pool_addr, bAVAX_balance_wei, wallet_addr).buildTransaction({
                            'gas': 1600000,
                            'gasPrice': w3.eth.gas_price + w3.toWei(20, 'gwei'),
                            'from': wallet_addr,
                            'nonce': w3.eth.get_transaction_count(wallet_addr),
                        })
            # logging.info("Smart Contract Functions Created for Withdrawal")
            # logging.info("Attempting to Sign Withdrawal transaction...")
            signed_txn = w3.eth.account.signTransaction(
                withdraw_tx,
                private_key=private_key
            )
            # logging.info("Withdrawal Transaction is Signed")
            # logging.info("Attempting to Send Withdrawal Transaction...")

            with_hex_output = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
            # logging.info("Withdrawal Transaction has been sent")

            # logging.info("Withdrawal Transaction is waiting to be mined...")

            tx_receipt = w3.eth.wait_for_transaction_receipt(with_hex_output)
            # logging.info(with_hex_output)

            # logging.info("Arb Transaction has been mined")
            print(f"Withdrew {bAVAX_balance} bAVAX")

        # Parameters

        # AVAX => TOKEN SWAP - BUY
        # logging.info("Attempting to calculate buy trade...")

        # Trade Math

        sleep(10)
        avax_balance_wei = w3.eth.get_balance(wallet_addr)
        avax_balance = w3.fromWei(avax_balance_wei, 'ether')
        trade_amount = min(float(avax_balance)*0.85, 5)
        trade_start_balance = trade_amount/2
        trade_amount_wei = w3.toWei(trade_start_balance, 'ether')
        slippage = 0.02

        reserves_wei = blzz_avax_pool_joe_contract.functions.getReserves().call()
        reserveOfToken0 = w3.fromWei(reserves_wei[0], 'ether')
        reserveOfToken1 = w3.fromWei(reserves_wei[1], 'ether')

        currency_rate = reserveOfToken0 / reserveOfToken1
        # Currency arrangement for amountOutMin
        path = [blzz_avax_pool_joe_contract.functions.token1().call(), blzz_avax_pool_joe_contract.functions.token0().call()]
        to = wallet_addr
        deadline = int(time.time() * 1000 + 1000 * 60 * 10)  # deadline is 10 minutes
        amountOutMin = int((trade_amount_wei - trade_amount_wei * slippage) * float(currency_rate))
        params = (amountOutMin, path, to, deadline)

        # logging.info("Calculate buy trade is completed")

        # Seperate and Create Transaction
        # logging.info("Attempting to seperate Smart Contract Buy Function and Create Transaction...")
        buy_tx = spooky_router_contract.functions.swapExactAVAXForTokens(amountOutMin, path, to, deadline).buildTransaction({
            'gas': 1000000,
            'gasPrice': w3.eth.gas_price + w3.toWei(30, 'gwei'),
            'from': wallet_addr,
            'nonce': w3.eth.get_transaction_count(wallet_addr),
            'value': trade_amount_wei
        })
        signed_txn = w3.eth.account.signTransaction(
            buy_tx,
            private_key=private_key
        )

        # logging.info("buy Transaction is Signed")
        # logging.info("Attempting to Send buy Transaction...")

        buy_hex_output = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        # logging.info("buy Transaction has been sent")

        # logging.info("buy Transaction is waiting to be mined...")

        tx_receipt = w3.eth.wait_for_transaction_receipt(buy_hex_output)
        # logging.info(buy_hex_output)
        sleep(10)
        blzz_balance_wei = blzz_contract.functions.balanceOf(wallet_addr).call()
        blzz_balance = w3.fromWei(blzz_balance_wei, 'ether')
        blzz_balance_wei = w3.toWei(float(blzz_balance)*0.99, 'ether')
        blzz_balance_min = w3.toWei(float(blzz_balance)*0.95, 'ether')
        reserves_wei = blzz_avax_pool_joe_contract.functions.getReserves().call()
        reserveOfToken0 = w3.fromWei(reserves_wei[0], 'ether')
        reserveOfToken1 = w3.fromWei(reserves_wei[1], 'ether')

        currency_rate = reserveOfToken0 / reserveOfToken1
        avax_balance_min = float(blzz_balance)*0.95/float(currency_rate)
        avax_balance_min_wei = w3.toWei(avax_balance_min, 'ether')
        pool_tx = spooky_router_contract.functions.addLiquidityAVAX(blzz_addr, blzz_balance_wei, blzz_balance_min, avax_balance_min_wei, wallet_addr, deadline).buildTransaction({
            'gas': 1000000,
            'gasPrice': w3.eth.gas_price + w3.toWei(30, 'gwei'),
            'from': wallet_addr,
            'nonce': w3.eth.get_transaction_count(wallet_addr),
            'value': w3.toWei(float(blzz_balance)/float(currency_rate), 'ether')
        })
        signed_txn = w3.eth.account.signTransaction(
            pool_tx,
            private_key=private_key
        )
        # logging.info("buy Transaction is Signed")
        # logging.info("Attempting to Send buy Transaction...")

        pool_hex_output = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

        #logging.info("pool Transaction has been sent")

        #logging.info("pool Transaction is waiting to be mined...")

        tx_receipt = w3.eth.wait_for_transaction_receipt(pool_hex_output)

        #logging.info(pool_hex_output)
        del tx_receipt
        del signed_txn
        del pool_hex_output
        del pool_tx
        del avax_balance_min_wei
        del avax_balance_wei
        del path
        del to
        del deadline
        del currency_rate
        del reserveOfToken0
        del reserveOfToken1
        del reserves_wei
        del blzz_balance_wei
        del blzz_balance
        del blzz_balance_min
        del buy_tx
        del buy_hex_output
        del amountOutMin
        del params
        del slippage
        del trade_amount_wei
        del trade_start_balance
        del trade_amount
        del avax_balance
        del bAVAX_balance
        del bAVAX_balance_wei
        del with_hex_output
        del withdraw_tx
        gc.collect()
        print("added liquidity!!")
    gas = w3.eth.gas_price
    pfof = 32000000000
    signed_txn1 = w3.eth.account.signTransaction(
        blzz_arb_contract.functions.buyAVAX(1000000000000000000).buildTransaction({
            'gas': 350000,
            'maxFeePerGas': gas + pfof,
            'maxPriorityFeePerGas': pfof,
            'from': wallet_addr,
            'nonce': w3.eth.get_transaction_count(wallet_addr),
            'type': '0x2',
        }),
        private_key=private_key
    )

    bal = (bAVAX_contract.functions.balanceOf(blzz_arb_addr).call())
    print(blzz_avax_pool_joe_contract.all_functions())
    #bAVAX_contract.functions.transferFrom(blzz_arb_addr, wallet_addr, 1000000000000000000).call()
    # bAVAX_contract.functions.transferFrom(blzz_arb_addr, wallet_addr, 1000000000000000000).call({
    #     'gas': 350000,
    #     'maxFeePerGas': gas + pfof,
    #     'maxPriorityFeePerGas': pfof,
    #     'from': wallet_addr,
    #     'nonce': w3.eth.get_transaction_count(wallet_addr),
    #     'type': '0x2',
    # })
    #bAVAX_contract.functions.transferFrom(blzz_arb_addr, wallet_addr, 200000000000000).call()
    # while True:
    #     try:
    #         print(f"Tried")
    #         bAVAX_contract.functions.transferFrom(blzz_arb_addr, wallet_addr, 1000000000000000000).call()
    #     #     x = blzz_arb_contract.functions.buyAVAX(1000000000000000000).call({
    #     #     'gas': 350000,
    #     #     'maxFeePerGas': gas + pfof,
    #     #     'maxPriorityFeePerGas': pfof,
    #     #     'from': wallet_addr,
    #     #     'nonce': w3.eth.get_transaction_count(wallet_addr),
    #     #     'type': '0x2',
    #     # })
    #
    #         arb_hex_output = w3.eth.sendRawTransaction(signed_txn1.rawTransaction)
    #         print(f"SENT ARB OF {bal}")
    #         tx_receipt = w3.eth.wait_for_transaction_receipt(arb_hex_output)
    # #         y=9
    #     except:
    #         y = 0



    if (gas < 235000000000) and (blzz_lp_balance_wei > 2*lp_per_AVAX_wei):

        while bal < 2000000000000000000:

            try:

                bal = get_bal()
                # print(bal)
            except:


                try:
                     bal = bAVAX_contract.functions.balanceOf(blzz_arb_addr).call()
                     print(f"{bal}: w3 ws API, error with Moralis")
                except:
                    bal = int(requests.get((
                                               f"https://api.snowtrace.io/api?module=account&action=tokenbalance&contractaddress={'0xb2ac04b71888e17aa2c5102cf3d0215467d74100'}&address={'0x8d426bfe128b171d8fd38a58dfea257f01206f34'}&tag=latest&apikey='C61VPEA18VV5YF2WK13MFYYJ487YBICSP3'")).json()[
                                  'result'])
                    #sleep(10)

            #print(f"Public API: {bal / 2000000000000000000}")
    bal = bal//2
    if bal >= 1400000000000000000 and (blzz_lp_balance_wei > (lp_per_AVAX_wei*bal / 1000000000000000000)):
        signed_txn = w3.eth.account.signTransaction(
            blzz_arb_contract.functions.buyAVAX(bal).buildTransaction({
                'gas': 400000,
                'maxFeePerGas': w3.eth.gas_price + pfof,
                'maxPriorityFeePerGas': pfof,
                'from': wallet_addr,
                'nonce': w3.eth.get_transaction_count(wallet_addr),
                'type': '0x2',
            }),
            private_key=private_key
        )
        try:
            arb_hex_output = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
            print(f"SENT ARB OF {bal}")
            tx_receipt = w3.eth.wait_for_transaction_receipt(arb_hex_output)
            del arb_hex_output
            del tx_receipt
            del signed_txn
            del gas
            del bal
            del lp_per_AVAX_wei
            del blzz_lp_balance_wei
            gc.collect()
            sleep(10)
        except:
            del signed_txn
            del gas
            del bal
            del lp_per_AVAX_wei
            del blzz_lp_balance_wei
            gc.collect()
            sleep(10)

    elif blzz_lp_balance_wei > (lp_per_AVAX_wei*max(bal, 2000000000000000000) / 1000000000000000000):
        try:
            arb_hex_output = w3.eth.sendRawTransaction(signed_txn1.rawTransaction)
            print(f"SENT ARB OF {bal}")
            tx_receipt = w3.eth.wait_for_transaction_receipt(arb_hex_output)
            del arb_hex_output
            del tx_receipt
            del signed_txn1
            del gas
            del bal
            del lp_per_AVAX_wei
            del blzz_lp_balance_wei
            gc.collect()
            sleep(5)
        except:
            del signed_txn1
            del gas
            del bal
            del lp_per_AVAX_wei
            del blzz_lp_balance_wei
            gc.collect()
            sleep(5)

    # except:
    #     sleep(1)
    # if bal < (float(blzz_lp_balance/lp_per_AVAX)*1000000000000000000):
    #         signed_txn = w3.eth.account.signTransaction(
    #             blzz_arb_contract.functions.buyAVAX(bal).buildTransaction({
    #                 'gas': 400000,
    #                 'maxFeePerGas': gas + 40000000000,
    #                 'maxPriorityFeePerGas': 40000000000,
    #                 'from': wallet_addr,
    #                 'nonce': w3.eth.get_transaction_count(wallet_addr),
    #                 'type': '0x2',
    #             }),
    #             private_key=private_key
    #         )
    #         arb_hex_output = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    #         tx_receipt = w3.eth.wait_for_transaction_receipt(arb_hex_output)
    # else:
    #         arb_amt = w3.toWei(blzz_lp_balance/lp_per_AVAX, 'ether')
    #         signed_txn = w3.eth.account.signTransaction(
    #             blzz_arb_contract.functions.buyAVAX(arb_amt).buildTransaction({
    #                 'gas': 400000,
    #                 'maxFeePerGas': gas + 40000000000,
    #                 'maxPriorityFeePerGas': 40000000000,
    #                 'from': wallet_addr,
    #                 'nonce': w3.eth.get_transaction_count(wallet_addr),
    #                 'type': '0x2',
    #             }),
    #             private_key=private_key
    #         )
    #         arb_hex_output = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    #         tx_receipt = w3.eth.wait_for_transaction_receipt(arb_hex_output)
        # if blzz_arb_bal < (float(blzz_lp_balance/lp_per_AVAX)):
        #     arb_tx = blzz_arb_contract.functions.buyAVAX(blzz_arb_bal_wei).buildTransaction({
        #                 'gas': 4000000,
        #                 'gasPrice': w3.eth.gas_price + w3.toWei(35, 'gwei'),
        #                 'from': wallet_addr,
        #                 'nonce': w3.eth.get_transaction_count(wallet_addr),
        #
        #             })
        #
        # else:
        #     arb_amt = w3.toWei(blzz_lp_balance/lp_per_AVAX, 'ether')
        #     arb_tx = blzz_arb_contract.functions.buyAVAX(arb_amt).buildTransaction({
        #         'gas': 4000000,
        #         'gasPrice': w3.eth.gas_price + w3.toWei(35, 'gwei'),
        #         'from': wallet_addr,
        #         'nonce': w3.eth.get_transaction_count(wallet_addr),
        #     })
        #logging.info("Smart Contract Functions Created for Arb")
        #logging.info("Attempting to Sign Arb transaction...")
    # signed_txn = w3.eth.account.signTransaction(
    #             arb_tx,
    #             private_key=private_key
    #         )
        #logging.info("Arb Transaction is Signed")
        #logging.info("Attempting to Send arb Transaction...")
    #

    #     #logging.info(arb_hex_output)


        #logging.info("Arb Transaction has been mined")

    #sleep(2)

    # logging.info("")
    # logging.info("")
    # logging.info("New Check is starting...")
    # logging.info("---------- WALLET BALANCES ----------")
    # logging.info("AVAX: " + str(avax_balance))
    # logging.info("BLZZ: " + str(blzz_balance))
    # logging.info("bAVAX: " + str(bAVAX_balance))
    # logging.info("BLZZ AVAX LP: " + str(blzz_lp_balance))
    # logging.info("BLZZ Arb Bal: " + str(blzz_arb_bal))
    # logging.info(" ")


    #
    # if (blzz_lp_balance_wei < min(lp_per_AVAX_wei*bal / 1000000000000000000, 2.5*lp_per_AVAX_wei)) and (w3.fromWei(w3.eth.gas_price, 'ether') < 250):
    #     avax_balance_wei = w3.eth.get_balance(wallet_addr)
    #     avax_balance = w3.fromWei(avax_balance_wei, 'ether')
    #
    #     blzz_balance_wei = blzz_contract.functions.balanceOf(wallet_addr).call()
    #     blzz_balance = w3.fromWei(blzz_balance_wei, 'ether')
    #
    #     bAVAX_balance_wei = bAVAX_contract.functions.balanceOf(wallet_addr).call()
    #     bAVAX_balance = w3.fromWei(bAVAX_balance_wei, 'ether')
    #     if bAVAX_balance > 5:
    #         withdraw_tx = blzz_weth_contract.functions.withdrawETH(lend_pool_addr, bAVAX_balance_wei, wallet_addr).buildTransaction({
    #                         'gas': 1600000,
    #                         'gasPrice': w3.eth.gas_price + w3.toWei(20, 'gwei'),
    #                         'from': wallet_addr,
    #                         'nonce': w3.eth.get_transaction_count(wallet_addr),
    #                     })
    #         # logging.info("Smart Contract Functions Created for Withdrawal")
    #         # logging.info("Attempting to Sign Withdrawal transaction...")
    #         signed_txn = w3.eth.account.signTransaction(
    #             withdraw_tx,
    #             private_key=private_key
    #         )
    #         # logging.info("Withdrawal Transaction is Signed")
    #         # logging.info("Attempting to Send Withdrawal Transaction...")
    #
    #         with_hex_output = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    #         # logging.info("Withdrawal Transaction has been sent")
    #
    #         # logging.info("Withdrawal Transaction is waiting to be mined...")
    #
    #         tx_receipt = w3.eth.wait_for_transaction_receipt(with_hex_output)
    #         # logging.info(with_hex_output)
    #
    #         # logging.info("Arb Transaction has been mined")
    #         print(f"Withdrew {bAVAX_balance} bAVAX")
    #
    #     # Parameters
    #
    #     # AVAX => TOKEN SWAP - BUY
    #     # logging.info("Attempting to calculate buy trade...")
    #
    #     # Trade Math
    #
    #     sleep(10)
    #     avax_balance_wei = w3.eth.get_balance(wallet_addr)
    #     avax_balance = w3.fromWei(avax_balance_wei, 'ether')
    #     trade_amount = min(float(avax_balance)*0.85, 20)
    #     trade_start_balance = trade_amount/2
    #     trade_amount_wei = w3.toWei(trade_start_balance, 'ether')
    #     slippage = 0.02
    #
    #     reserves_wei = blzz_avax_pool_joe_contract.functions.getReserves().call()
    #     reserveOfToken0 = w3.fromWei(reserves_wei[0], 'ether')
    #     reserveOfToken1 = w3.fromWei(reserves_wei[1], 'ether')
    #
    #     currency_rate = reserveOfToken0 / reserveOfToken1
    #     # Currency arrangement for amountOutMin
    #     path = [blzz_avax_pool_joe_contract.functions.token1().call(), blzz_avax_pool_joe_contract.functions.token0().call()]
    #     to = wallet_addr
    #     deadline = int(time.time() * 1000 + 1000 * 60 * 10)  # deadline is 10 minutes
    #     amountOutMin = int((trade_amount_wei - trade_amount_wei * slippage) * float(currency_rate))
    #     params = (amountOutMin, path, to, deadline)
    #
    #     # logging.info("Calculate buy trade is completed")
    #
    #     # Seperate and Create Transaction
    #     # logging.info("Attempting to seperate Smart Contract Buy Function and Create Transaction...")
    #     buy_tx = spooky_router_contract.functions.swapExactAVAXForTokens(amountOutMin, path, to, deadline).buildTransaction({
    #         'gas': 1000000,
    #         'gasPrice': w3.eth.gas_price + w3.toWei(30, 'gwei'),
    #         'from': wallet_addr,
    #         'nonce': w3.eth.get_transaction_count(wallet_addr),
    #         'value': trade_amount_wei
    #     })
    #     signed_txn = w3.eth.account.signTransaction(
    #         buy_tx,
    #         private_key=private_key
    #     )
    #
    #     # logging.info("buy Transaction is Signed")
    #     # logging.info("Attempting to Send buy Transaction...")
    #
    #     buy_hex_output = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    #     # logging.info("buy Transaction has been sent")
    #
    #     # logging.info("buy Transaction is waiting to be mined...")
    #
    #     tx_receipt = w3.eth.wait_for_transaction_receipt(buy_hex_output)
    #     # logging.info(buy_hex_output)
    #     sleep(10)
    #     blzz_balance_wei = blzz_contract.functions.balanceOf(wallet_addr).call()
    #     blzz_balance = w3.fromWei(blzz_balance_wei, 'ether')
    #     blzz_balance_wei = w3.toWei(float(blzz_balance)*0.99, 'ether')
    #     blzz_balance_min = w3.toWei(float(blzz_balance)*0.95, 'ether')
    #     reserves_wei = blzz_avax_pool_joe_contract.functions.getReserves().call()
    #     reserveOfToken0 = w3.fromWei(reserves_wei[0], 'ether')
    #     reserveOfToken1 = w3.fromWei(reserves_wei[1], 'ether')
    #
    #     currency_rate = reserveOfToken0 / reserveOfToken1
    #     avax_balance_min = float(blzz_balance)*0.95/float(currency_rate)
    #     avax_balance_min_wei = w3.toWei(avax_balance_min, 'ether')
    #     pool_tx = spooky_router_contract.functions.addLiquidityAVAX(blzz_addr, blzz_balance_wei, blzz_balance_min, avax_balance_min_wei, wallet_addr, deadline).buildTransaction({
    #         'gas': 1000000,
    #         'gasPrice': w3.eth.gas_price + w3.toWei(30, 'gwei'),
    #         'from': wallet_addr,
    #         'nonce': w3.eth.get_transaction_count(wallet_addr),
    #         'value': w3.toWei(float(blzz_balance)/float(currency_rate), 'ether')
    #     })
    #     signed_txn = w3.eth.account.signTransaction(
    #         pool_tx,
    #         private_key=private_key
    #     )
    #     # logging.info("buy Transaction is Signed")
    #     # logging.info("Attempting to Send buy Transaction...")
    #
    #     pool_hex_output = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    #
    #     #logging.info("pool Transaction has been sent")
    #
    #     #logging.info("pool Transaction is waiting to be mined...")
    #
    #     tx_receipt = w3.eth.wait_for_transaction_receipt(pool_hex_output)
    #
    #     #logging.info(pool_hex_output)
    #
    #     print("added liquidity!!")
    #
    #     # avax_balance_wei = w3.eth.get_balance(wallet_addr)
    #     # avax_balance = w3.fromWei(avax_balance_wei, 'ether')
    #     # if avax_balance > 6:
    #     #     #logging.info("Attempting to calculate buy trade...")
    #     #
    #     #     # Trade Math
    #     #     trade_start_balance = avax_balance - 3
    #     #     trade_amount_wei = w3.toWei(trade_start_balance, 'ether')
    #     #     slippage = 0.02
    #     #
    #     #     reserves_wei = dai_avax_pool_joe_contract.functions.getReserves().call()
    #     #     reserveOfToken0 = w3.fromWei(reserves_wei[0], 'ether')
    #     #     reserveOfToken1 = w3.fromWei(reserves_wei[1], 'ether')
    #     #
    #     #     currency_rate = reserveOfToken0 / reserveOfToken1
    #     #     currency_rate = float((1 / currency_rate))
    #     #     # Currency arrangement for amountOutMin
    #     #     path = [dai_avax_pool_joe_contract.functions.token0().call(),
    #     #             dai_avax_pool_joe_contract.functions.token1().call()]
    #     #     to = wallet_addr
    #     #     deadline = int(time.time() * 1000 + 1000 * 60 * 10)  # deadline is 10 minutes
    #     #     amountOutMin = int((trade_amount_wei - trade_amount_wei * slippage) * float(currency_rate))
    #     #     params = (amountOutMin, path, to, deadline)
    #     #
    #     #     #logging.info("Calculate buy trade is completed")
    #     #
    #     #     # Seperate and Create Transaction
    #     #     #logging.info("Attempting to seperate Smart Contract Buy Function and Create Transaction...")
    #     #     buy_tx = joe_router_contract.functions.swapExactAVAXForTokens(amountOutMin, path, to,
    #     #                                                                   deadline).buildTransaction({
    #     #         'gas': 1000000,
    #     #         'gasPrice': w3.eth.gas_price + w3.toWei(30, 'gwei'),
    #     #         'from': wallet_addr,
    #     #         'nonce': w3.eth.get_transaction_count(wallet_addr),
    #     #         'value': trade_amount_wei
    #     #     })
    #     #     signed_txn = w3.eth.account.signTransaction(
    #     #         buy_tx,
    #     #         private_key=private_key
    #     #     )
    #     #     #logging.info("buy Transaction is Signed")
    #     #    # logging.info("Attempting to Send buy Transaction...")
    #     #
    #     #     buy_hex_output = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    #     #   #  logging.info("buy Transaction has been sent")
    #     #
    #     #  #   logging.info("buy Transaction is waiting to be mined...")
    #     #
    #     #     tx_receipt = w3.eth.wait_for_transaction_receipt(buy_hex_output)
    #     #
    #     #
    #     #
