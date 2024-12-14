# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 16:02:13 2024

@author: Gitansha Aggarwal
"""
import pandas as pd


def join_data_pd(data_1, data_2, key: str, sort="mergesort"):
    data_1.sort_values(by=key, kind=sort, inplace=True)
    data_2.sort_values(by=key, kind=sort, inplace=True)
    joined_df = pd.merge(data_1, data_2, on=key, how="left")
    joined_df.drop(columns=[key], inplace=True)
    return joined_df


# def join_data_pd(data_1, data_2, key: str, sort_kind="stable", sort=True):
#     """
#     Joins two DataFrames on a specified key with optional sorting.

#     Parameters:
#     - data_1 (pd.DataFrame): First DataFrame.
#     - data_2 (pd.DataFrame): Second DataFrame.
#     - key (str): The key column to join on.
#     - sort_kind (str): The sorting algorithm to use ('heapsort', 'mergesort', 'quicksort', 'stable').
#     - sort (bool): Whether to sort the DataFrames before joining.

#     Returns:
#     - pd.DataFrame: The resulting joined DataFrame.
#     """
#     if sort:
#         if sort_kind not in ["heapsort", "mergesort", "quicksort", "stable"]:
#             raise ValueError(f"Unknown sort method: {sort_kind}")
#         data_1 = data_1.sort_values(by=key, kind=sort_kind)
#         data_2 = data_2.sort_values(by=key, kind=sort_kind)

#     joined_df = pd.merge(data_1, data_2, on=key, how="left")

#     # Optionally drop the key column if it's no longer needed
#     # joined_df.drop(columns=[key], inplace=True)

#     return joined_df


from IA_task_1_read_pd import elec_data, dwelling_data, date_data, area_data


data = elec_data
data = join_data_pd(area_data, data, "AreaID")
print(data)
data = join_data_pd(dwelling_data, data, "dwelling_type_id")
print(data)
data = join_data_pd(date_data, data, "DateID")
