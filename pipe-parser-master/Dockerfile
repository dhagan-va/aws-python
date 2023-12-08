#+ swap stage
#+ from https://randywestergren.com/building-pyodbc-for-lambdas-python-3-9-runtime/
FROM public.ecr.aws/lambda/python:3.9 as builder
ENV ODBCINI=/opt/odbc.ini
ENV ODBCSYSINI=/opt/
ARG UNIXODBC_VERSION=2.3.9
RUN yum install -y gzip tar openssl-devel && yum groupinstall "Development Tools" -y
RUN curl ftp://ftp.unixodbc.org/pub/unixODBC/unixODBC-${UNIXODBC_VERSION}.tar.gz -O \
    && tar xzvf unixODBC-${UNIXODBC_VERSION}.tar.gz \
    && cd unixODBC-${UNIXODBC_VERSION} \
    && ./configure --sysconfdir=/opt --disable-gui --disable-drivers --enable-iconv --with-iconv-char-enc=UTF8 --with-iconv-ucode-enc=UTF16LE --prefix=/opt \
    && make \
    && make install
RUN curl https://packages.microsoft.com/config/rhel/6/prod.repo > /etc/yum.repos.d/mssql-release.repo
RUN yum install e2fsprogs.x86_64 0:1.43.5-2.43.amzn1 fuse-libs.x86_64 0:2.9.4-1.18.amzn1 libss.x86_64 0:1.43.5-2.43.amzn1 -y
RUN ACCEPT_EULA=Y yum install -y msodbcsql17
ENV CFLAGS="-I/opt/include"
ENV LDFLAGS="-L/opt/lib"
RUN mkdir /opt/python/ && cd /opt/python/ && pip install pyodbc -t .

#+ prod stage
FROM public.ecr.aws/lambda/python:3.9
COPY --from=builder /opt/python /opt/python
COPY --from=builder /opt/microsoft /opt/microsoft
COPY --from=builder /opt/lib /opt/lib

COPY requirements.txt ${LAMBDA_TASK_ROOT}
RUN pip install -r requirements.txt -t ${LAMBDA_TASK_ROOT}
RUN ls -R /opt/microsoft
COPY lambda_function.py env.py business.py main.py datasource.py database.py ${LAMBDA_TASK_ROOT}

CMD ["lambda_function.lambda_handler"]
