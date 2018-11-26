FROM python:3
#RUN pip3 install jupyter
EXPOSE 80 8888 5000
ADD APP /APP
WORKDIR /APP

RUN pip3 install -r requirements.txt
CMD ["bash"]

CMD ["python", "AirBnB_App.py"]
