#!/usr/bin/python3
import sys
sys.path.insert(0,"/var/www/tammy/")
sys.path.insert(0,"/var/www/tammy/tammy/")

import logging
logging.basicConfig(stream=sys.stderr)

from jackietest import app as application
