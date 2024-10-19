{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPqxjrZJui6L8ndgCMVPRX5",
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
        "<a href=\"https://colab.research.google.com/github/usmangul23/Unit-Conversion/blob/main/Age_Calculator.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "from datetime import datetime\n",
        "\n",
        "# Function to calculate age\n",
        "def calculate_age(dob):\n",
        "    today = datetime.today()\n",
        "    age_years = today.year - dob.year\n",
        "    age_months = today.month - dob.month\n",
        "    age_days = today.day - dob.day\n",
        "\n",
        "    if age_days < 0:\n",
        "        age_months -= 1\n",
        "        age_days += 30  # Approximation for days in a month\n",
        "\n",
        "    if age_months < 0:\n",
        "        age_years -= 1\n",
        "        age_months += 12\n",
        "\n",
        "    return age_years, age_months, age_days\n",
        "\n",
        "# Streamlit app title\n",
        "st.title('Age Calculator')\n",
        "\n",
        "# Input for date of birth\n",
        "dob_input = st.text_input(\"Enter your date of birth (YYYY-MM-DD):\")\n",
        "\n",
        "# Check if input is provided\n",
        "if dob_input:\n",
        "    try:\n",
        "        # Convert input to date object\n",
        "        dob = datetime.strptime(dob_input, \"%Y-%m-%d\")\n",
        "\n",
        "        # Calculate age\n",
        "        years, months, days = calculate_age(dob)\n",
        "\n",
        "        # Display the result\n",
        "        st.success(f\"You are {years} years, {months} months, and {days} days old.\")\n",
        "    except ValueError:\n",
        "        st.error(\"Please enter a valid date in the format YYYY-MM-DD.\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7v3CZDtTeTRz",
        "outputId": "9083dd83-3586-481d-a769-91be4dad3908"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2024-10-19 06:47:36.437 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-19 06:47:36.440 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-19 06:47:36.441 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-19 06:47:36.443 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-19 06:47:36.444 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-19 06:47:36.446 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-19 06:47:36.448 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-19 06:47:36.449 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ]
    }
  ]
}