<template>
    <div>
        <h1> Welcome {{firstName}} {{lastName}}</h1>
        <h2 id="potato-title"> Your potato list </h2>

        <div class="potato-list" v-if="homepagePotatos">
            <ul>
                <li v-for="(potato, index) in homepagePotatos" :key="index">{{potato.name}}</li>
            </ul>
        </div>
        <div class="potato-form-section">
            <button @click="openPotatoForm()">Click to begin adding some potatos!</button>
            <AddPotatoForm v-if="showPotatoForm" />
        </div>
    </div>
</template>
<script>
import AddPotatoForm from '../components/AddPotatoForm.vue'
export default {
    name: 'HomePage',
    components: {
        AddPotatoForm,
    },
    data () {
        return {
            firstName: 'Hia',
            lastName: 'Al Dalaty',
            showPotatoForm: false,
        }
    },
    props: {
        homepagePotatos: Array,
    },
    methods: {
        openPotatoForm() {
            this.showPotatoForm = true;
        }
    }
    
}
</script>
<style scoped>
#potato-title {
    font-size: 20px;
    text-align: left;
}
.potato-list {
    text-align: left;
}
</style>