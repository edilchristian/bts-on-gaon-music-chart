import streamlit as st
import pandas as pd
import plotly.express as px



header=st.container()
yearend=st.container()
bwl=st.container()
mots7=st.container()


data=pd.read_csv('data/motsgaon.csv')
data2=pd.read_csv('data/gaon2020mots7.csv')

with header:
	st.title("BTS on South Korean Music Chart 2020 ")
	st.markdown("South Korea is the world's 6th biggest music market(IFPI). Gaon is the company that collects and publishes weekly music charts. Map Of The Soul: 7, released on Feb 21, 2020 was the best-selling album worldwide in 2020 and also on Gaon Music Charts.")
	
with yearend:
	st.header("Year End Performance")
	fig = px.scatter(data, x="rank",y="streams",color="song", labels={
                     "rank": "year end rank",
                     "streams": "streams in millions",
                 },title="Year End Rank of songs from the album Map Of The Soul :7 on Gaon Music Chart 2020")
	fig['layout']['yaxis']['autorange'] = "reversed"
	st.plotly_chart(fig)

	st.markdown("All the 14 new songs on the album landed on the Gaon 2020 Year End Chart, hence proving exceptional performance of all the songs. 'ON', the title song, landed at #20 and was the best performing song on the album with over 560 million digital index. ")

with bwl:

	st.header("Boy With Luv weekly analysis")
	fig2 = px.line(data2, x="week",y="boy_with_luv", labels={"week": "week # of 2020", "boy_with_luv": "rank on Gaon Weekly Chart"}, title="Boy With Luv on Gaon Weekly Chart")
	fig2['layout']['yaxis']['autorange'] = "reversed"
	fig2['data'][0]['line']['color']="#ff1493"
	st.plotly_chart(fig2)

	st.markdown("Boy With Luv, another of BTS' biggest hits, released in April 2019, was probably the most consistent song of the year, as it charted for every week of 2020. It never left the top 100 rank throughout the year.")

