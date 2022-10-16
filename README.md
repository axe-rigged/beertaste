# BEERTASTE
Website that let's me or user to keep own reviews to check what they had drunk and what it taste like.

---

## SETUP
There is few things that need to be done before runnning docker.
-	We need to create SECRET_KEY for django
-	We need to create DATABAE_PASS for django and maria

...
docker secret create <name> <value>
...

Might be good idea use printf or echo.

You can find secrets to use environments in /run/secrets/
We need to create "django_secret_key" and "maria_pass"
