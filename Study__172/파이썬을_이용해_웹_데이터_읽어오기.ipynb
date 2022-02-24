{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "파이썬을 이용해 웹 데이터 읽어오기",
      "provenance": [],
      "authorship_tag": "ABX9TyMR80eGPEy25UZMflJSzFh+"
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
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LBH0Ko_TDylq",
        "outputId": "995e0da5-ecbf-428f-b65b-104b5e4a5482"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "HTTP/1.1 200 OK\r\n",
            "Date: Thu, 24 Feb 2022 14:08:11 GMT\r\n",
            "Server: Apache/2.4.18 (Ubuntu)\r\n",
            "Last-Modified: Sat, 13 May 2017 11:22:22 GMT\r\n",
            "ETag: \"a7-54f6609245537\"\r\n",
            "Accept-Ranges: bytes\r\n",
            "Content-Length: 167\r\n",
            "Cache-Control: max-age=0, no-cache, no-store, must-revalidate\r\n",
            "Pragma: no-cache\r\n",
            "Expires: Wed, 11 Jan 1984 05:00:00 GMT\r\n",
            "Connection: close\r\n",
            "Content-Type: text/plain\r\n",
            "\r\n",
            "But soft what light through yonder window breaks\n",
            "It is the east and Juliet is the sun\n",
            "Arise fair sun and kill the envious moon\n",
            "Who is already sick and pale with grief\n"
          ]
        }
      ],
      "source": [
        "import socket\n",
        "\n",
        "mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n",
        "mysock.connect(('data.pr4e.org', 80)) #80포트 연결\n",
        "cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\\r\\n\\r\\n'.encode() 웹 서버 연결\n",
        "mysock.send(cmd)\n",
        "\n",
        "while True:\n",
        "    data = mysock.recv(512)\n",
        "    if (len(data) < 1):\n",
        "        break\n",
        "    print(data.decode(),end='') #외부에서 데이터를 가져오기에 복호화(encode)필수\n",
        "mysock.close()\n",
        "\n",
        "#빈칸은 헤더가 끝나고 시작된다는 의미/ 메타 데이터와 데이터 구분"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "LkA4DOp3EpNQ"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}