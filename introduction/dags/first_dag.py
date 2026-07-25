from airflow.sdk import dag, task

@dag
def first_dag():

    @task
    def first_task():
        print("Hello from the first task!")

    @task
    def second_task():
        print("Hello from the second task!")