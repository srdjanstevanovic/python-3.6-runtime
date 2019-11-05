FROM openwhisk/python3action

# lapack-dev is available in community repo.
RUN echo "http://dl-4.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories

# add package build dependencies
RUN apk add --no-cache \
        g++ \
        lapack-dev \
        gfortran


COPY requirements.txt requirements.txt
RUN pip install --upgrade pip setuptools six && pip install --no-cache-dir -r requirements.txt