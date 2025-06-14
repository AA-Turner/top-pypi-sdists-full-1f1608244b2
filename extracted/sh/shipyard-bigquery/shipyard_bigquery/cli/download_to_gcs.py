import argparse
import sys
import os

from shipyard_bigquery import BigQueryClient
from shipyard_bigquery.utils.exceptions import DownloadToGcsError
from shipyard_templates import ShipyardLogger, ExitCodeException
import shipyard_bp_utils as shipyard
from shipyard_bigquery.utils.creds import get_credentials

logger = ShipyardLogger.get_logger()


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", dest="query", required=True)
    parser.add_argument("--service-account", dest="service_account", required=False)
    parser.add_argument("--project-id", dest="project_id", required=False)
    parser.add_argument("--location", dest="location", required=False)
    parser.add_argument("--bucket-name", dest="bucket_name", required=True)
    parser.add_argument(
        "--destination-file-name",
        dest="destination_file_name",
        default="output.csv",
        required=True,
    )
    parser.add_argument(
        "--destination-folder-name",
        dest="destination_folder_name",
        default="",
        required=False,
    )
    return parser.parse_args()


def main():
    try:
        args = get_args()
        creds = get_credentials()
        if args.project_id:
            creds["project_id"] = args.project_id
        if args.location:
            creds["location"] = args.location
        destination_file_name = args.destination_file_name
        target_folder = args.destination_folder_name or os.getcwd()
        target_path = shipyard.files.combine_folder_and_file_name(
            folder_name=target_folder, file_name=destination_file_name
        )
        client = BigQueryClient(**creds)
        logger.info("Successfully connected to BigQuery")
        logger.debug(f"Service account email is {client.email}")

        logger.info("Beginning job to store query results in GCS")
        client.download_to_gcs(
            query=args.query, bucket_name=args.bucket_name, path=target_path
        )
    except (ExitCodeException, DownloadToGcsError) as ec:
        logger.error(ec.message)
        sys.exit(ec.exit_code)
    except Exception as e:
        logger.error(f"An error occurred in downloading query results to GCS: {str(e)}")
        sys.exit(BigQueryClient.EXIT_CODE_NO_RESULTS)
    else:
        logger.info("Successfully stored query results in GCS")


if __name__ == "__main__":
    main()
