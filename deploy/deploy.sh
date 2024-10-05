echo "deploy code to aws"
aws s3 cp ../../datalake-retail-analytics/ s3://dlk-code-glue-code1042024/ --recursive

