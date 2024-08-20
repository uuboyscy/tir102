CREATE TABLE
  demo.test_time_unit_column (transaction_id INT64, transaction_date DATE)
PARTITION BY
  transaction_date
  OPTIONS (
    partition_expiration_days = 3,
    require_partition_filter = TRUE);
