from airflow.decorators import dag, task

@dag(dag_id="first_dag")
def first_dag():

    @task.python(task_id="first_task")
    def first_task():
        print("Hello from the first task!")

    @task.python(task_id="second_task")
    def second_task():
        print("Hello from the second task!")

    
    t1 = first_task()
    t2 = second_task()

    t1 >> t2


first_dag_instance = first_dag()