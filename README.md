# BEERTASTE
Website that let's me or user to keep own reviews to check what they had drunk and what it taste like.

---

## SETUP
###NOT WORKING. YOU CANT USE SWARM AND SECRETS ON COMPOSE!
We need to have swarm in docker before we can create secrets there.

Check from settings.py has DEBUG false when you don't change thinks.

There is few things that need to be done before runnning docker.
-	We need to create SECRET_KEY for django
-	We need to create DATABAE_PASS for django and maria

```
docker secret create name value/file
```

```
printf "text" | docker secret create name -
```
Might be good idea use printf or echo.

You can find secrets to use environments in /run/secrets/
We need to create "django_secret_key" and "maria_pass"

## SHOULD KNOW THINKGS
You need to install are bin and lib for building C-code and python librarys.
You should know how services and rights have been divided by different apps/services.
