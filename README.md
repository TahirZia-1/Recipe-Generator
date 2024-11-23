# Recipe-Generator
User enters ingredients (comma-separated) to get recipes. Uses spoonacular API. You can get API key from https://spoonacular.com/food-api.

1. After building the Flask based Recipe Generator and Installing Docker Desktop, The command to create image is:
docker build -t recipe_generator .
where recipe_generator is name of the folder.

2. After creating image you will run it on any port you like:
docker run -p 5000:5000 recipe_generator
It will give you an IP to run it on any browser.

3. You can check the process using Docker Desktop app or these commands:
docker ps -a
docker ps
The ps -a command gives list of all the containers, the ps gives all the containers that are running.

4. You can also delete containers using this command:
docker rm <container name or id>


