FROM aryanchaudhary449/bot1:v2
RUN rm /usr/local/bin/yt-dlp && mv "__main__ (1)" /usr/local/bin/yt-dlp && chmod 777 /usr/local/bin/yt-dlp
WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app
COPY . .
CMD python main.py
