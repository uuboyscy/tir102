
CREATE OR REPLACE EXTERNAL TABLE `tir102_demo.SalePartitionExternal`
WITH PARTITION COLUMNS
OPTIONS (
  format = 'CSV',
  uris = ['gs://tir102-allen-demo/demo_partition/*/sale.csv'],
  hive_partition_uri_prefix = 'gs://tir102-allen-demo/demo_partition',
  skip_leading_rows = 1,
  max_bad_records = 1
);


CREATE OR REPLACE EXTERNAL TABLE `tir102_demo.SalePartitionExternal`
(
  TransactionID STRING,
  ProductID STRING,
  Quantity INT64,
  SaleDate DATE,
)
WITH PARTITION COLUMNS
OPTIONS (
  format = 'CSV',
  uris = ['gs://tir102-allen-demo/demo_partition/*'],
  hive_partition_uri_prefix = 'gs://tir102-allen-demo/demo_partition',
  skip_leading_rows = 1,
  max_bad_records = 1
);
