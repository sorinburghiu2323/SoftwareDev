<template>
    <div class="potato-form">
        <div>
            <p> Potato name? You have written: {{potatoName}} </p> 
            <input type="text" v-model="potatoName" name="potato-name" />
        </div>

        <div>
            <p> Is it sweet? You have selected: {{isSweet}}</p>
            <input type="radio" id="sweet" name="sweetness" :value="true" v-model="isSweet">
            <label for="sweetness">Sweet</label><br>
            <input type="radio" id="not-sweet" name="sweetness" :value="false" v-model="isSweet">
            <label for="not-sweet">Not Sweet</label><br>
        </div>

        <div>
            <p> Potato quantity? You have written: {{potatoQuantity}} </p> 
            <input type="number" v-model="potatoQuantity" name="potato-quantity" />
        </div>

        <p :class="{errorMessage : failure, successMessage: !failure}"> {{message}} </p>

        <div>
            <button @click="submitForm()"> Add potato uwu </button>
        </div>

    </div>
</template>
<script>
import axios from 'axios';
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
export default {
    name: 'AddPotatoForm',
    data() {
        return {
            potatoName: null,
            isSweet: null,
            potatoQuantity: null,
            //message: '',
            failure: null,
        }
    },
    computed: {
        message() {
            if(this.failure === true) {
                return 'Failed to create potato'
            }
            else if(this.failure === false){
                return 'Successfully added your potato';
            }
            return '';
        },
    },
    methods: {
        submitForm(){
            axios.post('api/potato', {
                potatoes: [
                    {
                        name: this.potatoName,
                        is_sweet: this.isSweet,
                        quantity: this.potatoQuantity
                    }
                ]
            }).then(response => {
                console.log(response);
                // Update potato list
                this.$root.$emit('updatePotatos');

                // Clear inputs
                this.potatoName = null;
                this.isSweet = null;
                this.potatoQuantity = null;

                // Update message
                this.failure = false;
                //this.message = 'Successfully added your potato'
            }).catch(error => {
                console.log(error);

                // Update message
                this.failure = true;
                //this.message = 'Failed to create potato - ' + error.response.data;
            })
        }
    }
}
</script>

<style scoped>
.potato-form{
    display:flex;
    flex-direction: column;
    background: #41b883;
    border-radius: 8px;
    text-align: left;
    padding: 20px;
    color: black;
}

.potato-form input {
    border-radius: 5px;
    border: solid 1px black;
}

.errorMessage {
    color: red;
}

.successMessage{
    color: green;
}

</style>