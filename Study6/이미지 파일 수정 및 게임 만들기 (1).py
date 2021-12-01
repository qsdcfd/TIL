#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('  mkdir -p ~/aiffel/data_represent/image')
get_ipython().system('  ln -s ~/data/newyork.jpg ~/aiffel/data_represent/image')


# In[4]:


from PIL import Image, ImageColor
import os
img_path = os.getenv("HOME") + "/aiffel/data_represent/image/newyork.jpg"
img = Image.open(img_path)
print(img_path)
print(type(img))
img


# In[5]:


img.size


# In[6]:


W, H = img.size
print((W, H))


# In[7]:


print(img.format)
print(img.size)
print(img.mode)


# In[8]:


img.crop((30,30,100,100))


# In[9]:


# 새로운 이미지 파일명
cropped_img_path = os.getenv("HOME") + "/aiffel/data_represent/image/cropped_img.jpg"
img.crop((30,30,100,100)).save(cropped_img_path)
print("저장 완료!")


# In[10]:


get_ipython().system('ls ~/aiffel/data_represent/image/cropped_img.jpg')


# In[11]:


get_ipython().system('ls ~/aiffel/data_represent/image/cropped_img.jpg')


# In[12]:


img_arr


# https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes

# In[13]:


img_g = Image.open(img_path).convert('L')
img_g


# In[14]:


img_g_arr = np.array(img_g)
print(type(img_g_arr))
print(img_g_arr.shape)
print(img_g_arr.ndim)


# In[15]:


red = ImageColor.getcolor('RED','RGB')
reda = ImageColor.getcolor('red','RGBA')
yellow = ImageColor.getcolor('yellow','RGB')
print(red)
print(reda)
print(yellow)


# In[18]:


# 파이썬 dict 로 표현한 전화번호부입니다. 
Country_PhoneNumber = {'Korea': 82, 'America': 1, 'Swiss': 41, 'Italy': 39, 'Japan': 81, 'China': 86, 'Rusia': 7}
Country_PhoneNumber['Korea']  # 키를 가지고 값을 조회할 수 있습니다.


# In[22]:


treasure_box = {'rope':2, 
                'apple':10, 
                'torch': 6, 
                'gold coin': 50, 
                'knife': 1, 
                'arrow': 30}

def display_stuff(treasure_box):
    print("Congraturation!! you got a treasure box")
    for k, v in treasure_box.items():
        print("you have {} {}pcs".format(k, v))
display_stuff(treasure_box)

coin_per_treasure = {'rope':1,
        'apple':2,
        'torch': 2,
        'gold coin': 5, 
        'knife': 30,
        'arrow': 1}

def total_silver(treasure_box, coin_per_treasure):
    total_coin = 0
    for treasure in treasure_box:
        coin = coin_per_treasure[treasure] * treasure_box[treasure]
        print("{} : {}coins/pcs * {}pcs = {} coins".format(
          treasure, coin_per_treasure[treasure], treasure_box[treasure], coin))
        total_coin += coin
    print('total_coin : ', total_coin)
total_silver(treasure_box, coin_per_treasure)
treasure_box = {'rope': {'coin': 1, 'pcs': 2},
                'apple': {'coin': 2, 'pcs': 10},
                'torch': {'coin': 2, 'pcs': 6},
                'gold coin': {'coin': 5, 'pcs': 50},
                'knife': {'coin': 30, 'pcs': 1},
               	'arrow': {'coin': 1, 'pcs': 30}
               }
treasure_box['rope']


# In[23]:


def display_stuff(treasure_box):
    ## type your code
    print("Congraturation!! you got a treasure box!!")
    for treasure in treasure_box:
             print("You have {} {}pcs".format(treasure, treasure_box[treasure]['pcs']))
display_stuff(treasure_box)

def total_silver(treasure_box, coin_per_treasure):
    ## type your code
    total_coin = 0
    for treasure in treasure_box:
        coin = coin_per_treasure[treasure] * treasure_box[treasure]['pcs']
        print("{} : {}coins/pcs * {}pcs = {} coins".format(
          treasure, coin_per_treasure[treasure], treasure_box[treasure]['pcs'], coin))
        total_coin += coin
    print('total_coin : ', total_coin)
total_silver(treasure_box, coin_per_treasure)


# In[ ]:




