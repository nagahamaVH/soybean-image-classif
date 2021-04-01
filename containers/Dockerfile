# syntax=docker/dockerfile:experimental
FROM nvidia/cuda:11.0-cudnn8-devel-rc

RUN apt-get update
RUN apt-get install python3 python3-pip -y

RUN python3 -m pip install pip -U

RUN apt-get install curl -y
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -

RUN pip3 install plotly -U
RUN pip3 install 'jupyterlab<3.0.0' ipywidgets -U

RUN apt-get install nodejs -y

RUN jupyter labextension install jupyterlab-plotly
RUN jupyter labextension install @jupyter-widgets/jupyterlab-manager plotlywidget

WORKDIR /notebook/workspace
RUN chown -R 1001:1001 /notebook
RUN chmod 755 /notebook

ENV HOME /notebook

COPY requirements.txt .

RUN --mount=type=cache,mode=0755,target=/notebook/.cache/pip pip3 install -r requirements.txt

RUN apt-get install libgl1-mesa-glx -y

USER 1001:1001

CMD jupyter lab --ip="0.0.0.0" --no-browser --port=9999
