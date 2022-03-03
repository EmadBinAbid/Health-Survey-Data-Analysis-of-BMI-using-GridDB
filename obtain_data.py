
import numpy as np
import griddb_python as griddb
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

factory = griddb.StoreFactory.get_instance()

argv = sys.argv

try:
    # Get GridStore object
    # Provide the necessary arguments
    gridstore = factory.get_store(
        host=argv[1], 
        port=int(argv[2]), 
        cluster_name=argv[3], 
        username=argv[4], 
        password=argv[5]
    )

    # Define the container names
    data_container = "data_container"

    # Get the containers
    obtained_data = gridstore.get_container(data_container)
    
    # Fetch all rows - language_tag_container
    query = obtained_data.query("select *")
    
    rs = query.fetch(False)
    print(f"{data_container} Data")

    
    # Iterate and create a list
    retrieved_data= []
    while rs.has_next():
        data = rs.next()
        retrieved_data.append(data)

    # Convert the list to a pandas data frame
    data = pd.DataFrame(retrieved_data,
                        columns=["ID","GeneralHealthCondition", "HowHealthyIsTheDiet", 
                                 "WeightKg", "StandingHeightCm","BodyMassIndexKgm2",
                                 "WaistCircumferenceCm", "DirectHdlcholesterolMgdl", 
                                 "TotalCholesterolMgdl", "EverToldYouHadHeartAttack", 
                                 "EverToldYouHadAStroke" ,"Gender" ])

    # Get the data frame details
    print(data)
    data.info()
    
    
except griddb.GSException as e:
    for i in range(e.get_error_stack_size()):
        print("[", i, "]")
        print(e.get_error_code(i))
        print(e.get_location(i))
        print(e.get_message(i))
 
##creating new columns with BMI categories        
def categoriseBMI(row):  
    if row['BodyMassIndexKgm2'] < 18.5:
        return 'Underweight'
    if row['BodyMassIndexKgm2'] >= 18.5 and row['BodyMassIndexKgm2'] < 24.9:
        return 'Healthy Weight'
    if row['BodyMassIndexKgm2'] >= 25.0 and row['BodyMassIndexKgm2'] < 29.9:
        return 'Overweight'
    else:
        return 'Obesity'

data['BMI category'] = data.apply(lambda row: categoriseBMI(row), axis=1)


##comapre BMI of men and women
Gender_groupby = data.groupby(["Gender", "BMI category"], as_index = False).count()
sns.barplot(x="BMI category", y="HDL Level", hue="Gender", data=Gender_groupby)
plt.ylabel("Count")
plt.show()

##creating new columns with HDL Level  
def categoriseHDL(row):  
    if row['DirectHdlcholesterolMgdl'] >= 40:
        return 'Normal'
    else:
        return 'Dangerzone'
    
data['HDL Level'] = data.apply(lambda row: categoriseHDL(row), axis=1)
HDL_groupby = data.groupby(["HDL Level", "BMI category"], as_index = False).count()


##plotting relation between BMI and HDL colestrol
sns.barplot(x="BMI category", y="Gender", hue="HDL Level", data=HDL_groupby)
plt.ylabel("Count")
plt.show()

##BMI and How healthy is diet
Diet_groupby = data.groupby(["HowHealthyIsTheDiet", "BMI category"], as_index = False).count()
sns.barplot(x="BMI category", y="HDL Level", hue="HowHealthyIsTheDiet", data=Diet_groupby)
plt.ylabel("Count")
plt.show()

##subset the true values of stroke and heart attack then plot their BMI's 
data_stroke = data[data["EverToldYouHadAStroke"] == 1]
stroke_groupby = data_stroke.groupby(["BMI category"], as_index = False).count()
sns.barplot(x="BMI category", y="HDL Level", data=stroke_groupby)
plt.ylabel("Count")
plt.title("Relation between BMI and chances of stroke")
plt.show()

data_heartattack = data[data["EverToldYouHadHeartAttack"] == 1]
heartattack_groupby = data_heartattack.groupby(["BMI category"], as_index = False).count()
sns.barplot(x="BMI category", y="HDL Level", data=heartattack_groupby)
plt.ylabel("Count")
plt.title("Relation between BMI and chances of heart attack")
plt.show()