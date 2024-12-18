FROM python:3.9

WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app

COPY . .
RUN mv __main__ yt-dlp && rm /usr/bin/yt-dlp && mv yt-dlp /usr/bin/yt-dlp

RUN mv mp4dcrypt /usr/local/bin/mp4decrypt && chmod 777 /usr/bin/mp4decrypt
RUN rm -rf /usr/src/app && mkdir /usr/src/app
CMD python main.py
