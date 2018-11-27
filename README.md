# Spark-Docker-Assighnment

Spark:

   file AirBnB_EDA.ipynb: Includes data exploration from the DataCup assignment written in Spark      

Docker:

   1- Download  Spark-Docker-Assighnment folder to c:
   
   2- Go to c:\ Spark-Docker-Assighnment
   
   3- build the docker application
    
         docker build -t airbnb_app .
   
   4- to run the app directly execute below steps:
               
         docker run -it -p 8888:8888 -p 80:80 -p 5000:5000 airbnb_app 

      - open the following link:  http://0.0.0.0:5000/ 
       
   4- to run AirBnB_App.ipynb on jupyter
   
         docker run -it -p 8888:8888 -p 80:80 -p 5000:5000 airbnb_app bash
         
      - in bash run the following command:
       
         jupyter notebook --ip 0.0.0.0 --no-browser --allow-root

