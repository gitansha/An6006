# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 10:26:35 2024

@author: Gitansha Aggarwal
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def read_file(file_name: str, sep: str) -> list:
    """

    This function returns the input data read from the text file in form of a dictionary
    eg output: [{'AreaID': '1002', 'Area': 'Sembawang', 'Region': 'North Region'}]
    ----------
    file_name : str
        The name of the text file to read teh values from.
    sep : str
       Seperator used in the file.

    Returns : List
    -------
    List with dictionaries containing the input data from text file


    """
    data = []
    with open(f"{file_name}.txt") as f:
        headers = f.readline().strip().split(sep)
        lines = [line.strip() for line in f.readlines()]

        if file_name == "Dwelling":
            headers[0] = "dwelling_type_id"

        for line in lines:
            input_data = line.strip().split(sep)
            record = {
                headers[i]: input_data[i] for i in range(len(input_data))
            }
            data.append(record)
        # print(data)
        return data


area_data = read_file("Area", ";")
date_data = read_file("DateDim", ";")
dwelling_data = read_file("Dwelling", ",")
elec_data = read_file("Electricity", ";")


# %%
