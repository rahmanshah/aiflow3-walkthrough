from airflow.decorators import dag, task

@dag
def xcoms_manual():

    @task.python(task_id="task1")
    def fetch_data(ti):
        # Simulate fetching data from an external source/api
        data = {"name": "Airflow", "version": "3.0"}
        return data

        # Push the data to XCom
        ti.xcom_push(key="fetched_data", value=data)

    @task.python(task_id="task2")
    def process_data(ti):
        # Pull the data from XCom
        pulled_data = ti.xcom_pull(key="fetched_data", task_ids="task1")
        # simulate processing the data
        processed_data = f"Processed {pulled_data['name']} version {pulled_data['version']}"
        print(processed_data)
