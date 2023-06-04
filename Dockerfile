#Docker
# Use an official Python base image from the Docker Hub
FROM python:3.10-slim

# Install git and chromium-driver
RUN apt-get update \
    && apt-get install -y git chromium-driver

# Install Xvfb and other dependencies for headless browser testing
RUN apt-get install -y wget gnupg2 libgtk-3-0 libdbus-glib-1-2 dbus-x11 xvfb ca-certificates

# Install Firefox / Chromium
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y chromium firefox-esr

# # Install Python3 and pip3
RUN apt install -y python3 python3-pip git 

RUN pip3 install --upgrade pip


# Set environment variables
ENV PIP_NO_CACHE_DIR=yes \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="/home/.local/bin:$PATH"

# Create a non-root user and set permissions
# RUN useradd --create-home appuser
# WORKDIR /home/appuser
# RUN chown appuser:appuser /home/appuser
# USER appuser:appuser
ENV APP_HOME /app/
WORKDIR $APP_HOME

# # Set the working directory
# WORKDIR /home/appuser/app/ui

# Copy the requirements.txt file and install the requirements
COPY requirements.txt .
RUN export PATH="/root/.local/bin:$PATH" && \
	pip3 install -r requirements.txt

# Copy the application files
COPY . /app

#copy migrations
RUN export PATH="/root/.local/bin:$PATH" && \
    python manage.py migrate
RUN export PATH="/root/.local/bin:$PATH" && \
    python manage.py collectstatic 

# Expose the port
EXPOSE 3000

# Set the entrypoint
ENTRYPOINT ["python", "manage.py","runserver", "0.0.0.0:3000"]
