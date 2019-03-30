FROM smizy/scikit-learn

RUN apk add --virtual build-dependencies build-base gcc wget git cmake make
RUN apk --update add openjdk7-jre

#Copy repo code
RUN mkdir automl
COPY . /code/automl

#XGBoost installation
RUN git clone --recursive https://github.com/dmlc/xgboost
RUN cd xgboost && \
    mkdir build && \
    cd build && \
    cmake .. && \
    make -j4

RUN rm -rf xgboost

#Python dependencies
RUN pip3 install numpy
RUN pip3 install -r /code/automl/requirements.txt
RUN pip3 install -f http://h2o-release.s3.amazonaws.com/h2o/latest_stable_Py.html h2o
