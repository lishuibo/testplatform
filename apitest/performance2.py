__author__ = 'Administrator'
from locust import HttpLocust, TaskSet, task


class WebsiteTasks(TaskSet):
    @task
    def index(self):
        self.client.post('/test', {'username': 'admin', 'password': 'test123456'})


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 100
    max_wait = 1000