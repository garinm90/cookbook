<template>
  
</template>

<script>
import RecipeService from '@/services/RecipeService.js'
export default {
    name: 'RecipeList',
    data(){
        return{
            recipes: {}
        }
    },
    created:{
        this.getRecipesData();
    },
    methods: {
        async getRecipesData(){
            RecipeService.getRecipes()
            .then(
                (event => {
                    this.$set(this, "recipes", recipes);
            }).bind(this)
            );
        }
    }

}
</script>

<style>

</style>