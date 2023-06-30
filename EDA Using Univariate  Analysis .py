#!/usr/bin/env python
# coding: utf-8

# # Exploratory Data Analysis

# Univariate, Bivariate, and Multivariate Analysis Techniques

# # Univariate Analysis

# Uni means one and variate means variable, so in univariate analysis, there is only one dependable variable. The objective of univariate analysis is to derive the data, define and summarize it, and analyze the pattern present in it. In a dataset, it explores each variable separately. It is possible for two kinds of variables- Categorical and Numerical.

# In[4]:


import pandas as pd
import seaborn as sns


# In[2]:


df=pd.read_csv('train.csv')


# In[3]:


df.head()


# # Categorical Data

# 1. CountPlot

# In[5]:


sns.countplot(df['Survived'])


# In[7]:


sns.countplot(df['Survived'])
df['Survived'].value_counts().plot(kind='bar')


# In[8]:


sns.countplot(df['Embarked'])
#df['Survived'].value_counts().plot(kind='bar')


# 2. Piechart

# In[9]:


df['Sex'].value_counts().plot(kind='pie',autopct='%.2f')


# # Numerical Data

# 1. Histogram

# In[10]:


import matplotlib.pyplot as plt
plt.hist(df['Age'],bins=5)


# 2.Distplot

# In[11]:


sns.distplot(df['Age'])


# 3.Boxplot

# In[12]:


sns.boxplot(df['Age'])


# In[13]:


df['Age'].min()


# In[14]:


df['Age'].max()


# In[15]:


df['Age'].mean()


# In[16]:


df['Age'].skew()


# In[ ]:




