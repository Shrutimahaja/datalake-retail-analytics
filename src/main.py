import sys
import yaml
from awsglue.utils import getResolvedOptions
from jobs.glue_job import run_glue_job  # Importing the function from glue_job.py

def main():
    # Load configuration
    with open('config/config.yaml', 'r') as file:
        config = yaml.safe_load(file)
        print("this is test")

    # Get job arguments
    args = getResolvedOptions(sys.argv, ['JOB_NAME'])

    # Run the Glue job with configuration and arguments
    run_glue_job(args['JOB_NAME'], config)

if __name__ == "__main__":
    main()



