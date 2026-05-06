from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Load data from Google Drive
DATA_URL = "https://drive.google.com/uc?id=1XX_gytNXjcaj0jeERfpYlaMcZg7x91pK"
df = pd.read_csv(DATA_URL)

# Initialize app
app = Dash(__name__)
server = app.server
app.title = "Student Behavior Dashboard"

# Features to use
features = [
    "total_clicks",
    "active_days",
    "avg_assessment_score",
    "assessment_count"
]

# Layout
app.layout = html.Div([
    
    html.H1("Student Behavior Clustering Dashboard", style={
        "textAlign": "center",
        "color": "#2c3e50"
    }),

    # Dropdown
    html.Div([
        html.Label("Select Cluster:", style={"fontWeight": "bold"}),
        dcc.Dropdown(
            id="cluster-dropdown",
            options=[
                {"label": f"Cluster {i}", "value": i}
                for i in sorted(df["cluster"].unique())
            ],
            value=0
        )
    ], style={"width": "30%", "margin": "auto", "padding": "20px"}),

    # KPIs
    html.Div(id="kpi-container"),

    # Cluster Description
    html.Div(id="cluster-description", style={
        "textAlign": "center",
        "marginTop": "20px",
        "fontSize": "18px",
        "fontWeight": "bold"
    }),

    # Graphs
    html.Div([
        dcc.Graph(id="scatter-plot"),
        dcc.Graph(id="bar-chart"),
        dcc.Graph(id="cluster-comparison")
    ])
])

# Callback
@app.callback(
    Output("scatter-plot", "figure"),
    Output("bar-chart", "figure"),
    Output("cluster-comparison", "figure"),
    Output("kpi-container", "children"),
    Output("cluster-description", "children"),
    Input("cluster-dropdown", "value")
)
def update_dashboard(selected_cluster):

    filtered_df = df[df["cluster"] == selected_cluster]

    # 🔹 Scatter Plot (Engagement vs Performance)
    scatter_fig = px.scatter(
        filtered_df,
        x="total_clicks",
        y="avg_assessment_score",
        title="Engagement vs Performance",
        color="cluster",
        color_continuous_scale="viridis"
    )

    # 🔹 Bar Chart (Key Features)
    bar_data = filtered_df[features].mean().reset_index()
    bar_data.columns = ["feature", "value"]

    bar_fig = px.bar(
        bar_data,
        x="feature",
        y="value",
        title="Key Metrics (Selected Cluster)"
    )

    # 🔹 Cluster Comparison (All clusters)
    cluster_means = df.groupby("cluster")[features].mean().reset_index()

    comparison_fig = px.bar(
        cluster_means,
        x="cluster",
        y=features,
        barmode="group",
        title="Cluster Comparison Overview"
    )

    # 🔹 KPIs
    kpis = html.Div([
        html.Div([
            html.H3("Students"),
            html.P(len(filtered_df))
        ], style={"padding": "10px", "border": "1px solid #ddd", "borderRadius": "8px"}),

        html.Div([
            html.H3("Avg Score"),
            html.P(round(filtered_df["avg_assessment_score"].mean(), 2))
        ], style={"padding": "10px", "border": "1px solid #ddd", "borderRadius": "8px"}),

        html.Div([
            html.H3("Avg Clicks"),
            html.P(round(filtered_df["total_clicks"].mean(), 2))
        ], style={"padding": "10px", "border": "1px solid #ddd", "borderRadius": "8px"})
        
    ], style={"display": "flex", "justifyContent": "space-around", "marginTop": "20px"})

    # 🔹 Cluster Description
    if selected_cluster == 0:
        description = "🔵 Cluster 0: High Engagement & High Performance Students"
    else:
        description = "🔴 Cluster 1: Low Engagement & At-Risk Students"

    return scatter_fig, bar_fig, comparison_fig, kpis, description


# Run server
if __name__ == "__main__":
    app.run(debug=True)