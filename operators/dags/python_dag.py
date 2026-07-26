from airflow.decorators import dag, task
from airflow.operators.python import PythonOperator

def third_task():
    return "Hello from the third task!"

@dag(dag_id="python_dag")
def python_dag():
    @task.python(task_id="first_task")     # new appoach
    def first_task():
        return "Hello from the first task!"

    second_task = PythonOperator(
        task_id="second_task",
        python_callable=lambda: "Hello from the second task!"
    )

    third_task = PythonOperator(
        task_id="third_task",
        python_callable=lambda: "Hello from the third task!"
    )

    t1 = first_task()
    t2 = second_task()
    t3 = third_task()

    t1 >> t2 >> t3

python_dag_instance = python_dag()