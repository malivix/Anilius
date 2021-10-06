FROM centos/s2i-base-centos7

EXPOSE 8080
EXPOSE 8081

ARG GIT_SHA=0
ENV GIT_SHA=$GIT_SHA
ENV TZ=UTC
ENV PHASE=build
ENV APP_ROOT=/opt/app-root
ENV SCRIPTS_PATH=/opt/app-root/scripts
ENV PYTHON_VERSION=3.6 \
    PATH=$HOME/.local/bin/:$PATH \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=UTF-8 \
    LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    PIP_NO_CACHE_DIR=off

RUN INSTALL_PKGS="rh-python36 rh-python36-python-devel rh-python36-python-setuptools rh-python36-python-pip nss_wrapper \
        httpd24 httpd24-httpd-devel httpd24-mod_ssl httpd24-mod_auth_kerb httpd24-mod_ldap \
        httpd24-mod_session atlas-devel gcc-gfortran libffi-devel libtool-ltdl enchant MySQL-python" && \
    yum install -y centos-release-scl && \
    yum -y --setopt=tsflags=nodocs install --enablerepo=centosplus $INSTALL_PKGS && \
    rpm -V $INSTALL_PKGS && \
    # Remove centos-logos (httpd dependency) to keep image size smaller.
    rpm -e --nodeps centos-logos && \
    yum -y clean all --enablerepo='*'

RUN source scl_source enable rh-python36 && \
    virtualenv ${APP_ROOT}

WORKDIR ${APP_ROOT}

RUN pip install -U pip setuptools wheel

COPY ./pip/requirements.txt ${APP_ROOT}
RUN pip install -r ${APP_ROOT}/requirements.txt

COPY . ${APP_ROOT}
RUN chown -R 1001:0 ${APP_ROOT} && \
    chmod +x ${APP_ROOT}/main.py && \
    chmod +x -R ${SCRIPTS_PATH} && \
    fix-permissions ${APP_ROOT} -P && \
    rpm-file-permissions


USER 1001

STOPSIGNAL SIGTERM
CMD $SCRIPTS_PATH/run.sh
