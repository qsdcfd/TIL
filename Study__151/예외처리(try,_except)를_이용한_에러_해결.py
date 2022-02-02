{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "예외처리(try, except)를 이용한 에러 해결",
      "provenance": [],
      "authorship_tag": "ABX9TyMg4/vYltL9FAXWiNXXxqSf"
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
        "#예외처리 해보기\n",
        "#숫자가 아닌 문자가 입력되었을 때 숫자 입력하도록 유도하기\n",
        "sh = input(\"Enter Hours: \")\n",
        "sr = input(\"Enter Rate: \")\n",
        "try:\n",
        "    fh = float(sh)\n",
        "    fr = float(sr)\n",
        "except:\n",
        "    print(\"Error, please enter numeric input\")\n",
        "    quit()\n",
        "#print(fh, fr)\n",
        "if fh > 40 :\n",
        "\t#print(\"Overtime\")\n",
        "\treg = fr * fh\n",
        "\totp = (fh - 40.0) * (fr * 0.5)\n",
        "\t#print(reg, otp)\n",
        "\txp = reg + otp\n",
        "else:\n",
        "\t#print(\"regular\")\n",
        "\txp = fh * fr\n",
        "print(\"Pay:\", xp)"
      ],
      "metadata": {
        "id": "8LapFfd4Lo6U"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}