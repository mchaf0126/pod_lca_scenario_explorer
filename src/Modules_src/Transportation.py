import pandas as pd
from pathlib import Path
import os


def transportation(module_folder_path, templatemodel_path):

    #STEP1: Importing CSVs and change them to dataframe
    dfs = {}
    for file in sorted (os.listdir(module_folder_path)):
        if file.endswith(".csv"):
            
            file_path = os.path.join (module_folder_path, file)
            df = pd.read_csv (file_path)
            df_name = os.path.splitext (file)[0]
            dfs[df_name] = df
            
    tem_df = pd.read_csv(templatemodel_path)
    trans_mass = tem_df[tem_df['Life Cycle Stage'] == '[A1-A3] Product']
    trans_mass = trans_mass[['element_index', 'Material Group', 'Mass Total (kg)']]
    dfs_keys = list(dfs.keys())

        # IMPORTANT: Variable names should be written in alphabetical order
    distances, mode_scenario, modes, scenarios, stg_code, trans_mode = (
    dfs[dfs_keys[i]] for i in range(len(dfs_keys)))

    #STEP2: Merging the dataframes
    
    mass = (trans_mass.merge(stg_code, how='right', left_on='Material Group', right_on='material_id').drop(columns='material_id'))

    mode_scenario_df = (mode_scenario.merge(modes, left_on='mode_id', right_on='id', suffixes=(None, '_mode')).merge(scenarios,left_on='scenario_id',
        right_on='id', suffixes=(None, '_scenario')))

    mode_scenario_df = mode_scenario_df[['id', 'name', 'name_scenario']].rename(columns={'name': 'mode_name', 'name_scenario': 'scenario_name'})

    trans_mode_df = (trans_mode.merge( mode_scenario_df, left_on='mode_scenario_id', right_on='id', suffixes=(None, '_mode_scenario')))

    trans_mode_df = trans_mode_df[['mode_scenario_id', 'return_trip_factor', 'gwp', 'mode_name', 'scenario_name']]

    mass_distance = mass.merge(distances, how='left', on = 'stg_code')

    final = mass_distance.merge( trans_mode_df, on = 'mode_scenario_id').drop(columns=['id', 'mode_scenario_id', 'reference'])

    #STEP3: Calculation
    final = final.assign(total_a4=final['Mass Total (kg)'] * final['distance'] * final['gwp'] * final['return_trip_factor'])

    return final



if __name__ == "__main__":

    module_folder_path = r"C:\Users\mhtaba\Desktop\pod_lca_building_git\pod_lca_scenario_explorer\data\databases\transportation"
    templatemodel_path = r"C:\Users\mhtaba\Desktop\pod_lca_building_git\pod_lca_scenario_explorer\data\template_model\Template_Model_1.csv"

    test = transportation(module_folder_path, templatemodel_path)
    print (test)
