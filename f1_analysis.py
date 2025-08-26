import pandas as pd
import plotly.express as px
import plotly.io as pio

# ==== DATA ====
data = {
    "Pos": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
    "Driver": ["Norris","Leclerc","Piastri","Hamilton","Verstappen","Hadjar","Alonso","Ocon",
               "Lawson","Albon","Sainz","Tsunoda","Hulkenberg","Russell","Antonelli",
               "Bortoleto","Bearman","Gasly","Stroll","Colapinto"],
    "Team": ["McLaren","Ferrari","McLaren","Ferrari","Red Bull","Racing Bulls","Aston Martin","Haas",
             "Racing Bulls","Williams","Williams","Red Bull","Kick Sauber","Mercedes","Mercedes",
             "Kick Sauber","Haas","Alpine","Aston Martin","Alpine"],
    "Gap": [0,0.109,0.175,0.428,0.715,0.969,0.970,0.988,1.175,1.259,1.408,1.461,1.642,
            None,None,1.948,2.025,2.040,2.609,2.643],
    "AvgSpeed": [171.730,171.463,171.301,170.686,169.993,169.384,169.381,169.338,168.893,
                 168.694,168.342,168.217,167.791,None,None,167.077,166.899,166.864,165.555,165.478]
}
df = pd.DataFrame(data)

# ==== TEAM COLORS ====
team_colors = {
    "McLaren": "#FF8000",
    "Ferrari": "#DC0000",
    "Red Bull": "#1E41FF",
    "Racing Bulls": "#6692FF",
    "Aston Martin": "#006F62",
    "Haas": "#B6BABD",
    "Williams": "#005AFF",
    "Kick Sauber": "#52E252",
    "Mercedes": "#00D2BE",
    "Alpine": "#0090FF"
}
df["Color"] = df["Team"].map(team_colors)

# ==== 1. LAP DELTA ====
fig1 = px.bar(
    df.sort_values("Gap", na_position="last"),
    x="Gap", y="Driver", orientation="h",
    color="Team", text="Gap",
    color_discrete_map=team_colors,
    title="Monaco 2025 - Qualification Lap Delta"
)
fig1.update_layout(
    template="plotly_dark",
    plot_bgcolor="black",
    paper_bgcolor="black",
    yaxis=dict(title="Driver", autorange="reversed"),
    xaxis=dict(title="Gap (s)")
)
fig1.update_traces(texttemplate="%{text:.3f}", textposition="outside")

# ==== 2. AVERAGE SPEED COMPARISON ====
fig2 = px.bar(
    df, x="Driver", y="AvgSpeed",
    color="Team", text="AvgSpeed",
    color_discrete_map=team_colors,
    title="Monaco 2025 - Average Speed Comparison"
)
fig2.update_layout(template="plotly_dark", plot_bgcolor="black", paper_bgcolor="black")
fig2.update_traces(texttemplate="%{text:.1f}", textposition="outside")

# ==== 3. QUALI SPREAD ====
fig3 = px.scatter(
    df, x="Driver", y="Gap", color="Team",
    color_discrete_map=team_colors,
    title="Monaco 2025 - Qualification Spread (Gap vs Pole)"
)
fig3.update_layout(template="plotly_dark", plot_bgcolor="black", paper_bgcolor="black")


# ==== EXPORT HTML ====
fig1.write_html("f1_lap_delta.html", auto_open=True)
fig2.write_html("f1_avg_speed.html", auto_open=True)
fig3.write_html("f1_quali_spread.html", auto_open=True)
