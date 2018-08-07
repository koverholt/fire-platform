from debian:7

RUN apt-get update && apt-get install -y curl bzip2

RUN curl -L -o /tmp/anaconda.sh https://repo.anaconda.com/miniconda/Miniconda3-4.5.4-Linux-x86_64.sh
RUN bash /tmp/anaconda.sh -p /opt/anaconda -b
RUN rm /tmp/anaconda.sh
ENV PATH=/opt/anaconda/bin:${PATH}
RUN /opt/anaconda/bin/conda update -y conda
RUN /opt/anaconda/bin/conda install -y flask numpy

copy . /
EXPOSE 5000
CMD /opt/anaconda/bin python /hgl-temp.py