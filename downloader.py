'''

import requests
import json
import time

if __name__ == '__main__':
    db = {}
    while True:
        r = requests.get('https://opentdb.com/api.php?amount=50')
        results = r.json()['results']
        for result in results:
            db[result['question']] = result
        len_db = len(list(db.values()))
        if len_db >= 4122:
            break
        time.sleep(.5)
        print(len_db)
    with open('db.json', 'w') as f:
        json.dump(list(db.values()), f)

'''



import requests
import json
import time

if __name__ == '__main__':
    db = {}
    target_count = 4122

    while len(db) < target_count:
        r = requests.get('https://opentdb.com/api.php?amount=50')
        results = r.json()['results']
        
        for result in results:
            db[result['question']] = result

        len_db = len(db)
        print(len_db)
        
        time.sleep(0.5)

    with open('db.json', 'w') as f:
        json.dump(list(db.values()), f)

