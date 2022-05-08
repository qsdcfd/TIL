{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "__iter__.py",
      "provenance": [],
      "authorship_tag": "ABX9TyPUcym5pv2esorMIaXYdCh4"
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
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "T0XU5XNNlQFd",
        "outputId": "771f520b-9eb0-4bd5-d8c4-4788810aa78e"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']\n"
          ]
        }
      ],
      "source": [
        "li = [1,2,3]\n",
        "print(dir(li))\n",
        "#__iter__: 함수가 있는지 확인: 반복 가능한 객체인지 확인 하는 것이다."
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#__iter__함수는 이터레이터 객체이기에\n",
        "#__next__함수가 존재합니다.\n",
        "\n",
        "li = [1, 2, 3]\n",
        "iter_li = li.__iter__()\n",
        "print(dir(iter_li))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WKcwSbXq1RPy",
        "outputId": "5ce85f8a-2e7f-4bcb-9807-ce76c35a0ec7"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__length_hint__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#리스트의 이터레이터를 변수에 저장한 후 __next__ 메소드 사용하여 호출\n",
        "li = [1,2,3,4]\n",
        "iter_li = li.__iter__()\n",
        "\n",
        "print(iter_li) #<list_iterator object at 0x7f4b04086210>\n",
        "print(iter_li.__next__()) #1\n",
        "print(iter_li.__next__()) #2\n",
        "print(iter_li.__next__()) #3\n",
        "print(iter_li.__next__()) # StopIteration "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pEjqivgu48L6",
        "outputId": "067a0637-567d-434e-8735-fd466f0980e8"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<list_iterator object at 0x7f4b040d26d0>\n",
            "1\n",
            "2\n",
            "3\n",
            "4\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "'Hello, world!'.__iter__() #__next__ 호출 시 H,e,~,!\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "chwbDF8o70j0",
        "outputId": "a5d74227-a75e-4df5-c748-7a0bbe023b07"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<str_iterator at 0x7f4b04086650>"
            ]
          },
          "metadata": {},
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "{'a' : 1, 'b': 2}.__iter__() #__next__ 호출 시 'a','b'"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_ACiHuBZ70oe",
        "outputId": "e0523e60-c1ad-47e9-e4ed-81bb85c843f3"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<dict_keyiterator at 0x7f4b04085ef0>"
            ]
          },
          "metadata": {},
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "{1,2,3}.__iter__() #__next__호출 시 1,2,3"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "F64CyUgPCtgH",
        "outputId": "3c1709f6-1cd8-4de0-a87a-e59293710de5"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<set_iterator at 0x7f4b0402d960>"
            ]
          },
          "metadata": {},
          "execution_count": 14
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "## 요소가 눈에 보이지 않아도 이터레이터를 얻은 후 next메서드 호출 시\n",
        "# 값이 나올 것입니다.\n",
        "it = range(3).__iter__() \n",
        "it.__next__() #1\n",
        "it.__next__() #2\n",
        "it.__next__() #3\n",
        "it.__next__() #Stopiteration"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 209
        },
        "id": "XdauvxUXCu_w",
        "outputId": "abb91ff0-fb76-4b51-ed6a-ff63f4aff3e7"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "error",
          "ename": "StopIteration",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mStopIteration\u001b[0m                             Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-16-d4f07a09e4ee>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0mit\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__next__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;31m#2\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      6\u001b[0m \u001b[0mit\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__next__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;31m#3\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 7\u001b[0;31m \u001b[0mit\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__next__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;31m#Stopiteration\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mStopIteration\u001b[0m: "
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "pTLpPtxND9n4"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}