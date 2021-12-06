#!/usr/bin/env python
# coding: utf-8

# ### 하위 디렉터리 출력
# 
# 

# In[ ]:


#C:/doit/sub_dir_search.py

def search(dirname):
    print(dirname)
    
search("c:/") #search함수를 만들어서 시직 디렉토리 코드

## 디렉터리에 있는 파일 검색 가능 코드

# C:/doit/sub_dir_search.py
import os

def search(dirname):
    filenames = os.listdir(dirname) #해당 디렉터리에 있는 파일들의 리스트 구하기 가능
    for filename in filenames:
        full_filename = os.path.join(dirname, filename) #파일 이름 구할 땐 dirname이용
        print(full_filename)

search("c:/")

# 결과값
c:/$Recycle.Bin
c:/$WINDOWS.~BT
c:/$Windows.~WS
c:/adb
c:/AMD
c:/android
c:/bootmgr
c:/BOOTNXT
    

# c:| 디렉토리에 있는 파일 중 .py파일만 출력
    
# C:/doit/sub_dir_search.py
import os

def search(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        ext = os.path.splitext(full_filename)[-1] # 파일 확장자만 추출하기
        if ext == '.py': 
            print(full_filename)

search("c:/")


## 우리가 원하는 것

## 하위 디렉토리 포함한 모든 파이썬 파일 검색

# C:/doit/sub_dir_search.py
import os

def search(dirname):
    
    # tru except PermissionError: 권한 없는 디렉터리가 접근해도 오류로 종료하지 않고 수행함
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename) # 파일인지 디렉토리인지 구분
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.py': 
                    print(full_filename)
    except PermissionError:
        pass

search("c:/") # 재귀호출 하여 해당 디렉터리 하위 파일 다시 검색


# #### 위의 코드 보다 더 쉬운 방법 os.walk
# 
# - os.walk:  시작 디렉터리 ~ 하위 모든 디렉터리까지 차례대로 방문한다.

# In[ ]:


import os

for (path, dir, files) in os.walk("c:/"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.py':
            print("%s/%s" % (path, filename))

