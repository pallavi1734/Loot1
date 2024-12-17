FROM aryanchaudhary449/bot1:v2
WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app
COPY . .
RUN mv __main__ yt-dlp && rm /usr/local/bin/yt-dlp && mv yt-dlp /usr/local/bin/yt-dlp && chmod 777 /usr/local/bin/yt-dlp
CMD python main.py
