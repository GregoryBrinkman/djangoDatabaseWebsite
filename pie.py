from django.contrib.auth.models import User
user = User.objects.create_user(username='user',
                                 email='',
                                 password='cs430@SIUC')
