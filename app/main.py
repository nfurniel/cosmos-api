import json
import random
import os
from typing import Optional, List
from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="CosmosAPI",
    description="A high-performance API for astronomy facts.",
    version="1.0.0"
)

# Helper to load facts
def load_facts():
    file_path = os.path.join("data", "cosmos_facts.json")
    with open(file_path, "r") as f:
        return json.load(f)

@app.get("/")
def read_root():
    return {"message": "Welcome to CosmosAPI! Visit /docs for documentation."}

@app.get("/api/v1/facts")
def get_all_facts():
    """Get all available facts."""
    return load_facts()

@app.get("/api/v1/random")
def get_random_fact():
    """Get a single random fact."""
    facts = load_facts()
    if not facts:
        raise HTTPException(status_code=404, detail="No facts found")
    return random.choice(facts)

@app.get("/api/v1/category/{category_name}")
def get_facts_by_category(category_name: str):
    """Filter facts by category (e.g., 'planets', 'stars')."""
    facts = load_facts()
    filtered_facts = [f for f in facts if f["category"].lower() == category_name.lower()]
    
    if not filtered_facts:
        raise HTTPException(status_code=404, detail=f"No facts found for category: {category_name}")
    
    return filtered_facts