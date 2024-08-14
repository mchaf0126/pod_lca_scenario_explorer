"""Data Manipulation functions."""
import pandas as pd


def create_all_impacts_df(df: pd.DataFrame,
                          scope: str) -> pd.DataFrame:
    """create the all impact dataframe for "All" option in results.

    Args:
        df (pd.DataFrame): _description_
        scope (str): _description_

    Returns:
        pd.DataFrame: _description_
    """
    new_df = pd.melt(
        df,
        id_vars=scope,
        value_vars=[
            'Global Warming Potential Total (kgCO2eq)',
            'Acidification Potential Total (kgSO2eq)',
            'Eutrophication Potential Total (kgNeq)',
            'Ozone Depletion Potential Total (CFC-11eq)',
            'Smog Formation Potential Total (kgO3eq)'
        ],
        var_name='Impacts',
        value_name='Impact Amount'
    )

    grouped_impacts = new_df.groupby(
        ['Impacts', scope]
    )[['Impact Amount']].sum()

    abs_value_group_impacts = grouped_impacts.copy()
    abs_value_group_impacts.loc[
        grouped_impacts['Impact Amount'] < 0, 'Impact Amount'
    ] = abs(grouped_impacts['Impact Amount'])
    neg_sum = abs_value_group_impacts.groupby('Impacts')[['Impact Amount']].sum()

    pos_sum = grouped_impacts.loc[
        grouped_impacts['Impact Amount'] > 0
    ].groupby('Impacts')[['Impact Amount']].sum()

    new_grouped_impacts = grouped_impacts.reset_index(level=1)

    new_grouped_impacts.loc[
        new_grouped_impacts['Impact Amount'] > 0, 'total_impact'
    ] = pos_sum['Impact Amount']
    new_grouped_impacts.loc[
        new_grouped_impacts['Impact Amount'] < 0, 'total_impact'
    ] = neg_sum['Impact Amount']

    new_grouped_impacts['percentage'] = \
        new_grouped_impacts['Impact Amount'].div(new_grouped_impacts['total_impact'])

    new_grouped_impacts = new_grouped_impacts.reset_index().replace(
        {
            'Global Warming Potential Total (kgCO2eq)': 'GWP',
            'Acidification Potential Total (kgSO2eq)': 'AP',
            'Eutrophication Potential Total (kgNeq)': 'EP',
            'Ozone Depletion Potential Total (CFC-11eq)': 'ODP',
            'Smog Formation Potential Total (kgO3eq)': 'SFP'
        }
    )
    return new_grouped_impacts
