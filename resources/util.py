import os
import json

msg_files = list(filter(lambda x: x.endswith('.json'), os.listdir('.')))

for f in msg_files:
    msg = json.load(open(f, 'r', encoding='utf-8'))
    utf8f = f.split('.')[0]+'_utf.json'
    print('build utf8 file name[{}]'.format(utf8f))
    print("checking the encoding for message[{}]".format(msg))
    #json.dumps(msg, open(utf8f, 'w'), ensure_ascii=True)