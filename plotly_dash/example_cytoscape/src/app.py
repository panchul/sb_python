import dash
import dash_cytoscape as cyto
import dash_html_components as html
from dash.dependencies import Input, Output

# Sample hierarchical data (like a file structure)
tree_data = {
    "nodes": [
        {"data": {"id": "root", "label": "Root", "type": "folder"}},
        {"data": {"id": "folder1", "label": "Folder 1", "type": "folder"}},
        {"data": {"id": "folder2", "label": "Folder 2", "type": "folder"}},
        {"data": {"id": "file1", "label": "File 1", "type": "file"}},
        {"data": {"id": "file2", "label": "File 2", "type": "file"}},
        {"data": {"id": "file3", "label": "File 3", "type": "file"}},
        {"data": {"id": "folder3", "label": "Folder 3", "type": "folder"}},
        {"data": {"id": "file4", "label": "File 4", "type": "file"}}
    ],
    "edges": [
        {"data": {"source": "root", "target": "folder1"}},
        {"data": {"source": "root", "target": "folder2"}},
        {"data": {"source": "folder1", "target": "file1"}},
        {"data": {"source": "folder1", "target": "file2"}},
        {"data": {"source": "folder2", "target": "file3"}},
        {"data": {"source": "root", "target": "folder3"}},
        {"data": {"source": "folder3", "target": "file4"}},
    ]
}

# Create the Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Foldable Tree Structure"),
    
    # Tree visualization using Cytoscape
    cyto.Cytoscape(
        id="cytoscape",
        elements=tree_data['nodes'] + tree_data['edges'],
        layout={'name': 'breadthfirst', 'roots': '#root'},
        style={'width': '100%', 'height': '600px'},
        stylesheet=[
            {
                'selector': 'node',
                'style': {
                    'label': 'data(label)',
                    'background-color': '#00aaff',
                    'color': 'white',
                    'width': '30px',
                    'height': '30px',
                    'text-valign': 'center',
                    'text-halign': 'center'
                }
            },
            {
                'selector': 'edge',
                'style': {
                    'width': 2,
                    'line-color': '#ccc',
                    'target-arrow-color': '#ccc',
                    'target-arrow-shape': 'triangle'
                }
            },
            {
                'selector': '.folder',
                'style': {
                    'background-color': '#ff6600',
                    'shape': 'ellipse'
                }
            },
            {
                'selector': '.file',
                'style': {
                    'background-color': '#00cc00',
                    'shape': 'rectangle'
                }
            }
        ]
    ),
    
    # Hidden div to store expanded/collapsed nodes
    html.Div(id='expanded-nodes', style={'display': 'none'})
])

# Callback to handle node expand/collapse
@app.callback(
    Output('cytoscape', 'elements'),
    [Input('cytoscape', 'tapNode')],
    [dash.dependencies.State('cytoscape', 'elements'),
     dash.dependencies.State('expanded-nodes', 'children')]
)
def update_tree_on_node_click(node_data, current_elements, expanded_nodes):
    if node_data is None:
        return current_elements

    node_id = node_data['data']['id']
    new_elements = current_elements[:]
    current_expanded_nodes = set(expanded_nodes.split(',')) if expanded_nodes else set()

    # Handle expand/collapse logic
    if node_id not in current_expanded_nodes:
        # Expanding node - show its children
        children = [edge for edge in tree_data['edges'] if edge['data']['source'] == node_id]
        for edge in children:
            target = edge['data']['target']
            # Add child node if it exists in the initial data and is not already in the elements list
            if not any(elem['data']['id'] == target for elem in new_elements):
                new_elements.append({
                    "data": {"id": target, "label": target, "type": "folder" if target.startswith("folder") else "file"}
                })
        current_expanded_nodes.add(node_id)
    else:
        # Collapsing node - hide its children
        children = [edge for edge in tree_data['edges'] if edge['data']['source'] == node_id]
        child_ids = [edge['data']['target'] for edge in children]
        new_elements = [elem for elem in new_elements if elem['data']['id'] not in child_ids]
        current_expanded_nodes.remove(node_id)

    # Update the hidden div storing the expanded nodes state
    return new_elements, ','.join(current_expanded_nodes)

if __name__ == '__main__':
    app.run_server(debug=True)
