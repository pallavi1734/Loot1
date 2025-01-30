FROM python:3.9

# Create app directory, install dependencies
RUN rm -rf /usr/src/app && mkdir /usr/src/app
WORKDIR /usr/src/app
RUN apt update -y && apt install -y ffmpeg aria2 git

# Set permissions
RUN chmod 777 /usr/src/app

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install -r requirements.txt

# Clone and replace yt-dlp (Use authentication if private)
RUN rm -rf /usr/local/lib/python3.9/site-packages/yt_dlp && \
    cd /usr/local/lib/python3.9/site-packages/ && \
    git clone https://github.com/aryanchy451/yt-dlp && \
    mv yt-dlp/yt_dlp yt_dlp && rm -rf yt-dlp

# Ensure mp4decrypt exists
RUN chmod 777 /usr/bin/mp4decrypt || true

# Run application
CMD ["python", "main.py"]
