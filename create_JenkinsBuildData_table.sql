set character set utf8; 

CREATE DATABASE IF NOT EXISTS test;

USE test;

create table JenkinsBuildData(
   build_num_api int not null,
   build_result varchar(10) not null,
   trigger_reason varchar(100) not null,
   build_time datetime not null,
   build_url varchar(120) not null,
   build_duration int not null,
   grabdata_time datetime not null,
   version_num varchar(40) not null,
   test_part_name varchar(40) not null,
   test_total_count int not null,
   test_fail_count int not null,
   test_pass_count int not null,
   build_num_wfapi int not null,
   alloctopo_result varchar(12) not null,
   alloctopo_duration int not null,
   deploy_result varchar(12) not null,
   deploy_duration int not null,
   test_result varchar(12) not null,
   test_duration int not null,
   PRIMARY KEY (build_num_api,test_part_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


--build_num_api,build_result,trigger_reason,build_time,build_url,build_duration,grabdata_time,version_num,test_part_name,test_total_count,test_fail_count,test_pass_count,build_num_wfapi,alloctopo_result,alloctopo_duration,deploy_result,deploy_duration,test_result,test_duration
