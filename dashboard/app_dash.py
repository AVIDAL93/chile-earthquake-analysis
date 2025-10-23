import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# === Data ===
df = pd.read_csv("/content/seismic_data.csv")

# === App ===
app = dash.Dash(__name__, title="Chile Earthquake Dashboard")

# === Figures ===
fig_map = px.scatter_mapbox(
    df,
    lat="Latitude",
    lon="Longitude",
    color="Magnitude",
    size="Magnitude",
    hover_name="Date(UTC)",
    hover_data={"Depth": True, "Latitude": False, "Longitude": False},
    color_continuous_scale="Inferno",
    zoom=3,
    height=600,
    title="Distribución Geográfica de Sismos en Chile (2012–2025)"
)
fig_map.update_layout(mapbox_style="carto-positron")

fig_trend = px.line(
    df.groupby(pd.to_datetime(df['Date(UTC)']).dt.year)['Magnitude'].mean().reset_index(),
    x="Date(UTC)",
    y="Magnitude",
    markers=True,
    title="Evolución Anual de la Magnitud Promedio"
)
fig_trend.update_traces(line_color="orange", line_width=3)

# === Layout ===
app.layout = html.Div([
    html.H1("🌎 Chile Earthquake Analysis", style={"textAlign": "center"}),
    html.P("Visualización interactiva de patrones sísmicos en Chile — IBM Data Science Capstone",
           style={"textAlign": "center"}),
    html.Hr(),
    dcc.Graph(figure=fig_map),
    dcc.Graph(figure=fig_trend),
    html.Footer("Autor: Angello Vidal | 2025", style={"textAlign": "center", "padding": "20px"})
])

if __name__ == "__main__":
    app.run(debug=True)
