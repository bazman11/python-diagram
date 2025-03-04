# Re-importing the necessary library since the execution state was reset
from graphviz import Digraph

# Create a new directed graph
er = Digraph('ER Diagram', filename='/mnt/data/er_diagram', format='png')
er.attr(rankdir='LR', size='10')

# Define Entities (Tables)
entities = {
    "Users": ["user_id (PK)", "name", "email", "password", "role"],
    "Artists": ["artist_id (PK)", "name", "birth_year", "death_year", "nationality", "biography"],
    "Paintings": ["painting_id (PK)", "title", "artist_id (FK)", "year", "medium", "dimensions", "image_url", "description", "location"],
    "Museums": ["museum_id (PK)", "name", "location", "website", "contact", "description", "latitude", "longitude"],
    "Exhibitions": ["exhibition_id (PK)", "name", "start_date", "end_date", "museum_id (FK)", "description"],
    "Exhibition_Paintings": ["exhibition_id (FK, PK)", "painting_id (FK, PK)"],
    "Favorites": ["user_id (FK, PK)", "painting_id (FK, PK)"],
    "Reviews": ["review_id (PK)", "user_id (FK)", "exhibition_id (FK)", "rating", "comment", "created_at"]
}

# Add entities to the diagram
for entity, attributes in entities.items():
    label = f"{entity} | " + " \\l ".join(attributes) + " \\l"
    er.node(entity, shape="record", label=f"{{ {label} }}")

# Define Relationships (Foreign Keys)
relationships = [
    ("Paintings", "Artists", "artist_id"),
    ("Exhibitions", "Museums", "museum_id"),
    ("Exhibition_Paintings", "Exhibitions", "exhibition_id"),
    ("Exhibition_Paintings", "Paintings", "painting_id"),
    ("Favorites", "Users", "user_id"),
    ("Favorites", "Paintings", "painting_id"),
    ("Reviews", "Users", "user_id"),
    ("Reviews", "Exhibitions", "exhibition_id")
]

# Add relationships to the diagram
for child, parent, key in relationships:
    er.edge(parent, child, label=key)

# Save and render the ER diagram
er_path = "/Users/benjaminazman/Desktop/python-diagram/er_diagram"
er.render(er_path, format='png', cleanup=True)
er_path
