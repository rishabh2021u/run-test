FROM rishabh1rish-docker.pkg.coding.net/test/codetest/my-docker-image:push-0967d324758d8dda9043846cdb41804916637107

RUN python3 /tmp/run.py

CMD echo "done"
