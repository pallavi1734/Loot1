FROM aryanchaudhary449/bot1:v2
WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app
COPY . .
CMD python main.py
