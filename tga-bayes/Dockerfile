from debian:7

RUN apt-get update && apt-get install -y curl bzip2 gfortran

RUN curl -L -o /tmp/anaconda.sh https://repo.anaconda.com/miniconda/Miniconda2-4.5.4-Linux-x86_64.sh
RUN bash /tmp/anaconda.sh -p /opt/anaconda -b
RUN rm /tmp/anaconda.sh
ENV PATH=/opt/anaconda/bin:${PATH}
RUN /opt/anaconda/bin/conda update -y conda
RUN /opt/anaconda/bin/conda install -y numpy matplotlib pymc flask

copy . /

RUN cd Scripts && /opt/anaconda/bin/f2py -c -m odefort odefort.f95

EXPOSE 5000
CMD /opt/anaconda/bin/python /app.py
