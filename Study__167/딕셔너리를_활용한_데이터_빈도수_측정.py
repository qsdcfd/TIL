{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "딕셔너리를 활용한 데이터 빈도수 측정",
      "provenance": [],
      "authorship_tag": "ABX9TyOSTCqC/myMXX0CasI73r+R"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "source": [
        "fname = input('Enter File: ')\n",
        "if len(fname) < 1 : fname = 'clown.txt'#clown.txt파일 받기\n",
        "hand = open(fname)# 파일 열기\n",
        "\n",
        "di = dict()#딕셔너리 만들기\n",
        "for lin in hand :\n",
        "    lin = lin.rstrip()#개행문자 지우기\n",
        "    wds = lin.split()# 공백 기준 나누기\n",
        "    for w in wds : #단어별 빈도수 check\n",
        "        di[w] = di.get(w,0) + 1\n",
        "\n",
        " #가장 많이 나타난 단어 찾기\n",
        "\n",
        "largest = -1 #최댓값\n",
        "theword = None # 가장 많이 나온 단어\n",
        "for k, v in di.items() :#키와 값을 뽑는 거로, 두 개의 변수 필요(item사용 시)\n",
        "    print(k,v)\n",
        "    if v > largest : #단어 수 \n",
        "        largest = v #최댓값\n",
        "        theword = k #가장 많이 나온 단어\n",
        "        \n",
        "print('Done', theword, largest)"
      ],
      "metadata": {
        "id": "J3mAC7WJkiNZ"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}