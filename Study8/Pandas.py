#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


s =pd.Series([1,3,5, np.nan, 6 ,8])


# In[4]:


s


# In[5]:


dates = pd.date_range("20130101", periods=6)


# In[6]:


dates


# In[8]:


df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list("ABCD"))


# In[9]:


df


# In[10]:


df2 =pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)


# In[11]:


df2


# In[12]:


df2.dtypes


# In[14]:


df2.<TAB>  # noqa: E225, E999
df2.A                  df2.bool
df2.abs                df2.boxplot
df2.add                df2.C
df2.add_prefix         df2.clip
df2.add_suffix         df2.columns
df2.align              df2.copy
df2.all                df2.count
df2.any                df2.combine
df2.append             df2.D
df2.apply              df2.describe
df2.applymap           df2.diff
df2.B                  df2.duplicated


# In[15]:


df.head()


# In[16]:


df.tail(3)


# In[17]:


df.index


# In[18]:


df.columns


# In[20]:


df.to_numpy()


# In[21]:


df2.to_numpy()


# In[22]:


df.describe()


# In[23]:


df.T


# In[24]:


df.sort_index(axis=1, ascending=False)


# In[25]:


df.sort_values(by="B")


# In[26]:


df["A"]


# In[27]:


df[0:3]


# In[28]:


df["20130102":"20130104"]


# In[29]:


df.loc[dates[0]]


# In[30]:


df.loc[:, ["A", "B"]]


# In[31]:


df.loc["20130102":"20130104", ["A", "B"]]


# In[32]:


df.loc["20130102", ["A", "B"]]


# In[33]:


df.loc[dates[0], "A"]


# In[34]:


df.at[dates[0], "A"]


# In[35]:


df.iloc[3]


# In[36]:


df.iloc[3:5, 0:2]


# In[37]:


df.iloc[[1, 2, 4], [0, 2]]


# In[38]:


df.iloc[1:3, :]


# In[39]:


df.iloc[:, 1:3]


# In[40]:


df.iloc[1, 1]


# In[41]:


df.iat[1, 1]


# In[42]:


df[df["A"] > 0]


# In[43]:


df[df > 0]


# In[44]:


df2 = df.copy()


# In[45]:


df2["E"] = ["one", "one", "two", "three", "four", "three"]


# In[46]:


df2


# In[47]:


df2[df2["E"].isin(["two", "four"])]


# In[48]:


s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130102", periods=6))

 


# In[49]:


s1


# In[50]:


df["F"] = s1


# In[51]:


df.at[dates[0], "A"] = 0


# In[52]:


df.iat[0, 1] = 0


# In[53]:


df.loc[:, "D"] = np.array([5] * len(df))


# In[54]:


df


# In[55]:


df2 = df.copy()


# In[56]:


df2[df2 > 0] = -df2


# In[57]:


df2


# In[58]:


df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ["E"])


# In[59]:


df1.loc[dates[0] : dates[1], "E"] = 1


# In[60]:


df1


# In[61]:


df1.dropna(how="any")


# In[62]:


df1.fillna(value=5)


# In[63]:


pd.isna(df1)


# In[64]:


df.mean()


# In[65]:


df.mean(1)


# In[66]:


s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)


# In[67]:


s


# In[68]:


df.sub(s, axis="index")


# In[69]:


df.apply(np.cumsum)


# In[70]:


df.apply(lambda x: x.max() - x.min())


# In[71]:


s = pd.Series(np.random.randint(0, 7, size=10))


# In[72]:


s


# In[73]:


s.value_counts()


# In[74]:


s = pd.Series(["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"])


# In[75]:


s.str.lower()


# In[76]:


df = pd.DataFrame(np.random.randn(10, 4))


# In[77]:


df


# In[78]:


pieces = [df[:3], df[3:7], df[7:]]


# In[79]:


pd.concat(pieces)


# In[80]:


left = pd.DataFrame({"key": ["foo", "foo"], "lval": [1, 2]})


# In[81]:


right = pd.DataFrame({"key": ["foo", "foo"], "rval": [4, 5]})


# In[82]:


left


# In[83]:


right


# In[84]:


pd.merge(left, right, on="key")


# In[85]:


df = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
    }
)


# In[86]:


df


# In[87]:


df.groupby("A").sum()


# In[88]:


df.groupby(["A", "B"]).sum()


# In[89]:


tuples = list(
    zip(
        *[
            ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
            ["one", "two", "one", "two", "one", "two", "one", "two"],
        ]
    )
)


# In[90]:


index = pd.MultiIndex.from_tuples(tuples, names=["first", "second"])


# In[91]:


df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["A", "B"])


# In[92]:


df2 = df[:4]


# In[93]:


df2


# In[94]:


stacked = df2.stack()


# In[95]:


stacked


# In[96]:


stacked.unstack()


# In[97]:


stacked.unstack(1)


# In[99]:


stacked.unstack(0)


# In[100]:


df = pd.DataFrame(
    {
        "A": ["one", "one", "two", "three"] * 3,
        "B": ["A", "B", "C"] * 4,
        "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 2,
        "D": np.random.randn(12),
        "E": np.random.randn(12),
    }
)


# In[101]:


df


# In[102]:


pd.pivot_table(df, values="D", index=["A", "B"], columns=["C"])


# In[103]:


rng = pd.date_range("1/1/2012", periods=100, freq="S")


# In[104]:


ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)


# In[105]:


ts.resample("5Min").sum()


# In[106]:


rng = pd.date_range("3/6/2012 00:00", periods=5, freq="D")


# In[107]:


ts = pd.Series(np.random.randn(len(rng)), rng)


# In[108]:


ts


# In[109]:


ts_utc = ts.tz_localize("UTC")


# In[110]:


ts_utc


# In[111]:


ts_utc.tz_convert("US/Eastern")


# In[112]:


rng = pd.date_range("1/1/2012", periods=5, freq="M")


# In[113]:


ts = pd.Series(np.random.randn(len(rng)), index=rng)


# In[114]:


ts


# In[115]:


ps = ts.to_period()


# In[116]:


ps


# In[117]:


ps.to_timestamp()


# In[118]:


prng = pd.period_range("1990Q1", "2000Q4", freq="Q-NOV")


# In[119]:


s = pd.Series(np.random.randn(len(prng)), prng)


# In[121]:


ts.index = (prng.asfreq("M", "e") + 1).asfreq("H", "s") + 9


# In[122]:


ts.head()


# In[123]:


df = pd.DataFrame(
    {"id": [1, 2, 3, 4, 5, 6], "raw_grade": ["a", "b", "b", "a", "a", "e"]}
)


# In[124]:



df["grade"] = df["raw_grade"].astype("category")


# In[125]:


df["grade"]


# In[126]:


df["grade"].cat.categories = ["very good", "good", "very bad"]


# In[127]:


df["grade"] = df["grade"].cat.set_categories(
    ["very bad", "bad", "medium", "good", "very good"]
)


# In[128]:


df["grade"]


# In[129]:


df.sort_values(by="grade")


# In[130]:


df.groupby("grade").size()


# In[131]:


import matplotlib.pyplot as plt


# In[132]:


plt.close("all")


# In[133]:


ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))


# In[134]:


ts = ts.cumsum()


# In[135]:


ts.plot();


# In[136]:


df = pd.DataFrame(
    np.random.randn(1000, 4), index=ts.index, columns=["A", "B", "C", "D"]
)


# In[137]:


df = df.cumsum()


# In[138]:


plt.figure();


# In[143]:


df.plot();


# In[144]:


df.to_csv("foo.csv")


# In[145]:


pd.read_csv("foo.csv")


# In[ ]:




