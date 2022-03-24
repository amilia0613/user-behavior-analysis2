from flask import Flask, render_template
import time
import datetime
import re
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from io import BytesIO
import base64

app = Flask(__name__)

#Objective 1: User and Session Identification
weblog_path = os.path.join("weblog.csv")
weblog = pd.read_csv(weblog_path)

weblog['date'] = weblog['datetime'].str.slice(0, 2)

weblog['request'] = weblog['request'].str.slice(10, )

main = weblog[weblog['request'] == '']
main["page_category"] = "main_page"

landing_page = weblog[weblog['request'].str.contains('landing_page')==True]
landing_page["page_category"] = "landing_page"

signup = weblog[weblog['request'].str.contains('signup')==True]
signup["page_category"] = "sign_up"

login = weblog[weblog['request'].str.contains('login')==True]
login["page_category"] = "login"

dashboard = weblog[weblog['request'].str.contains('dashboard')==True]
dashboard["page_category"] = "dashboard"

scoreboard = weblog[weblog['request'].str.contains('scoreboard')==True]
scoreboard["page_category"] = "scoreboard"

profile = weblog[weblog['request'].str.contains('profile')==True]
profile["page_category"] = "profile"

available_rewards = weblog[weblog['request'].str.contains('available_rewards')==True]
available_rewards["page_category"] = "available_rewards"

faq = weblog[weblog['request'].str.contains('faq')==True]
faq["page_category"] = "faq"

contact_us = weblog[weblog['request'].str.contains('contact_us')==True]
contact_us["page_category"] = "contact_us"

logout = weblog[weblog['request'].str.contains('logout')==True]
logout["page_category"] = "logout"

quiz = weblog[weblog['request'].str.contains('quiz')==True]
quiz["page_category"] = "quiz"

weblog_df = pd.concat([main, landing_page, signup, login, dashboard, scoreboard, profile, available_rewards, faq, contact_us, logout, quiz])

weblog_df = weblog_df.sort_values('datetime')

weblog_df['user'].nunique()
weblog_df['page_category'].nunique()

path = 'weblog_df.csv'

with open(path, 'w', encoding = 'utf-8-sig') as f:
  weblog_df.to_csv(f)

@app.route("/")
# This fuction for rendering the table
def index():
    #Statistics
    stats = {
        'num_of_users': weblog_df['user'].nunique(),
        'num_of_pages': weblog_df['page_category'].nunique(),
        'rev_table': asc_df. \
            head(10).reset_index().to_html(
            classes=['table thead-light table-striped table-bordered table-hover table-sm'])
    }
# Tambahkan hasil result plot pada fungsi render_template()
    return render_template('index.html', stats=stats)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
