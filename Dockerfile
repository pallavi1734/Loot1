FROM aryanchaudhary449/sample


WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app
COPY . .


CMD python main.py
