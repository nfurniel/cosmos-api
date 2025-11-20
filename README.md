# 🪐 CosmosAPI

![Python](https://img.shields.io/badge/python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![License](https://img.shields.io/github/license/tu-usuario/cosmos-api?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Live_🟢-success?style=for-the-badge)

> **The open-source, high-performance REST API for astronomy enthusiasts, educators, and space-bots.** 🚀

**CosmosAPI** provides curated, scientifically accurate facts about the universe (planets, stars, black holes, and more). Built with **FastAPI** for blazing speed and simplicity.

---

##  Live Demo & Documentation

The API is deployed and ready to use! You can test all endpoints directly in your browser via the interactive Swagger UI:

 **[Click here to try the API (Live Docs)](https://cosmos-api-production.onrender.com/docs)**

---

##  Features

* 🌌 **Vast Database:** Facts about planets, stars, nebulae, and space history.
* 🚀 **Blazing Fast:** Built on top of Starlette and Pydantic.
* 📖 **Self-Documented:** Automatic interactive documentation.
* 🔍 **Smart Filtering:** Filter facts by specific categories.
* 🆓 **Free & Open Source:** No API keys required (yet).

---

##  API Endpoints

Base URL: https://cosmos-api-production.onrender.com

| Method | Endpoint | Description | Example Usage |
| :--- | :--- | :--- | :--- |
| `GET` | **/api/v1/random** | Returns a single random fact. | `curl /api/v1/random` |
| `GET` | **/api/v1/facts** | Returns the full list of facts. | `curl /api/v1/facts` |
| `GET` | **/api/v1/category/{name}** | Filter facts by category. | `curl /api/v1/category/planets` |
| `GET` | **/docs** | Interactive Swagger UI. | Visit in browser |

### Example Response (`/api/v1/random`)

```json
{
  "id": "fact_001",
  "content": "Neutron stars are so dense that a teaspoon of them would weigh about 6 billion tons.",
  "category": "stars",
  "complexity": "medium",
  "source": "National Geographic"
}
```

## 📂 Project Structure

```bash
cosmos-api/
├── app/
│   ├── main.py           # The API entry point & logic
│   └── __init__.py
├── data/
│   └── cosmos_facts.json # The database of facts
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

<p align="center">
  If you find this API useful, please <strong>give it a star</strong> ⭐ on GitHub!
  <br>
  Built with ❤️ and 🔭 by <a href="https://github.com/nfurniel">Furni</a>
</p>
