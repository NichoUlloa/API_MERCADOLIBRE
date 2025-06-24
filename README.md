# MercadoLibre Recommender

Simple full stack demo using FastAPI backend and Vite frontend.

## Backend

```bash
uvicorn app.api:app --reload --app-dir backend/app
```

## Frontend

```bash
npm install --prefix frontend
npm run dev --prefix frontend
```

CI runs pytest and eslint. Deployment builds the frontend and publishes the `frontend/dist` folder to GitHub Pages.
