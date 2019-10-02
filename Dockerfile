# load the base docker image
FROM alpine:latest

#install python3 and pip3 inside the alpine image
RUN apk add --no-cache python3-dev && pip3 install --upgrade pip

#copy the source code and libraries inside the alpine image
#creating a app_directory inside my image
WORKDIR /app
#copy everything inside the app_dir of image
COPY . /app
#run pip cmd to install all libraies form requirements.txt
RUN pip3 --no-cache-dir install -r requirements.txt

#Expose a port
EXPOSE 5000

#Now build the EXECUTABLE IMAGE using python CMD
# python3 app.py
ENTRYPOINT ["python3"]
CMD ["main.py"]

#################################################################
# create an image from cmd
#docker build -t nyclibrary:latest .

#damon RUN (PUBLIC), IT will RUN in DOCKER VIRTUALLY using "PORT-FORWORDING"
#docker run -it -d -p 5000:5000 nyclibrary

# see all the running container of a image
#docker ps

#NB:: docker stop to stop the container
#docker stop <IMAGE-ID>

#show all my images
# docker images
