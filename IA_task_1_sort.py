# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 13:45:17 2024

@author: Gitansha Aggarwal
"""


def join_data(data_1: list, data_2: list, key: str) -> list:
    """
    This functions performs the left join on the basis of th specified key. It also removes the key from the data on which the join was performed.

        Parameters
        ----------
        data_1 : list
            List containing the data. It should be the right list
        data_2 : list
            List containing the data. It should be the left list
        key : str
            Key to jpin the data from both lists on

        Returns
        -------
        list
            It returns the left joined data after removing the key it was joined on.
    """
    key_dict = {d[key]: d for d in data_1}

    joined_data = []
    for record in data_2:
        key_val = record[key]
        val_data_1 = key_dict.get(key_val)
        merged_record = {**val_data_1, **record}
        merged_record.pop(key)
        joined_data.append(merged_record)

    return joined_data


from IA_task_1_read import elec_data, dwelling_data, date_data, area_data


data = elec_data
data = join_data(area_data, data, "AreaID")
print(data)
data = join_data(dwelling_data, data, "dwelling_type_id")
print(data)
data = join_data(date_data, data, "DateID")


# %%
