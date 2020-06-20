FROM python:3.8

COPY scripts scripts
RUN python -m pip install elasticsearch

ENTRYPOINT ["bash","/scripts/start.sh"]