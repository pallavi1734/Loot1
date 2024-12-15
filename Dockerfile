FROM aryanchaudhary449/bot1


WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app
RUN chmod 777 /usr/bin/mp4decrypt
COPY . .


CMD python main.py
