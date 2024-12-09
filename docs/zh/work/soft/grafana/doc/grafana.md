https://grafana.com/grafana/download



https://gitee.com/derek2468/grafana-dashboards




nohup bin/grafana-server &




SELECT 
  date_format(sync_date,'%Y-%m-%d'),
	STR_TO_DATE(date_format(sync_date,'%Y-%m-%d'),'%Y-%m-%d'),
  count(1) as value,
  sync_reason
FROM cs.t_sync_history
GROUP BY 
  sync_reason,
  date_format(sync_date,'%Y-%m-%d')