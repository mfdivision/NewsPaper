#Команды для shell

from news.models import *

#Создать двух пользователей (с помощью метода User.objects.create_user('username')).

u1 = User.objects.create(username = "First")
u2 = User.objects.create(username = "Second")

#Создать два объекта модели Author, связанные с пользователями.

a1 = Author.objects.create(user = u1)
a2 = Author.objects.create(user = u2)

#Добавить 4 категории в модель Category.

cat1 = Category.objects.create(cat_name="Cat1")
cat2 = Category.objects.create(cat_name="Cat2")
cat3 = Category.objects.create(cat_name="Cat3")
cat4 = Category.objects.create(cat_name="Cat4")

#Добавить 2 статьи и 1 новость.

p1=Post.objects.create(name="1 from First user", text=";jwfjkwefojwreijwer", author=a1, post_type=Post.POSTS)
p2=Post.objects.create(name="2 from First user", text=";jwfjkwefojwreijwer", author=a1, post_type=Post.POSTS)
p3=Post.objects.create(name="3 from First user", text=";jwfjkwefojwreijwer", author=a1, post_type=Post.NEWS)
p4=Post.objects.create(name="4 from First user", text=";jwfjkwefojwreijwer", author=a1, post_type=Post.NEWS)

p5=Post.objects.create(name="1 from Second user", text=";jwfjkwefojwreijwer", author=a2, post_type=Post.NEWS)
p6=Post.objects.create(name="2 from Second user", text=";jwfjkwefojwreijwer", author=a2, post_type=Post.POSTS)
p7=Post.objects.create(name="3 from Second user", text=";jwfjkwefojwreijwer", author=a2, post_type=Post.POSTS)
p8=Post.objects.create(name="4 from Second user", text=";jwfjkwefojwreijwer", author=a2, post_type=Post.NEWS)

#Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).

p1=Post.objects.get(pk=1)
p1.post_categories.set("1")
p1.post_categories.set("3")


#Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).
c1 = Comments.objects.create(comment="1 comment from First", post=p5, user=u1)
c2 = Comments.objects.create(comment="2 comment from First", post=p6, user=u1)
c3 = Comments.objects.create(comment="1 comment from Second", post=p1, user=u2)
c4 = Comments.objects.create(comment="2 comment from Second", post=p2, user=u2)

#Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.

c1 = Comments.objects.get(pk=1)

c1.comment_like()
c1.comment_like()
c1.comment_like()
c1.comment_like()
c1.comment_dislike()

p1.post_like()
p1.post_like()
p1.post_like()
p1.post_like()
p1.post_like()

c2 = Comments.objects.get(pk=3)

c2.comment_like()
c2.comment_like()
c2.comment_dislike()

#Обновить рейтинги пользователей.

a1=Author.objects.get(pk=1)
a2=Author.objects.get(pk=2)
a1.update_rating()
a2.update_rating()

#Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).

s=Author.objects.order_by("-author_rate").first().id
user=User.objects.get(pk=s).username
rate=Author.objects.order_by("-author_rate").first().author_rate
print(user, rate)

#Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.

post=Post.objects.order_by("-post_rate")
post.first().post_date
author=post.first().author_id
User.objects.get(pk=author).username
post.first().post_rate
post.first().name
post.first().preview()

#Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
com=post.first().id
comments=Comments.objects.filter(post_id=com)
comments.values("comment","comment_date","comment_rate", "user_id")
