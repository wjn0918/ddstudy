# 编译atlas


mvn clean -DskipTests install

mvn clean -DskipTests package -Pdist,embedded-hbase-solr

# 启动zookeeper


# 启动hbase


# 启动solr

solr/bin/solr start -p 8983 -z localhost:2181 -force


# 创建索引

solr/bin/solr  create -c fulltext_index -force -d conf/solr/ 
solr/bin/solr  create -c edge_index -force -d conf/solr/   
solr/bin/solr  create -c vertex_index -force -d conf/solr/