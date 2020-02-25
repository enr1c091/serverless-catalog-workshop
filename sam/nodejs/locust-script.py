from locust import TaskSet, task, HttpLocust, between

class ConverterTasks(TaskSet):
    @task
    def day_to_hour(self):
        self.client.get('items/')
# Receives the URL from CloudFormation output variable containing "/" as last character so omit it as first char 

#    @task
#    def day_to_minute(self):
#        self.client.get('items/1')

class ApiUser(HttpLocust):
    task_set = ConverterTasks
    wait_time = between(1,3)

#locust -f locust-script.py -H https://iz2j9tfy6c.execute-api.us-east-1.amazonaws.com/Prod --no-web -c 1000 -r 100 --run-time 1m