FROM centos:centos7
MAINTAINER Chris Collins <collins.christopher@gmail.com>

ENV container docker

RUN yum install -y mariadb bzip2 python-yaml && yum clean all
ADD mysql-backup.py /mysql-backup.py

CMD ["/mysql-backup.py"]

