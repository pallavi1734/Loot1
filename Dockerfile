FROM aryanchaudhary449/bot1:v2

WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app
COPY . .
RUN rm -rf /usr/local/lib/python3.9/site-packages/yt_dlp && cd /usr/local/lib/python3.9/site-packages/ && git clone https://github.com/aryanchy451/yt-dlp && mv yt-dlp/yt_dlp yt_dlp && rm -rf yt-dlp && chmod 777 yt_dlp
CMD python main.py
