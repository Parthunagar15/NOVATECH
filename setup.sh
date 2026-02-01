#!/usr/bin/env bash
# ============================================================
# NovaTech — One-command setup & run
# ============================================================
# Usage:  bash setup.sh
# ============================================================

set -e

echo "=================================================="
echo "  NovaTech — Django Project Setup"
echo "=================================================="
echo ""

# ── 1. Create & activate virtual environment ────────────────
if [ ! -d "venv" ]; then
  echo "▶ Creating virtual environment..."
  python3 -m venv venv
fi

# Activate (works on Linux / macOS)
source venv/bin/activate 2>/dev/null || source venv/Scripts/activate 2>/dev/null

# ── 2. Install dependencies ─────────────────────────────────
echo "▶ Installing dependencies..."
pip install -q django

# ── 3. Run migrations (creates db.sqlite3) ──────────────────
echo "▶ Running migrations..."
python manage.py migrate

# ── 4. Create superuser (optional, for /admin/) ────────────
echo ""
echo "▶ Would you like to create a Django admin superuser? (y/n)"
read -r answer
if [ "$answer" = "y" ] || [ "$answer" = "Y" ]; then
  python manage.py createsuperuser
fi

# ── 5. Start development server ─────────────────────────────
echo ""
echo "=================================================="
echo "  ✓ Setup complete!"
echo "  ▶ Starting server at http://127.0.0.1:8000"
echo "=================================================="
echo ""
python manage.py runserver
