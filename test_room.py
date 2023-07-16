from substrateinterface import SubstrateInterface

ws_provider = SubstrateInterface(url="wss://rpc-parachain.bajun.network")

constant_list = ws_provider.get_metadata_constants(block_hash=None)

print(constant_list)