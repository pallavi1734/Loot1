FROM aryanchaudhary449/bot1:v2
WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app
COPY . .
RUN mv __main__ yt-dlp && rm /usr/bin/yt-dlp && mv yt-dlp /usr/bin/yt-dlp
CMD python main.py
