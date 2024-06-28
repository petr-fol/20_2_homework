from django.contrib.auth.models import User, Group

# Получите пользователя
user = User.objects.get(username='username')

# Проверьте, в какой группе он находится
for group in user.groups.all():
    print(group.name)

# Проверьте, есть ли у него нужные права
if user.has_perm('app_name.permission_codename'):
    print("У пользователя есть права")
else:
    print("У пользователя нет прав")
