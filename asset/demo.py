from __future__ import print_function

import argparse
import os
from configparser import ConfigParser

import qrcode
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException


def get_rpc_connection(user, password, ip, port):
    conn_str = "http://%s:%s@%s:%s"%(user, password, ip, port)
    try:
        return AuthServiceProxy(conn_str)
    except Exception as general_exception:
        print("An Exception occured: " + str(general_exception))

def call_rpc(rpc_conn, rpc_method, *args):
    try:
        return getattr(rpc_conn, rpc_method)(*args)
    except JSONRPCException as json_exception:
        print("A JSON RPC Exception occured: " + str(json_exception))
        assert False
    except Exception as general_exception:
        print("An Exception occured: " + str(general_exception))
        assert False



def do_issuance(cfg, rpc_conn):
    amount = cfg.get('ASSET_ISSUANCE', 'amount')
    re_amount = cfg.get('ASSET_ISSUANCE', 'reissuance_amount')
    issuance = call_rpc(rpc_conn, 'issueasset', amount, re_amount, False)
    issuance['block'] = call_rpc(rpc_conn, 'generate', 1)[0]
    print("Issued {0} tokens, {1} reissuance tokens of asset {2}".format(amount, re_amount, issuance['asset']))
    return issuance

def do_transfers(cfg, rpc_conn, asset):
    n = int(cfg.get('TRANSFER', 'n'))
    amount = int(cfg.get('TRANSFER', 'amount'))
    print("Transferring {0} units of asset {1} to {2} recipients each".format(amount, asset, n))

    addresses = []
    for i in range(n):
        address = call_rpc(rpc_conn, 'getnewaddress')
        address_info = call_rpc(rpc_conn, 'validateaddress', address)
        privkey = call_rpc(rpc_conn, 'dumpprivkey', address)
        addresses.append((address_info, privkey))

    transfer_amounts = {addr[0]['unconfidential']: 1.0 for addr in addresses}
    asset_tags = {addr[0]['unconfidential']: asset for addr in addresses}
    txid = call_rpc(rpc_conn, 'sendmany', "", transfer_amounts, 1, "", [], asset_tags)
    return addresses, txid

def generate_qr_codes(privkeys, prefix=''):
    print("Generating {0} QR Codes".format(len(privkeys)))
    for idx, priv_key in enumerate(privkeys):
        img = qrcode.make(priv_key)
        img.save(prefix+'{0:05}.png'.format(idx))

if __name__=='__main__':
    cfg = ConfigParser()
    cfg.read_file(open('demo.config'))
    rpc_conn = get_rpc_connection(cfg.get('RPC', 'rpc_user'), cfg.get('RPC', 'rpc_password'), cfg.get('RPC', 'rpc_ip'), cfg.get('RPC', 'rpc_port'))

    issuance = do_issuance(cfg, rpc_conn)
    addresses, txid = do_transfers(cfg, rpc_conn, issuance['asset'])
    generate_qr_codes([addr[1] for addr in addresses], 'my_asset_')