with mots7:
	st.header("weekly analysis of Map Of The Soul: 7 songs")
	song=st.selectbox("choose song from the dropdown below", options=["Zero O Clock","On","Inner Child", "Louder Than Bombs", "Moon","Filter","Ugh!","Black Swan","Friends","Ego","Shadow","Respect","My Time", "We Are Bulletproof: The Eternal"])

	
	if song == "Zero O Clock":
		zoc = px.line(data2, x="week",y="zero_o_clock",labels={"week": "week # of 2020", "zero_o_clock": "rank on Gaon Weekly Chart"}, title="Zero O Clock on Gaon Weekly Chart")
		zoc['layout']['yaxis']['autorange'] = "reversed"
		zoc['data'][0]['line']['color']="#ffe100"
		st.plotly_chart(zoc)

	if song == "Inner Child":
		innerc = px.line(data2, x="week",y="inner_child", labels={"week": "week # of 2020", "inner_child": "rank on Gaon Weekly Chart"}, title="Inner Child on Gaon Weekly Chart")
		innerc['layout']['yaxis']['autorange'] = "reversed"
		innerc['data'][0]['line']['color']="#741aec"
		st.plotly_chart(innerc)

	
	if song == "On":
		on= px.line(data2, x="week",y="on", labels={"week": "week # of 2020", "on": "rank on Gaon Weekly Chart"}, title="On on Gaon Weekly Chart")
		on['layout']['yaxis']['autorange'] = "reversed"
		on['data'][0]['line']['color']="#ffffff"
		st.plotly_chart(on)
	if song == "Ugh!":
		ugh = px.line(data2, x="week",y="ugh",labels={"week": "week # of 2020", "ugh": "rank on Gaon Weekly Chart"},title="UGH! on Gaon Weekly Chart")
		ugh['layout']['yaxis']['autorange'] = "reversed"
		ugh['data'][0]['line']['color']="#c6d408"
		st.plotly_chart(ugh)

	if song == "Moon":
		moon = px.line(data2, x="week",y="moon",labels={"week": "week # of 2020", "moon": "rank on Gaon Weekly Chart"}, title="Moon on Gaon Weekly Chart")
		moon['layout']['yaxis']['autorange'] = "reversed"
		moon['data'][0]['line']['color']="#ff1fd6"
		st.plotly_chart(moon)

	if song == "Filter":
		filt = px.line(data2, x="week",y="filter",labels={"week": "week # of 2020", "filter": "rank on Gaon Weekly Chart"}, title="Filter on Gaon Weekly Chart")
		filt['layout']['yaxis']['autorange'] = "reversed"
		filt['data'][0]['line']['color']="#ff0000"
		st.plotly_chart(filt)

	if song == "We Are Bulletproof: The Eternal":
		eternal = px.line(data2, x="week",y="eternal",labels={"week": "week # of 2020", "eternal": "rank on Gaon Weekly Chart"}, title="We Are Bulletproof: The Eternal on Gaon Weekly Chart")
		eternal['layout']['yaxis']['autorange'] = "reversed"
		eternal['data'][0]['line']['color']="#4b212e"
		st.plotly_chart(eternal)

	if song == "Black Swan":
		bs = px.line(data2, x="week",y="black_swan",labels={"week": "week # of 2020", "black_swan": "rank on Gaon Weekly Chart"}, title="Black Swan on Gaon Weekly Chart")
		bs['layout']['yaxis']['autorange'] = "reversed"
		bs['data'][0]['line']['color']="#2d0045"
		st.plotly_chart(bs)

	if song == "Louder Than Bombs":
		ltb = px.line(data2, x="week",y="louder_than_bombs",labels={"week": "week # of 2020", "louder_than_bombs": "rank on Gaon Weekly Chart"}, title="Louder Than Bombs on Gaon Weekly Chart")
		ltb['layout']['yaxis']['autorange'] = "reversed"
		ltb['data'][0]['line']['color']="#c32b45"
		st.plotly_chart(ltb)

	if song == "My Time":
		mytime = px.line(data2, x="week",y="my_time",labels={"week": "week # of 2020", "my_time": "rank on Gaon Weekly Chart"}, title="My Time on Gaon Weekly Chart")
		mytime['layout']['yaxis']['autorange'] = "reversed"
		mytime['data'][0]['line']['color']="#656839"
		st.plotly_chart(mytime)
	if song == "Friends":
		frnds = px.line(data2, x="week",y="friends",labels={"week": "week # of 2020", "friends": "rank on Gaon Weekly Chart"}, title="Friends on Gaon Weekly Chart")
		frnds['layout']['yaxis']['autorange'] = "reversed"
		frnds['data'][0]['line']['color']="#355d5f"
		st.plotly_chart(frnds)
	if song == "Shadow":
		shad = px.line(data2, x="week",y="shadow",labels={"week": "week # of 2020", "shadow": "rank on Gaon Weekly Chart"}, title="Shadow on Gaon Weekly Chart")
		shad['layout']['yaxis']['autorange'] = "reversed"
		shad['data'][0]['line']['color']="#ff5900"
		st.plotly_chart(shad)
	if song == "Ego":
		ego = px.line(data2, x="week",y="ego",labels={"week": "week # of 2020", "ego": "rank on Gaon Weekly Chart"}, title="Ego on Gaon Weekly Chart")
		ego['layout']['yaxis']['autorange'] = "reversed"
		ego['data'][0]['line']['color']="#02334a"
		st.plotly_chart(ego)

	if song == "Respect":
		resp = px.line(data2, x="week",y="respect",labels={"week": "week # of 2020", "respect": "rank on Gaon Weekly Chart"}, title="Respect on Gaon Weekly Chart")
		resp['layout']['yaxis']['autorange'] = "reversed"
		resp['data'][0]['line']['color']="#0e7bcf"
		st.plotly_chart(resp)








