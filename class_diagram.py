# Re-import necessary library after execution state reset
from graphviz import Digraph

# Create a new class diagram
class_diagram = Digraph('Class Diagram', filename='class_diagram', format='png')
class_diagram.attr(rankdir='TB', size='10')

# Define classes with attributes
classes = {
    "User": ["+ user_id: int", "+ name: string", "+ email: string", "+ password: string", "+ role: enum(visitor, curator, admin)"],
    "Artist": ["+ artist_id: int", "+ name: string", "+ birth_year: int", "+ death_year: int", "+ nationality: string", "+ biography: string"],
    "Painting": ["+ painting_id: int", "+ title: string", "+ artist_id: int", "+ year: int", "+ medium: string", "+ dimensions: string", "+ image_url: string", "+ description: string", "+ location: string"],
    "Museum": ["+ museum_id: int", "+ name: string", "+ location: string", "+ website: string", "+ contact: string", "+ description: string", "+ latitude: float", "+ longitude: float"],
    "Exhibition": ["+ exhibition_id: int", "+ name: string", "+ start_date: date", "+ end_date: date", "+ museum_id: int", "+ description: string"],
    "ExhibitionPainting": ["+ exhibition_id: int", "+ painting_id: int"],
    "Favorite": ["+ user_id: int", "+ painting_id: int"],
    "Review": ["+ review_id: int", "+ user_id: int", "+ exhibition_id: int", "+ rating: int (1-5)", "+ comment: string", "+ created_at: timestamp"]
}

# Add classes to the diagram
for class_name, attributes in classes.items():
    label = f"{class_name} | " + " \\l ".join(attributes) + " \\l"
    class_diagram.node(class_name, shape="record", label=f"{{ {label} }}")

# Define Relationships
relationships = [
    ("Painting", "Artist", "artist_id"),
    ("Exhibition", "Museum", "museum_id"),
    ("ExhibitionPainting", "Exhibition", "exhibition_id"),
    ("ExhibitionPainting", "Painting", "painting_id"),
    ("Favorite", "User", "user_id"),
    ("Favorite", "Painting", "painting_id"),
    ("Review", "User", "user_id"),
    ("Review", "Exhibition", "exhibition_id")
]

# Add relationships to the diagram
for child, parent, key in relationships:
    class_diagram.edge(parent, child, label=key)

# Save and render the Class Diagram
class_diagram_path = "/Users/benjaminazman/Desktop/python-diagram/class_diagram"
class_diagram.render(class_diagram_path, format='png', cleanup=True)
class_diagram_path