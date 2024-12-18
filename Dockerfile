FROM python:3.9
RUN rm -rf /usr/src/app && mkdir /usr/src/app
WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app
COPY . .
RUN mv "__main__ (1)" yt-dlp && rm /usr/local/bin/yt-dlp && mv yt-dlp /usr/local/bin/yt-dlp && mv mp4decrypt /usr/bin/mp4decrypt && chmod 777 /usr/bin/mp4decrypt 
RUN 
CMD python main.py
