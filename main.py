import streamlit as st
import pandas as pd

st.set_page_config(page_title="Interactive Dashboard", layout="wide")
st.title("📊 Interactive Dashboard")
st.caption("This demo shows a simple Python dashboard with filters and charts.")
print("liron")
# Sample data
sales_data = pd.DataFrame(
    [
        {"Product": "Laptop", "Region": "North", "Sales": 320, "Profit": 80},
        {"Product": "Phone", "Region": "North", "Sales": 250, "Profit": 70},
        {"Product": "Tablet", "Region": "South", "Sales": 180, "Profit": 45},
        {"Product": "Laptop", "Region": "South", "Sales": 410, "Profit": 95},
        {"Product": "Phone", "Region": "East", "Sales": 290, "Profit": 60},
        {"Product": "Tablet", "Region": "East", "Sales": 220, "Profit": 50},
        {"Product": "Laptop", "Region": "West", "Sales": 360, "Profit": 88},
        {"Product": "Phone", "Region": "West", "Sales": 300, "Profit": 72},
    ]
)

# Sidebar filters
st.sidebar.header("Filters")
selected_regions = st.sidebar.multiselect(
    "Select regions",
    options=sorted(sales_data["Region"].unique()),
    default=sorted(sales_data["Region"].unique()),
)
minimum_sales = st.sidebar.slider("Minimum Sales", 0, 500, 150, 10)

filtered_data = sales_data[
    sales_data["Region"].isin(selected_regions) & (sales_data["Sales"] >= minimum_sales)
]

if filtered_data.empty:
    st.warning("No rows match the selected filters.")
    st.stop()

# Summary metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${filtered_data['Sales'].sum():,.0f}")
col2.metric("Total Profit", f"${filtered_data['Profit'].sum():,.0f}")
col3.metric("Average Margin", f"{(filtered_data['Profit'].sum() / filtered_data['Sales'].sum() * 100):.1f}%")

# Charts
st.subheader("Sales by Product")
product_summary = filtered_data.groupby("Product", as_index=False).agg({"Sales": "sum", "Profit": "sum"})
st.bar_chart(product_summary.set_index("Product"))

st.subheader("Profit vs Sales")
st.scatter_chart(filtered_data, x="Sales", y="Profit", color="Region")

st.subheader("Filtered Data")
st.dataframe(filtered_data, use_container_width=True)
