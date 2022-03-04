# Health-Survey-Data-Analysis-of-BMI-using-GridDB

**Introduction:**

BMI (Body mass index) is a ratio of body mass to height, used as a
health indicator among many fitness trainers and health professionals. A
person is classified into different categories, normal, overweight,
obese, and extremely obese, according to their gender and BMI.

We will be using National Health and Nutrition Examination Survey
(NHANES) data to relative different health indicators with BMI.
The [National Health and Nutrition Examination Survey
(NHANES)](https://www.cdc.gov/nchs/nhanes/index.htm) data is a complex
survey of tens of thousands of people designed to assess the health and
nutritional status of adults and children in the United States. The
NHANES data includes many measurements related to overall health,
physical activity, diet, psychological health, socioeconomic factors,
and more.

**Exporting and Import dataset using GridDB:**

We will be using GridDB to store a large amount of preprocessed data
from NHANES. GridDB is a highly scalable and in-memory No SQL database
that allows parallel processing for higher performance and efficiency.
It is optimized for time-series databases for IoT and big data
technologies. Using GridDB’s python client, we would be able to import
or export data in real-time.

*Setup GridDB*:

First and foremost, we need to make sure that we have properly installed
GridDB on our system. You can find the step-by-step guide to set up
GridDB on different operating systems using this
[link](https://griddb.net/en/blog/griddb-quickstart/).

*Dataset:*

NHANES has their built-in libraries available on python as well as R. we
would be able to use the data by installing the NHANES library by
running the following command on python or anaconda command prompt.

![](media/image1.png){width="5.729166666666667in"
height="0.3645833333333333in"}

Next, you can import the library and save the data into any variable; in
this case, “data\_df”. ![](media/image2.png){width="6.5in"
height="0.46875in"}

Along with the NHANES library, we would be using Pandas, Matplotlib, and
Seaborn library to analyze and visualize the dataset.

*Data Preprocessing:*

NHANES dataset contains around 200 variables, containing information
about diet and health conditions of the person. To make our analysis
easier to understand and concentrated on conditions affecting BMI, we
will filter out some columns that seem to be more important.

![](media/image3.png){width="6.5in" height="0.8138888888888889in"}

Lastly, we would drop the NULL columns and introduce the primary key
column into our dataset:

![](media/image4.png){width="5.668505030621172in"
height="0.5480774278215224in"}

To keep a local copy of the data, we can save it as a CSV file on our
system before exporting it on GridDB.

![](media/image5.png){width="6.067307524059492in"
height="0.36624234470691164in"}

*Uploading the data to GridDB:*

The standard approach set by GridDB to insert data is to create a
container and use the put methods.

![](media/image6.png){width="6.5in" height="3.6145833333333335in"}

We have successfully exported the data to the GridDB cloud without any
errors and can now access the data from anywhere using the GridDB
interface.

*Accessing Data from GridDB:*

To access the data from the GridDB cloud, we need to query out the
database using TQL, GridDB’s query language. TQL uses similar commands
to the standard SQL protocols to query data from the GridDB container.

![](media/image7.png){width="5.509615048118985in"
height="1.6084525371828522in"}

The next step would be to save the queried data into a dataframe to use
for analysis. We achieve this using pd.DataFrame() method to convert the
GridDB container lists to the data frame.

![](media/image8.png){width="6.5in" height="2.063888888888889in"}

**Analysis and Visualization:**

Before starting the analysis, we will import some python libraries to
help us in our project:

![](media/image9.png){width="6.5in" height="0.6805555555555556in"}

We will use a lambda method to apply the categorizeBMI function to our
data and divide it into four levels; ‘Underweight’, ‘Healthy Weight’,
‘Overweight’, and ‘Obesity’

![](media/image10.png){width="6.5in" height="1.7333333333333334in"}

We would start by exploring the relationship between BMI and the gender
of the person, to get an idea of how BMI varies among males and females.

![](media/image11.png){width="6.5in" height="0.8555555555555555in"}

![](media/image12.png){width="3.7692311898512685in"
height="2.500097331583552in"}

Figure : Male and Females with different BMI levels

As the graph shows, although men are more likely to be overweight than
women, women have higher chances of being obsessed.

One of our columns contains the HDL cholesterol level of the person.
Normal HDL levels are above 40 according to CDC, so we will use this
information to categorize the person into two categories; ‘Normal’ and
‘Dangerzone’.

![](media/image13.png){width="6.5in" height="1.1743055555555555in"}

We will use HDL level and BMI category to divide the data into sections
and examine how the BMI level affects the HDL level of a person.

![](media/image14.png){width="6.5in" height="0.9826388888888888in"}

![](media/image15.png){width="3.4519225721784776in"
height="2.2896292650918637in"}

Figure BMI categories in relation with HDL levels

We can see that a person is more likely to be in the danger zone when
their BMI would be in the Obesity or Overweight range.

Similarly, we will use BMI levels to investigate their relationship with
the diet taken by the person.

![](media/image16.png){width="6.5in" height="0.8638888888888889in"}

![](media/image17.png){width="3.971153762029746in"
height="2.705285433070866in"}

Figure : Diet effect on BMI category

It is evident by looking into the above graph that the highest number of
people having poor or fair diet end up facing obesity, while most of the
people having excellent diet have a healthy weight.

Lastly, but most important factor to compare with BMI is the chances of
strokes or heart attack. For that, we will first filter out the people
who had stroke or heart attack individually and then explore their BMI
levels.

![](media/image18.png){width="6.77380905511811in"
height="1.9322725284339457in"}

![](media/image19.png){width="3.1983562992125982in"
height="2.2857141294838144in"}![](media/image20.png){width="3.2649890638670165in"
height="2.3333333333333335in"}

> Figure & 5: Relationship between Stroke/Heart Attack and BMI

As expected, the graph verifies our common concern that people dealing
with obesity or overweight are more prone to having strokes or/and heart
attacks.

**Conclusion:**

NHANES survey data aided us to conclude that BMI should be an important
concern for people as it can be the reason for adverse health
conditions. Similarly, the diet of the person is a major contributor to
the BMI level of a person, and therefore, we should take care of our
diet to live a healthy life. All of the analysis was done using the
GridDB database at the backend, making the integration seamless and
efficient.
