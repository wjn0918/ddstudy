---
title: Bigtop
---



docker run -d -it -p 8000:8000 --network bigtop -v ./:/ws -v /root/.m2:/root/.m2 --workdir /ws --name hello bigtop/slaves:3.3.0-centos-7


/usr/local/maven/conf/settings.xml

. /etc/profile.d/bigtop.sh

gradle  -PparnetDir=/usr/bigtop -PsuffixPkg repo

gradle zookeeper-rpm -PparnetDir=/usr/bigtop -PsuffixPkg repo






yum -y install fuse-devel cmake cmake3 lzo-devel openssl-devel protobuf* cyrus-*

./gradlew tasks