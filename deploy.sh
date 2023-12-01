# deploy.sh

# Update the environment
railway run python manage.py migrate

# Collect static files
railway run python manage.py collectstatic --noinput

# Restart the Gunicorn server
railway restart
