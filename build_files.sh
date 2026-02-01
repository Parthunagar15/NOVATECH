# build_files.sh

# 1. Install dependencies using the --break-system-packages flag
# This bypasses the externally-managed-environment error on Vercel
pip install -r requirements.txt --break-system-packages

# 2. Collect static files
# Ensure the directory matches your settings.py STATIC_ROOT
python3 manage.py collectstatic --noinput

# 3. Run migrations
python3 manage.py migrate