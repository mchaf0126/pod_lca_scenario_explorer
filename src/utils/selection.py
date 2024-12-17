from dash import html, dcc
import dash_bootstrap_components as dbc


def create_dropdown(label: str, dropdown_list: list, first_item: str, dropdown_id: str) -> html.Div:
    """_summary_

    Args:
        labe (str): _description_
        dropdown_list (list): _description_
        first_item (str): _description_
        id (str): _description_

    Returns:
        html.Div: _description_
    """

    dropdown = html.Div(
        [
            dbc.Label(label),
            dcc.Dropdown(
                options=dropdown_list,
                value=first_item,
                id=dropdown_id,
                clearable=False,
                persistence=True,
                optionHeight=50
            ),
        ],
        className='mb-4'
    )
    return dropdown


def create_checklist(label: str,
                     checklist: list,
                     first_item: str,
                     dropdown_id: str) -> html.Div:
    """_summary_

    Args:
        labe (str): _description_
        dropdown_list (list): _description_
        first_item (str): _description_
        id (str): _description_

    Returns:
        html.Div: _description_
    """

    checklist = html.Div(
        [
            dbc.Label(label),
            dbc.Checklist(
                options=checklist,
                value=first_item,
                id=dropdown_id,
                persistence=True,
                inputCheckedClassName="border border-primary bg-primary"
            ),
        ],
        className='mb-4'
    )
    return checklist


def create_slider(label: str,
                  min_value: float,
                  max_value: float,
                  step: float,
                  marks: dict,
                  value: float,
                  slider_id: str) -> html.Div:
    """_summary_

    Args:
        label (str): _description_
        min (float): _description_
        max (float): _description_
        step (dict): _description_
        value (float): _description_
        id (str): _description_

    Returns:
        html.Div: _description_
    """
    slider = html.Div(
        [
            dbc.Label(label),
            dcc.Slider(
                min=min_value,
                max=max_value,
                step=step,
                marks=marks,
                value=value,
                id=slider_id,
            ),
        ],
        className='mb-4'
    )
    return slider


def create_radio(label: str,
                 radiolist: list,
                 first_item: str,
                 radio_id: str) -> html.Div:
    """_summary_

    Args:
        labe (str): _description_
        dropdown_list (list): _description_
        first_item (str): _description_
        id (str): _description_

    Returns:
        html.Div: _description_
    """

    radioitems = html.Div(
        [
            dbc.Label(label),
            dbc.RadioItems(
                options=radiolist,
                value=first_item,
                id=radio_id,
                inputCheckedClassName="border border-primary bg-primary"
            ),
        ],
        className='mb-4'
    )
    return radioitems
