#! /usr/bin/env python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
# py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
# py.exe mcb.pyw list - Loads all keywords to clipboard.
import shelve, pyperclip, sys, os

if not os.path.exists('/Users/paternhong/Desktop/ML100/1_Automate_the_Boring_Stuff_with_Python' \
                      + '/CH8_Project_Multiclipboard'):
    os.makedirs('/Users/paternhong/Desktop/ML100/1_Automate_the_Boring_Stuff_with_Python' \
                      + '/CH8_Project_Multiclipboard')

# 創建or打開多重剪貼簿mcbShelf
mcbShelf = shelve.open('/Users/paternhong/Desktop/ML100/1_Automate_the_Boring_Stuff_with_Python' \
                      + '/CH8_Project_Multiclipboard/mcb')
# 先以list形式弄出所有key
keys_list = list(mcbShelf.keys())
'''
把OS剪貼簿內容以關鍵字的方式儲存到 mcbShelf 中，此時需判斷是否有參數：
引數1: save
引數2: 作為OS剪貼簿內容的key，儲存到 mcbShelf
'''
if len(sys.argv) == 3:
    # 儲存
    if sys.argv[1].lower() == 'save':
        if sys.argv[2].lower() == 'save' or sys.argv[2].lower() == 'list':
            print('Illegal key setup value: {}'.format(sys.argv[2]))
        else:
            # shelve用類似字典的方式儲存資訊，把'剪貼簿的內容作為值'、'引數2做為對應 key'寫入mcb
            mcbShelf[sys.argv[2]] = pyperclip.paste()
    # 刪除   
    elif sys.argv[1].lower() == 'delete':
        if sys.argv[2] not in keys_list:
            print('Key: {} is not in the Clipboard!'.format(sys.argv[1]))
        else:
            del mcbShelf[sys.argv[2]]

# 從 mcbShelf 中，讀取“關鍵字(Key)的內容”存到剪貼簿，以便使用
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(keys_list))
    elif sys.argv[1].lower() == 'save':
        print(('Illegal key: {}'.format(sys.argv[1])))
    elif sys.argv[1] == 'delete':
        for i in keys_list:
            del mcbShelf[i]
    elif sys.argv[1] not in keys_list:
        print('Key: {} is not in the Clipboard!'.format(sys.argv[1]))
    else:
        pyperclip.copy(mcbShelf[sys.argv[1]])
        
    
mcbShelf.close()