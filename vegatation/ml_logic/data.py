import pandas as pd
from vegatation.params import *


def load_data(DATASET):

    data = pd.read_csv(DATASET)

    return data

def unencoded_Wilderness_Area(data):

    df_Wilderness_Area = data[Wilderness_columns]
    df_Wilderness_Area['wilderness'] = df_Wilderness_Area.idxmax(axis=1)
    df_Wilderness_Area = df_Wilderness_Area[['wilderness']]
    df_Wilderness_Area = df_Wilderness_Area.replace(wilderness_mapping)

    return df_Wilderness_Area

def unencoded_soil_type(data):

    df_Soil_Type = data[Soil_Type_columns]
    df_Soil_Type['Soil_Type'] = df_Soil_Type.idxmax(axis=1)
    df_Soil_Type = df_Soil_Type[['Soil_Type']]
    df_Soil_Type = df_Soil_Type.replace(soil_type_mapping)

    return df_Soil_Type

def unencoded_cover_type(data):

    df_cover_type = data[['Cover_Type']]
    df_cover_type = df_cover_type.replace(cover_type_mapping)
    df_cover_type.columns = ['cover_type']

    return df_cover_type

def unEncoded_data(data):

    df_Wilderness_Area = unencoded_Wilderness_Area(data)
    df_Soil_Type = unencoded_soil_type(data)
    df_cover_type = unencoded_cover_type(data)

    unencoded_data = pd.concat([data.iloc[:, :10],
    df_Wilderness_Area, df_Soil_Type, df_cover_type, data.iloc[:, 10:]], axis=1)

    return unencoded_data

def compress(unencoded_data, **kwargs):
    """
    Reduces the size of the DataFrame by downcasting numerical columns
    """
    input_size = unencoded_data.memory_usage(index=True).sum()/ 1024**2
    print("old dataframe size: ", round(input_size,2), 'MB')

    in_size = unencoded_data.memory_usage(index=True).sum()

    for t in ["float", "integer"]:
        l_cols = list(unencoded_data.select_dtypes(include=t))

        for col in l_cols:
            unencoded_data[col] = pd.to_numeric(unencoded_data[col], downcast=t)

    out_size = unencoded_data.memory_usage(index=True).sum()
    ratio = (1 - round(out_size / in_size, 2)) * 100

    print("optimized size by {} %".format(round(ratio,2)))
    print("new DataFrame size: ", round(out_size / 1024**2,2), " MB")

    return unencoded_data

def clean_data(unencoded_data):

    unencoded_data = unencoded_data.drop_duplicates()
    unencoded_data = unencoded_data.dropna(how='any', axis=0)


    unencoded_data = unencoded_data[unencoded_data.Elevation > 0]
    unencoded_data = unencoded_data[unencoded_data.Horizontal_Distance_To_Hydrology > 0]
    unencoded_data = unencoded_data[unencoded_data.Horizontal_Distance_To_Roadways > 0]
    unencoded_data = unencoded_data[unencoded_data.Horizontal_Distance_To_Fire_Points > 0]

    return unencoded_data
