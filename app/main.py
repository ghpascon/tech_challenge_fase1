from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

import os
import importlib
from pathlib import Path
readme_path = Path(__file__).parent.parent / "README.md"
readme_content = readme_path.read_text(encoding="utf-8")

app = FastAPI(
    title="TECH CHALLENGE FASE1",
    description=readme_content,
    version="1.0.0",
    terms_of_service="https://meusite.com/termos",
    contact={
        "name": "Gabriel Henrique Pascon",
        "url": "https://github.com/ghpascon",
        "email": "gh.pascon@gmail.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    }
)

def include_all_routes(current_path):
    routes_path = os.path.join(os.path.dirname(__file__), current_path)

    for filename in os.listdir(routes_path):
        if not filename == "__pycache__" and not "." in filename:
            include_all_routes(current_path + '/' + filename)
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = filename[:-3]
            file_path = os.path.join(routes_path, filename)

            spec = importlib.util.spec_from_file_location(f"app.routes.{module_name}", file_path)
            module = importlib.util.module_from_spec(spec)
            try:
                spec.loader.exec_module(module)
                if hasattr(module, "router"):
                    app.include_router(module.router)
                    print(f"✅ Rota incluída: {module_name}")
                else:
                    print(f"⚠️  Arquivo {filename} não contém um 'router'")
            except Exception as e:
                print(f"❌ Erro ao importar {filename}: {e}")

include_all_routes("routes")


@app.get("/", include_in_schema=False)
def home():
    return RedirectResponse(url="/docs")



# python -m app.database.init_db
# uvicorn app.main:app --reload
# uvicorn app.main:app --host 0.0.0.0 --port $PORT
