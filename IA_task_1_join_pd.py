# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 19:20:26 2024

@author: Gitansha Aggarwal
"""
import pandas as pd


def join_data_without_sort_pd(data_1, data_2, key: str):
    # data_1.sort_values(by=key, kind=sort, inplace=True)
    # data_2.sort_values(by=key, kind=sort, inplace=True)
    joined_df = pd.merge(data_1, data_2, on=key, how="left")
    joined_df.drop(columns=[key], inplace=True)
    return joined_df


from IA_task_1_read_pd import elec_data, dwelling_data, date_data, area_data


data = elec_data
data = join_data_without_sort_pd(area_data, data, "AreaID")
print(data)
data = join_data_without_sort_pd(dwelling_data, data, "dwelling_type_id")
print(data)
data = join_data_without_sort_pd(date_data, data, "DateID")
