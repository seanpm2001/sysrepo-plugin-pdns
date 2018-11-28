#!/usr/bin/env python3
__author__ = "Pieter Lexis <pieter.lexis@powerdns.com"
__copyright__ = "Copyright 2018, PowerDNS.COM BV"
__license__ = "Apache 2.0"

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sysrepo as sr
import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger()


def change_cb(session, modname, event, ctx):
    log.debug("change_cb called with:")
    log.debug("  session: %s", session)
    log.debug("  modname: %s", modname)
    log.debug("  event: %s", event)
    log.debug("  ctx: %s", ctx)

    return sr.SR_ERR_OK


def main():
    module_name = 'dns-server-amended-with-zone'
    log.debug("connecting to sysrepo")
    # connect to sysrepo
    conn = sr.Connection("pdns")
    log.info("connected to sysrepo")

    log.debug("starting session")
    # start session
    session = sr.Session(conn)
    log.info("session started")
    sub = sr.Subscribe(session)
    sub.module_change_subscribe(module_name, change_cb, None, sr.SR_SUBSCR_DEFAULT | sr.SR_SUBSCR_APPLY_ONLY)
    sr.global_loop()


if __name__ == "__main__":
    main()
