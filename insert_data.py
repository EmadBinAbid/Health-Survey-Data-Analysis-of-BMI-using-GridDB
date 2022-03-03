import griddb_python as griddb
import sys
import pandas as pd
from nhanes.load import load_NHANES_data, load_NHANES_metadata

factory = griddb.StoreFactory.get_instance()

argv = sys.argv

try:
    
    data_df = load_NHANES_data()
    
    
    data_unprocessed = data_df[["GeneralHealthCondition", "HowHealthyIsTheDiet", "WeightKg", "StandingHeightCm","BodyMassIndexKgm2","WaistCircumferenceCm", "DirectHdlcholesterolMgdl", "TotalCholesterolMgdl", "EverToldYouHadHeartAttack", "EverToldYouHadAStroke" ,"Gender" ]]
        
        
    print(data_unprocessed)
    
    data_unprocessed.dropna(inplace=True)
    data_unprocessed.reset_index(drop=True, inplace=True)
    data_unprocessed.index.name = 'ID'
    
    #data_unprocessed['EverToldYouHadHeartAttack'] = data_unprocessed['EverToldYouHadHeartAttack'].astype(bool)
    #data_unprocessed['EverToldYouHadAStroke'] = data_unprocessed['EverToldYouHadAStroke'].astype(bool) 
    
    data_unprocessed.to_csv("preprocessed.csv")
    
    #read the cleaned data from csv
    data_processed = pd.read_csv("preprocessed.csv")

    for row in data_processed.itertuples(index=False):
            print(f"{row}")

    # View the structure of the data frames
    data_processed.info()

    # Provide the necessary arguments
    gridstore = factory.get_store(
        host=argv[1], 
        port=int(argv[2]), 
        cluster_name=argv[3], 
        username=argv[4], 
        password=argv[5]
    )

    #Create container 
    data_container = "data_container"

    # Create containerInfo
    data_containerInfo = griddb.ContainerInfo(data_container,
                    [["ID", griddb.Type.INTEGER],
        		    ["GeneralHealthCondition", griddb.Type.STRING],
         		    ["HowHealthyIsTheDiet", griddb.Type.STRING],
                    ["WeightKg", griddb.Type.FLOAT],
                    ["StandingHeightCm", griddb.Type.FLOAT],
         		    ["BodyMassIndexKgm2", griddb.Type.FLOAT],
                    ["WaistCircumferenceCm", griddb.Type.FLOAT],
                    ["DirectHdlcholesterolMgdl", griddb.Type.FLOAT],
                    ["TotalCholesterolMgdl", griddb.Type.FLOAT],
         		    ["EverToldYouHadHeartAttack", griddb.Type.FLOAT],
                    ["EverToldYouHadAStroke", griddb.Type.FLOAT],
                    ["Gender", griddb.Type.STRING]],
                    griddb.ContainerType.COLLECTION, True)
    
    data_columns = gridstore.put_container(data_containerInfo)
    
    # Put rows
    data_columns.put_rows(data_processed)
    
    print("Data Inserted using the DataFrame")

except griddb.GSException as e:
    print(e)
    for i in range(e.get_error_stack_size()):
        print(e)
        # print("[", i, "]")
        # print(e.get_error_code(i))
        # print(e.get_location(i))
        print(e.get_message(i))
