# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 16:02:38 2024

@author: Gitansha Aggarwal
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def read_file_pd(file_name: str, sep: str):
    """
    This function returns the input data read from the text file in form of a pandas dataframe

       Parameters
       ----------
       file_name : str
           The name of the text file to read teh values from.
       sep : str
          Seperator used in the file

       Returns : pandas Dataframe
       -------
       Dataframe with values

    """
    df = pd.read_csv(f"{file_name}.txt", sep=sep)
    if file_name == "Dwelling":
        df = df.rename(columns={"TypeID": "dwelling_type_id"})
    # print(df)
    return df


area_data = read_file_pd("Area", ";")
date_data = read_file_pd("DateDim", ";")
dwelling_data = read_file_pd("Dwelling", ",")
elec_data = read_file_pd("Electricity", ";")
