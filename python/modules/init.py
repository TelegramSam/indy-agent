""" Handle agent initialization.
"""

# pylint: disable=import-error

import json
from aiohttp import web
from indy import wallet
import modules.ui as ui

async def initialize_agent(msg, agent):
    """ Initialize agent.
    """
    data = msg.data
    agent.owner = data['name']
    passphrase = data['passphrase']

    wallet_name = '%s-wallet' % agent.owner

    # pylint: disable=bare-except
    # TODO: better handle potential exceptions.
    try:
        await wallet.create_wallet('pool1', wallet_name, None, None, json.dumps({"key": passphrase}))
    except Exception as e:
        print(e)

    try:
        agent.wallet_handle = await wallet.open_wallet(wallet_name, None, json.dumps({"key": passphrase}))
    except Exception as e:
        print(e)
        print("Could not open wallet!")

    agent.initialized = True
    return await ui.ui_connect(None, agent)
