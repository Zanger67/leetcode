# https://leetcode.com/problems/combine-two-tables/description/

import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(left=person, right=address, how='left', on='personId')[['firstName', 'lastName', 'city', 'state']]