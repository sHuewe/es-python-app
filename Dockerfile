ARG PYTHON_IMAGE=python:3.8
FROM $PYTHON_IMAGE

COPY scripts es_python_app_scripts
RUN python -m pip install elasticsearch

ENTRYPOINT ["bash","/es_python_app_scripts/start.sh"]