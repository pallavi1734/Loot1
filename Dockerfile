FROM python:3.9

# Create app directory and install dependencies
RUN rm -rf /usr/src/app && mkdir /usr/src/app
WORKDIR /usr/src/app
RUN apt update -y && apt install -y ffmpeg aria2 git

# Set permissions
RUN chmod 777 /usr/src/app

# Copy project files
COPY . .

# Install Python dependencies and official yt-dlp
RUN pip install -r requirements.txt && \
    pip install -U yt-dlp

# Ensure mp4decrypt exists
RUN chmod 777 /usr/bin/mp4decrypt || true

# Run application
CMD ["python", "main.py"]
