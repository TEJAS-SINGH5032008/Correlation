
import ploty.express as px
import csv 
import numpy as np

def plotFigure(data_path):
  with open(data_path)as csv_files:
    df = csv.DictReader(csv_files)
  fig = px.scatter(df,x = "Weeks" , y = "cups of coffee ")
  fig.show()

  def getDataSource(data_path):
    coffee_in_ml = []
     sleep_in_hour= []
     with open(data_path)as csv_files:
       csv_reader  =csv.dictReader(csv_file)
       for row in csv_readrer:
         coffee_in_ml.append  (float(row["Weeks"]))
          sleep_in_hour.append  (float(row["cups of coffee"]))

         return{"x" : coffee_in_ml , "y" : sleep_in_hour}

         def findCorrelation(dataSource):
           correlation = np.corrcoef(datasource["x"] , datasource["y"])
           print("Correlation between weeks cupof coffee:- \n -->", correlation[0,1] )
           data_path = "coffee vs sleep in hour vs weeks - cups of coffee vs weeks data.csv"
           datasource = getDataSource(data_path)
           findCorrelation(datsource) 
           plotFigure(data_path)

           