from src.utils.selection import create_radio
from src.utils.load_config import app_config

config = app_config

energy_use_radio_yaml = config.get('energy_use_scenario_radio')
assert energy_use_radio_yaml is not None, 'The config for scenario checklist could not be set'

energy_use_radio_model_comp = create_radio(
    label=energy_use_radio_yaml['label'],
    radiolist=energy_use_radio_yaml['radiolist'],
    first_item=energy_use_radio_yaml['first_item'],
    radio_id=energy_use_radio_yaml['radio_id']
)
