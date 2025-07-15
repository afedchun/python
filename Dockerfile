FROM Ubuntu.20.04
LABEL maintainer="Artem Fedchun"

# Install dependencies
RUN apt-get update && \ 
    apt-get install -y python3 python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
# Set the working directory
WORKDIR /app
# Copy the requirements file
COPY requirements.txt .
# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt
# Copy the application code
COPY . .
# Expose the port the app runs on
EXPOSE 5000
# Set the environment variable for Flask
ENV FLASK_APP=app.py