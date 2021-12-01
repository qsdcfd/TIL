#!/usr/bin/env python
# coding: utf-8

# [텍스트 데이터를 문자열로 저장한다는 것]
# 
# 인코딩과 디코딩
# 문자열 다루기
# 정규 표현식
# 
# [파일과 디렉토리]
# 
# 파일
# 디렉토리
# 모듈과 패키지
# 
# [여러가지 파일 포맷 다루기]
# 
# CSV 파일
# XML파일
# JSON 파일
# 
# <텍스트 데이터를 문자열로 저장한다는 것>
# 바이트(byte): 컴퓨터의 기본 저장 단위
# 유니코드: 이 모든 것을 실현하게 해준 최상위 문자
# 인코딩: 문자열-->바이트(사람 언어--> 컴퓨터 언어)
# 디코딩: 바이트-->문자열(컴퓨터 언어--> 사람언어)
# 변수명= b'문자열' -->bytes출력
# 
# ord():해당 문자에 대응하는 유니숫자 반환.
# chr():해당 유니코드 숫자에 대응하는 문자 반환
# 
# * 문자열 다루기 *
# i)이스케이프 문자
# \' :홑따옴표' 출력
# \" :겹따옴표" 출력
# \t :탭
# \n :줄바꿈
# \\:백슬래시\ 출력
# \r:개행복귀
# ii)원시문자열(raw string)
# -->이스케이프 문자가 적용되지  않게 함.
# -->사용법: 문자열을 시작하는 따옴표 앞에 r을 붙이기
# 
# startswith('문자열'): 이 문자열로 시작하는 값 찾기
# endswith('문자열'):이 문자열로 끝나는 값 찾기
# trimming(): 띄어쓰기로 표기되는 공백문자 만드는 함수.
# strip(): 공백문자 제거 함수
# upper():모든 문자 대문자
# lower():모든 문자 소문자
# capitalize():첫 글자만 대문자로 변환
# isupper():문자열이 모두 대문자면 True ㅇ니면 False
# islower():문자열이 모두 소문자면 True 아니면 False
# istitle():문자열의 첫 글자만 대문자면 True아니면False
# isalpha():문자열이 모두 알파벳 문자면 True아니면False
# isalnum():문자열이 모두 알파벳 문자와 숫자로만 되어있다면 True 아니면 False
# isdecimal():문자열이 모두 숫자로 되어있으면 True 아니면 False
# join():반복 가능한 객체를 받는 메소드로 각각 원소를 모아 하나의 문자열로 합쳐줌,문자열 반환/
# split():구분자를 기준으로 하나의 문자열을 나누어 주고 기본값은 쉼표(,), 리스트 반환/
# replace():replace(s1,s2)형태로 문자열 내 문자열 s1->s2
# 
# iv)불변(immutable)의 문자열
# * 가변객체(mutable object)
#   -객체를 생성한 후 값 수정
#   -변수는 값이 수정된  객체
#   - 수정된 값 = 원래 값
#   ex)list, set, dict
# 
# * 불변객체(immutable object)
#   -객체를 생성한 후 객체의 값 수정X
#   - 변수는 해당 값을 가진 다른 객체를 가리킨다.
#   - 수정된 값 != 원래  값 
#    EX) int, float, complex, bool, string, tuple,
#      frozen set
# * 객체비교
#   -id(object): 객체를 위한 고유한 상수 리턴
#   -is
#   * 변수 is 변수
#   * 변수 is 객체
#   * 객체 is 객체
#  https://webnautes.tistory.com/1181
# https://ledgku.tistory.com/54
# 
# * 정규 표현식(crtl+F, 검색 기능 지원)
# - import re
# - Complile()
#   1) 찾고자 하는 문자열의 패턴 정의
#   2)re.compile()-->해당 객체 반복 사용 가능.
# - Method(메소드)
#   1)  정의된 패턴과 매칭되는 경우를 찾아 다양한 처리,
#   -search(): 일치하는 패턴 찾기
#   -match(): 패턴이 검색 대상에 처음부터 일치.
#   -findall():일치하는 모든 패턴 찾기
#   -split():패턴 나누기
#   -sub(): 일치하는 패턴으로 대체하기
#   -group(): 실제 결과에 해당하는 문자열을 반환.
# - 구현순서
#     1)import re 를 통해 정규식 모듈을 가져옵니다.
#     2)re.compile() 함수로 Regex 객체를 만듭니다.
#     3)검색할 문자열을 Regex 객체의 search() , findall() 메소드로 전달합니다.
# 
# 
# * 패턴: 특수문자, 메타문자
# [ ] : 문자
# - : 범위
# . : 하나의 문자
# ? : 0회 또는 1회 반복
# * : 0회 이상 반복
# + : 1회 이상 반복
# {m, n} : m ~ n
# \d : 숫자
# \D : 비숫자
# \w : 알파벳 문자
# \W : 비알파벳 문자
# \s : 공백 문자
# \S : 비공백 문자
# \b : 단어 경계
# \B : 비 단어 경계
# 훑어만 보아도 이 많은 것들
# 
# * 파일*
# 
# write: 파일을 열고 객체를 만들어주는 함수
# read:파일 읽기
# 
# -메소드
# f.read() : 파일을 읽는다.
# f.readline() : 파일을 한 줄씩 읽는다.
# f.readlines() : 파일 안의 모든 줄을 읽어 그 값을 리스트로 반환한다.
# f.write(str) : 파일에 쓴다. 문자열 타입을 인자로 받는다.
# f.writelines(str) : 파일에 인자를 한 줄씩 쓴다.
# f.close() : 파일을 닫는다.
# f.seek(offset) : 새 파일의 위치를 찾는다
# 
# * 디렉토리(파일이 저장되는 위치)
#  -표준: sys, os, glob
#  -개념
#  모듈(module) : 파이썬으로 만든 코드가 들어간 파일 .py
# 
# 패키지(package) : __init__.py가 포함된 폴더로 흔히 라이브러리라고 칭함
# 
# PIP(Package Installer for Python) : 패키지 관리자로 파이썬을 설치하면 기본으로 설치됨
# 
# PyPA(Python Packaging Authority) : 파이선 패키지를 관리하고 유지하는 그룹
# 
# PyPI(The Python Package Index) : 파이썬 패키지들의 저장소
# 
# -함수
# sys.path : 현재 폴더와 파이썬 모듈들이 저장되어 있는 위치를 리스트 형태로 반환
# 
# sys.path.append() : 자신이 만든 모듈의 경로를 append 함수를 이용해서 추가함으로써 추가한 디렉토리에 있는 파이썬 모듈을 불러와 사용할 수 있다.
# os.chdir() : 디렉토리 위치 변경
# os.getcwd() : 현재 자신의 디렉터리 위치를 반환
# os.mkdir() : 디렉토리 생성
# os.rmdir() : 디렉토리 삭제 (단, 디렉토리가 비어 있을 경우)
# glob.glob() : 해당 경로 안의 디렉토리나 파일들을 리스트 형태로 반환
# os.path.join() : 경로(path)를 병합하여 새 경로 생성
# os.listdir() : 디렉토리 안의 파일 및 서브 디렉토리 리스트
# os.path.exists() : 파일 혹은 디렉토리의 경로 존재 여부 확인
# os.path.isfile() : 파일 경로의 존재 여부 확인
# os.path.isdir() : 디렉토리 경로의 존재 여부 확인
# os.path.getsize() : 파일의 크기 확인
# 
#  * 리눅스 기본 명령어
#  
# https://itholic.github.io/linux-basic-command/
# 
# * CSV
# csv 파일은 주피터 실행 경로에 저장되어 있을 것입니다. 파일을 검색 해 열어 보시면 각각의 데이터가 쉼표(,)로 구분돼 있는 것을 확인하실 수 있을 거예요.
# 
# * CSV파일과 Pandas
#  판다스(pandas)의 DataFrame은 to_csv 메소드를 지원합니다. 이 메소드를 이용하면 csv 파일로 쉽게 저장할 수 있어요. 데이터를 준비한 뒤 판다스를 활용해 csv 파일로 저장해 보겠습니다.
# 
# * CSV파일과 DataFrame
#  csv file ---------------> DataFrame
#           (pd.read_csv())
#           <---------------
#           (df.to_csv())
# 
# * XML
# 
# <>로 구분된 언어
# API정보를 요청하고 저장할 때 이용
# XML은 다목적 마크업 언어(Extensible Markup Language)이다.
# 마크업 언어는 태그(tag)로 이루어진 언어를 말하며, 상위(부모)태그 - 하위(자식)태그의 계층적 구조를 가지고 있다.
# XML은 요소(element)들로 이루어져 있다.
# 요소는 <열린태그> 내용 </닫힌태그>가 기본적인 구조이며, 속성(attribute)값을 가질 수도 있다.
# 
# * XML파일 만들기
# ElementTree
# 파이썬 표준 라이브러리인 ElementTree는 XML 관련 기능을 다음과 같이 제공합니다.
# 
# Element() : 태그 생성
# SubElement() : 자식 태그 생성
# tag : 태그 이름
# text : 텍스트 내용 생성
# attrib : 속성 생성
# dump()
# 생성된 XML 요소 구조를 시스템(sys.stdout)에 사용합니다.
# 
# write() : XML 파일로 저장
# 리스트(list)와 유사한 메소드를 제공
# append, insert, remove, pop
# 
# * XML 파싱.
# 0) 추출하고자 하는 데이터가 문자열 안에 포함되어 있을 경우 편리하게 추출하는 방법입니다
# 1) ElementTree(아래 예시)
# 2) BeautifulSoup
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#parsing-xml
# 
# * JSON
# JSON은 JavaScript Object Notation의 약자로, 웹 언어인 JavaScript의 데이터 객체 표현 방식으로 웹 브라우저와 다른 애플리케이션 사이에서 HTTP 요청으로 데이터를 보낼 때 널리 사용하는 표준 파일 포맷중 하나로, XML과 더불어 웹 API나 config 데이터를 전송할 때 많이 쓰입니다
#  CSV 파일에 보다 더 유연하게 데이터를 표현할 수 있고 XML 파일보다 파일을 쉽게 읽고 쓸 수 있다는 장점이 있습니다. 
# javascript기반 이용 가능.
# 웹에서 JavaScript나 JavaScript 기반의 Framework가 많이 사용되고 있는 점을 미루어 봤을 때 이는 큰 강점이 될 수 있습니다.
# 
# -json 파싱
# 
# i)파일 저장
# ii)파일 읽기

