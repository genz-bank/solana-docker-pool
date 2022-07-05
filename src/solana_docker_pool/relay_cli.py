import logging
import os
import codecs
from builtins import IOError, FileNotFoundError
import time

_logger = logging.getLogger(__name__)


def handle_relay(args):
    _logger.info("Start handling relay command")
    
    print('relay handler')

def parse_args(subparsers):
    parser = subparsers.add_parser(
        'relay',
        help='Manages a relay node'
    )
    relay_parser = parser.add_subparsers(
        title="Manages relay node",
        description="A relay node sync DB with the network. This command help you to manage a node."
    )
    parser.set_defaults(func=handle_relay)
    
    #----------------------------------------------------------
    # init
    #----------------------------------------------------------
    subparsers_init = relay_parser.add_parser(
        'init',
        help='Initialize the relay node'
    )
    #subparsers_init.set_defaults(func=handle_relay_init)
    subparsers_init.add_argument(
        '--network',
        help='The name of the network (main, or test)',
        nargs=1,
        default='main',
        type=str,
        choices=['main', 'test'],
        required=False,
        dest='network'
    )
    subparsers_init.add_argument(
        '--name',
        help='target wallet name',
        dest='name',
        default='main'
    )
    

