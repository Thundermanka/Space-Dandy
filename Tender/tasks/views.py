from django.shortcuts import render

# Create your views here.
def publish(self):
    self.published_date = timezone.now()
    self.save()

def Event(self):
    return self.task_title

def list_tasks(self):
	return self.task_text

def new_link(self):
	return self.task_text