# In[ ]:


1)
import xml.etree.ElementTree as ET

person = ET.Element("Person")
name = ET.Element("name")
name.text = "이펠"
person.append(name)

age = ET.Element("age")
age.text = "28"
person.append(age)

ET.SubElement(person, 'place').text = '강남'

ET.dump(person)


# In[ ]:


속성값은 attrib 란 메소드를, name 태그명은 tag 메소드를 이용해 변경할 수 있습니다.


person.attrib["id"] = "0x0001"

name.tag = "firstname"

ET.dump(person)


# In[ ]:


이번에는 새롭게 lastname이라는 태그를 firstname 
태그 다음으로 삽입하고 속성에 date를 넣어 보겠습니다.

lastname = ET.Element('lastname', date='2020-03-20')
lastname.text = '아'
person.insert(1,lastname)
ET.dump(person)

lastname = ET.Element('lastname', date='2020-03-20')2
lastname.text = '아'

person.insert(1,lastname)

ET.dump(person)


# In[ ]:


속성은 태그를 생성하는 함수인 Element 의 인자로 
넣어 주어도 됩니다. firstname 태그의 다음이니까
인덱스 번호는 1번이 되겠네요. insert 를 이용해
인덱스 번호와 태그 이름을 삽입했습니다.
get_ipython().set_next_input('리스트의 insert 와 형태가 동일하지요');get_ipython().run_line_magic('pinfo', '동일하지요')

