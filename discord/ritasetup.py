#!/usr/bin/env python3

baseChan = ["public", "reapers-chat", "r4", "r3-r5"]
langDict = {"english": "english",
            "русский": "russian",
            "tiếng-việt": "vietnamese",
            "türkçe": "turkish",
            "deutsche": "german",
            "ภาษาไทย": "thai",
            "español": "spanish",
            "日本語": "japanese",
            "中文語": "chinese"}


for chan in baseChan:
    print("")
    print(f"{chan} group:")
    for key, val in langDict.items():
        print("")
        print(f"for {chan}-{key}")
        for k, v in langDict.items():
            if k != key:
                print(f"!t channel from {val} to {v} for #{chan}-{k}")
