from airflow.decorators import dag, task
from airflow.operators.bash import BashOperator

@dag(dag_id="bash_dag")
def bash_dag():
    @task.bash(task_id="first_task")     # new appoach
    def first_task():
        return "echo 'Hello from the first task!'"

    second_task = BashOperator(
        task_id="second_task",
        bash_command="echo 'Hello from the second task!'"
    )

    
    t1 = first_task()
    t2 = second_task()

    t1 >> t2

bash_dag_instance = bash_dag()