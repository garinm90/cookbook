import axios from 'axios'

export default {
    async getRecipes(){
        let res = await axios.get("http://localhost:8080/recipes")
        return res.data;
    },
    async getRecipeSingle(recipeId){
        let res = await axios.get("http://localhost:8080/recipe/" + recipeId)
        return res.data;
    }
}