<Person id="0x0001">
<firstname>이펠</firstname>
<lastname date='2020-03-20'>아</lastname>
<age>28</age>
<place>강남</place>
</Person>
삭제는 remove 혹은 pop 을 이용하면 됩니다.
age 태그를 지우고 싶다면 다음과 같이 하면 되겠습니다.


person.remove(age)
실행 완료
자, 이제 마지막으로 XML 파일로 저장을 해 보겠습니다.


# In[ ]:


ET.ElementTree(person).write('person.xml')


# In[1]:


2)
books.xml 파일의 "title" 태그의 내용만 가져오기

from bs4 import BeautifulSoup
with open("/aiffel/aiffel/ftext/data/books.xml", "r", encoding='utf8') as f:
    booksxml = f.read() 
    #- 파일을 문자열로 읽기
 
soup = BeautifulSoup(booksxml,'lxml') 
#- BeautifulSoup 객체 생성 : lxml parser를 이용해 데이터 분석

for title in soup.find_all('title'): 
#-  태그를 찾는 find_all 함수 이용
    print(title.get_text())
    


# In[ ]:


i)

import json

person = {
      "first name" : "Yuna",
      "last name" : "Jung",
      "age" : 33,
      "nationality" : "South Korea",
      "education" : [{"degree":"B.S degree", "university":"Daehan university", "major": "mechanical engineering", "graduated year":2010}]
       } 

with open("person.json", "w") as f:
    json.dump(person , f)


# In[ ]:


ii)

import json

with open("person.json", "r", encoding="utf-8") as f:
    contents = json.load(f)
    print(contents["first name"])
    print(contents["education"])


# In[ ]:




