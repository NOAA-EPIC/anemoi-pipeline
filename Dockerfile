FROM continuumio/miniconda3

COPY ./env/anemoi_pipeline.yaml .
RUN conda env create --file anemoi_pipeline.yaml python=3.12
