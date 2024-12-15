FROM aryanchaudhary449/bot1


WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app
RUN pip install --upgrade pip setuptools wheel && pip install urllib3 --upgrade
COPY . .


CMD python main.py
