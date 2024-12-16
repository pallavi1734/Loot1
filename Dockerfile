FROM aryanchaudhary449/bot1

RUN rm -rf /usr/src/app && mkdir /usr/src/app
WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app
RUN apt install aria2 -y
COPY . .


CMD python main.py
