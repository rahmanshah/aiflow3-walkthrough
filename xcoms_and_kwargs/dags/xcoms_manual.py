from airflow.decorators import dag, task

@dag
def xcoms_manual():

    @task.python
    def fetch_data(ti):
        # Simulate fetching data from an external source/api
        data = {"name": "Airflow", "version": "3.0"}
        return data

        # Push the data to XCom
        ti.xcom_push(key="fetched_data", value=data)

    