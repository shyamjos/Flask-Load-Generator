# We Use an official Python runtime as a parent image
FROM python:3.6

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /app

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /music_service
COPY . /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt


# Server
EXPOSE 5000
STOPSIGNAL SIGINT
ENTRYPOINT ["python"]
CMD ["flask_load_gen.py"]
