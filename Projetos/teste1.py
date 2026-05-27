{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPkm9AqzT7v8QNIQIiVJcdg",
      "include_colab_link": true
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
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Londrik/teste.py/blob/main/teste1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "sintaxe basica print igual a resultado\n"
      ],
      "metadata": {
        "id": "9PK9J9sDhZ3x"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "variáveis\n"
      ],
      "metadata": {
        "id": "mJ7cOlZOiilA"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "inteiro =  10\n",
        "inteiro2 = 11\n",
        "print(inteiro , inteiro2 )"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "In6s5Nrwi__J",
        "outputId": "0ca92480-aa3f-47d2-d347-7ef413dfedd1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "10 11\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "nome = \"joão\"\n",
        "sobrenome = \"silva\"\n",
        "idade = 25\n",
        "profissão = \"desenvolvedor\"\n",
        "print(f\"Olá, meu nome é {nome} {sobrenome}, tenho {idade} anos e sou {profissão}.\")\n",
        "# Saída: Olá, meu nome é joão silva, tenho 25 anos e sou desenvolvedor.\n",
        "\n",
        "produto = \"laptop\"\n",
        "marca = \"Dell\"\n",
        "preço = 4500.00\n",
        "print(f\"O {produto} da marca {marca} custa R${preço:.2f}.\")\n",
        "# Saída: O laptop da marca Dell custa R$4500.00.\n",
        "\n",
        "numero1 = 12\n",
        "numero2 = 6\n",
        "soma = 18\n",
        "subtração = 6\n",
        "multiplicação = 72\n",
        "divisão = 2.0\n",
        "print(f\"A soma de {numero1} e {numero2} é {soma}.\")\n",
        "print(f\"A subtração de {numero1} e {numero2} é {subtração}.\")\n",
        "print(f\"A multiplicação de {numero1} e {numero2} é {multiplicação}.\")\n",
        "print(f\"A divisão de {numero1} por {numero2} é {divisão}.\")\n",
        "# Saída:\n",
        "\n",
        "numero1 = 7\n",
        "numero2 = 2\n",
        "soma = 20\n",
        "subtração = 10\n",
        "multiplicação = 75\n",
        "divisão = 3.0\n",
        "potenciação = 16807\n",
        "print(f\"A soma de {numero1} e {numero2} é {soma}.\")\n",
        "print(f\"A subtração de {numero1} e {numero2} é {subtração}.\")\n",
        "print(f\"A multiplicação de {numero1} e {numero2} é {multiplicação}.\")\n",
        "print(f\"A divisão de {numero1} por {numero2} é {divisão}.\")\n",
        "print(f\"A potência de {numero1} elevado a {numero2} é {potenciação}.\")\n",
        "# Saída:\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Uq7Epeya-tNo",
        "outputId": "0b5bcd78-7d07-46a5-8e0f-3327ebefbee1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Olá, meu nome é joão silva, tenho 25 anos e sou desenvolvedor.\n",
            "O laptop da marca Dell custa R$4500.00.\n",
            "A soma de 12 e 6 é 18.\n",
            "A subtração de 12 e 6 é 6.\n",
            "A multiplicação de 12 e 6 é 72.\n",
            "A divisão de 12 por 6 é 2.0.\n",
            "A soma de 7 e 2 é 20.\n",
            "A subtração de 7 e 2 é 10.\n",
            "A multiplicação de 7 e 2 é 75.\n",
            "A divisão de 7 por 2 é 3.0.\n",
            "A potência de 7 elevado a 2 é 16807.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "materias = ['Matemática', 'História', 'Biologia']\n",
        "\n",
        "    # Tupla de notas\n",
        "notas = (8.5, 7.0, 9.2)\n",
        "\n",
        "    # Dicionário com informações do aluno\n",
        "aluno = {\n",
        "        'nome': 'Carlos',\n",
        "        'idade': 21,\n",
        "        'curso': 'Engenharia'\n",
        "    }\n",
        "\n",
        "    # Exibindo as informações\n",
        "print(f\"Matérias: {materias}\")\n",
        "print(f\"Notas: {notas}\")\n",
        "print(f\"Informações do aluno: {aluno}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "R-m8q8YqmtW_",
        "outputId": "ad717c27-4812-4084-d947-dc53f7c007f4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Matérias: ['Matemática', 'História', 'Biologia']\n",
            "Notas: (8.5, 7.0, 9.2)\n",
            "Informações do aluno: {'nome': 'Carlos', 'idade': 21, 'curso': 'Engenharia'}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Lista de acessórios\n",
        "acessorios = ['Ar-condicionado', 'Vidros elétricos', 'Freios ABS']\n",
        "\n",
        "# Tupla de especificações (potência do motor em cavalos, capacidade do tanque em litros)\n",
        "especificacoes = (150, 60)\n",
        "\n",
        "# Dicionário com informações do carro\n",
        "carro = {\n",
        "    'marca': 'Toyota',\n",
        "    'modelo': 'Corolla',\n",
        "    'ano': 2023\n",
        "}\n",
        "\n",
        "# Exibindo as informações\n",
        "print(f\"Acessórios: {acessorios}\")\n",
        "print(f\"Especificações: Potência {especificacoes[0]} cv, Tanque {especificacoes[1]}L\")\n",
        "print(f\"Informações do carro: {carro}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yCB4WTWMz5f0",
        "outputId": "fc12d864-f029-47cc-f389-8058dbbaec5d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Acessórios: ['Ar-condicionado', 'Vidros elétricos', 'Freios ABS']\n",
            "Especificações: Potência 150 cv, Tanque 60L\n",
            "Informações do carro: {'marca': 'Toyota', 'modelo': 'Corolla', 'ano': 2023}\n"
          ]
        }
      ]
    }
  ]
}