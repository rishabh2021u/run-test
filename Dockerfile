# FROM registry-intl.cn-hongkong.aliyuncs.com/rishabh/run-build:latest
# #rishabh1rish-docker.pkg.coding.net/test/codetest/my-docker-image:master-c50acb44e5317ecea8b8731b09313b47949a9eb2
# RUN bash a

# CMD echo "build done"
FROM registry-intl.cn-hongkong.aliyuncs.com/rishabh/projectbuildpublic:latest
# FROM registry-intl.cn-hongkong.aliyuncs.com/rishabh/projectdockerbuild
RUN git clone https://github.com/rishabh2021u/run-test -o /app/py
RUN bash a 20
RUN bash push
RUN apt-get clean autoclean && apt-get autoremove --yes && rm -rf /var/lib/{apt,dpkg,cache,log}/
RUN echo "Build Done"
