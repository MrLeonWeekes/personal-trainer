FROM python:3.6
COPY . .
RUN pip3 install -r requirements.txt
ENV DB_URI=sqlite:///data.db SECRET_KEY=shhhhh
RUN python3 create.py
EXPOSE 5000
ENTRYPOINT ["python3","app.py"]

