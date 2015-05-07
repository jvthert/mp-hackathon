import sys, os

sys.path.append('/var/www/hackathon')
os.environ["URL_PREFIX"] = "/"

from hackathon.mphackathon import app as application