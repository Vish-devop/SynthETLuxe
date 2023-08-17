from etl_tester import ETLTester

if __name__ == '__main__':
    num_records=10
    etl_tester=ETLTester(num_records)
    etl_tester.run_etl()