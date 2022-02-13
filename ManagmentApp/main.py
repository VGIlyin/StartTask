import boto3
import datetime


def create_alarm():
    session = boto3.session.Session()
    client = session.client(
    "cloudwatch",
    aws_access_key_id="vilyin:vilyin@cloud.croc.ru",
    aws_secret_access_key="ZPhuMX1iQE6bchSp0weifw",
    endpoint_url="https://api.cloud.croc.ru",
    region_name="croc"
)
    end = datetime.datetime.utcnow()
    start = end - datetime.timedelta(minutes=1)
    client.get_metric_data(period=60, namespace="AWS/EC2", start_time=start, end_time=end,
                                                dimensions={"InstanceId": "i-E7CB9C62"},
                                                metric_name="CPUUtilization", statistics=["Maximum"], unit="Percent")


if __name__ == "__main__":
    create_alarm()