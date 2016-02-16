from django.db import models


class Submission(models.Model):
    '''
    A submission to be graded asynchronously.
    '''
    queue_time = models.DateTimeField(auto_now_add=True, db_index=True)
    course_key = models.CharField(max_length=64)
    exercise_key = models.CharField(max_length=128)
    language = models.CharField(max_length=5)
    submission_url = models.CharField(max_length=256)
    submission_dir = models.CharField(max_length=256)
    worker_host = models.CharField(max_length=64, db_index=True)
    worker_time = models.DateTimeField(blank=True)
    feedback_time = models.DateTimeField(blank=True, db_index=True)

    class META:
        ordering = ['queue_time']
