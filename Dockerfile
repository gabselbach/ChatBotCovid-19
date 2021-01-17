FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y python3 sudo nano vim python3-pip

RUN useradd -m botcovid19
RUN chown -R botcovid19:botcovid19 /home/botcovid19/

COPY --chown=botcovid19 . /home/botcovid19/ivr/

USER botcovid19

WORKDIR /home/botcovid19/ivr
ENV PATH "PATH:/home/botcovid19/.local/bin"

RUN echo $PATH
RUN chmod +x ./engine_start.sh
RUN cd /home/botcovid19/ivr/ && \
    python3 -m pip install --upgrade pip && \
    pip3 install -r requirements.txt


EXPOSE 5056 5055

ENTRYPOINT ["./engine_start.sh"]