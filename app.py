#!/usr/bin/env python3

import datetime

def go_magic():
    now = datetime.datetime.now()
    return "Hello! {0}".format(now)

if __name__ == "__main__":
    print(go_magic())
