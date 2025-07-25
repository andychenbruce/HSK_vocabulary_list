#!/usr/bin/env python3

import requests
import json

def fetch_hsk_words(level: int) -> list[str]:
    level_ids=[level]
    endpoint = "https://api.hskmock.com/mock/word/searchWords"
    headers = {
        "Content-Type": "application/json",
    }
    
    page_num = 1
    all_data = []
    
    payload = {
        "level_ids": level_ids,
        "initial": "",
        "keyword": "",
        "page_num": page_num,
        "page_size": 1000000
    }
        
    # Send POST request
    response = requests.post(
        endpoint,
        headers=headers,
        data=json.dumps(payload)
    )
    response.raise_for_status()  # Raise HTTP errors
    
    data = response.json()

    assert data["errcode"] == 0

    words = [x["word"] for x in data["data"]["list"]]

    page_num += 1
    
    return words

if __name__ == "__main__":
    words_per_level = []

    for i in range(1, 7):
        hsk_words = fetch_hsk_words(i)
        print(f"got {len(hsk_words)} words in HSK{i}")
        words_per_level.append(hsk_words)
    
    with open("hsk_words.json", "w", encoding="utf-8") as f:
        json.dump(words_per_level, f, ensure_ascii=False, indent=2)
    print("dumped to hsk_words.json")
