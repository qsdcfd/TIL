{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "조건문(if,else)활용하여 급여 계산",
      "provenance": [],
      "authorship_tag": "ABX9TyMvQ11Q8NFj2+RhuKz3N2Qf"
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
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RJYb3nm4AuR0",
        "outputId": "7587d50f-00fb-4a8a-aee9-ca3d3508ff0a"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter Hours: 40\n",
            "Enter Rate: 10\n",
            "Regular pay\n",
            "Pay: 400.0\n"
          ]
        }
      ],
      "source": [
        "\n",
        "#조건문을 활용하여 급여계산하기\n",
        "#초과 수당 및 일반 급여 계산\n",
        "#문제: 근무 시간과 시급 넣기\n",
        "# 소수점으로 설정\n",
        "# 주 40시간이 넘으면 Overtime출력 후 초과수당 출력\n",
        "# 넘지 않으면 Regular pay출력 후 일반 수당 출력\n",
        "sh = input(\"Enter Hours: \")\n",
        "sr = input(\"Enter Rate: \")\n",
        "fr = float(sr)\n",
        "fh = float(sh)\n",
        "#print(fh, fr)\n",
        "\n",
        "if fh > 40:\n",
        "    print(\"Overtime\")\n",
        "    reg = fr * fh #일반 수당\n",
        "    otp = (fh-40.0) * (fr * 0.5) #초과수당\n",
        "    print(reg,otp)\n",
        "    xp = reg + otp\n",
        "else:\n",
        "    print(\"Regular pay\")\n",
        "    xp = fh * fr\n",
        "\n",
        "\n",
        "print(\"Pay:\", xp)\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "eUcOGmS-DfKg"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}