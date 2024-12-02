import dash_ag_grid as dag
from dash import Dash, html, dcc
import os

app = Dash()

rowData = [
    {
        "orgHierarchy": ["Erica Rogers"],
        "jobTitle": "CEO",
        "employmentType": "Permanent",
    },
    {
        "orgHierarchy": ["Erica Rogers", "Malcolm Barrett"],
        "jobTitle": "Exec. Vice President",
        "employmentType": "Permanent",
    },
    {
        "orgHierarchy": ["Erica Rogers", "Malcolm Barrett", "Esther Baker"],
        "jobTitle": "Director of Operations",
        "employmentType": "Permanent",
    },
    {
        "orgHierarchy": [
            "Erica Rogers",
            "Malcolm Barrett",
            "Esther Baker",
            "Brittany Hanson",
        ],
        "jobTitle": "Fleet Coordinator",
        "employmentType": "Permanent",
    },
    {
        "orgHierarchy": [
            "Erica Rogers",
            "Malcolm Barrett",
            "Esther Baker",
            "Brittany Hanson",
            "Leah Flowers",
        ],
        "jobTitle": "Parts Technician",
        "employmentType": "Contract",
    },
    {
        "orgHierarchy": [
            "Erica Rogers",
            "Malcolm Barrett",
            "Esther Baker",
            "Brittany Hanson",
            "Tammy Sutton",
        ],
        "jobTitle": "Service Technician",
        "employmentType": "Contract",
    },
    {
        "orgHierarchy": [
            "Erica Rogers",
            "Malcolm Barrett",
            "Esther Baker",
            "Derek Paul",
        ],
        "jobTitle": "Inventory Control",
        "employmentType": "Permanent",
    },
    {
        "orgHierarchy": ["Erica Rogers", "Malcolm Barrett", "Francis Strickland"],
        "jobTitle": "VP Sales",
        "employmentType": "Permanent",
    },
    {
        "orgHierarchy": [
            "Erica Rogers",
            "Malcolm Barrett",
            "Francis Strickland",
            "Morris Hanson",
        ],
        "jobTitle": "Sales Manager",
        "employmentType": "Permanent",
    },
    {
        "orgHierarchy": [
            "Erica Rogers",
            "Malcolm Barrett",
            "Francis Strickland",
            "Todd Tyler",
        ],
        "jobTitle": "Sales Executive",
        "employmentType": "Contract",
    },
    {
        "orgHierarchy": [
            "Erica Rogers",
            "Malcolm Barrett",
            "Francis Strickland",
            "Bennie Wise",
        ],
        "jobTitle": "Sales Executive",
        "employmentType": "Contract",
    },
    {
        "orgHierarchy": [
            "Erica Rogers",
            "Malcolm Barrett",
            "Francis Strickland",
            "Joel Cooper",
        ],
        "jobTitle": "Sales Executive",
        "employmentType": "Permanent",
    },
]

grid = html.Div(
    [
        dag.AgGrid(
            id="tree-data-example",
            columnDefs=[
                # we're using the auto group column by default!
                {"field": "jobTitle"},
                {"field": "employmentType"},
            ],
            defaultColDef={
                "flex": 1,
            },
            dashGridOptions={
                "autoGroupColumnDef": {
                    "headerName": "Organisation Hierarchy",
                    "minWidth": 300,
                    "cellRendererParams": {
                        "suppressCount": True,
                    },
                },
                "groupDefaultExpanded": -1,
                "getDataPath": {"function": "getDataPath(params)"},
                "treeData": True,
                "animateRows": False,
            },
            rowData=rowData,
            enableEnterpriseModules=True,
            licenseKey = os.environ['AGGRID_ENTERPRISE'],
        ),
    ]
)

app.layout = html.Div(
    [
        dcc.Markdown("Example: Organisational Hierarchy using Tree Data "),
        grid,
    ]
)


if __name__ == "__main__":
    app.run(debug=True)
