# Recipe Generator

A simple Flask-based web application that allows users to input ingredients (comma-separated) and get recipes. This app uses the [Spoonacular API](https://spoonacular.com/food-api) to fetch recipes.

---

## Features
- Input ingredients and receive recipe suggestions.
- Simple UI with Flask templates.
- Easy to deploy using Docker.

---

## Prerequisites

1. **Spoonacular API Key**: Get your API key from [Spoonacular](https://spoonacular.com/food-api).
2. **Python**: Ensure Python 3.7+ is installed.
3. **Docker**: Install [Docker Desktop](https://www.docker.com/).

---

## Some Commands

### Create Image
```bash
docker build -t recipe_generator .
```

### Run the Image
```bash
docker run -p 5000:5000 recipe_generator
```

### Check Containers
```bash
docker ps -a
docker ps
```

