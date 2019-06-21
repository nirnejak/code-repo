Vue.component('greeting', {
	template: `
        <p> Hey there I\'m {{ name }}. <br><br>
            <button v-on:click="changeName()" class="ui button teal">Change Name</button>
        </p>`,
	data: function(){
		return {
			name: 'Jittu'
		}
	},
	methods: {
		changeName: function(){
			this.name = 'Jitendra'
		}
	}
});

var one = new Vue({
	el : "#vue-app-one",
	data : {
		
	},
	methods : {
		
	},
	computed : {
		
	}
});

var two = new Vue({
	el : "#vue-app-two",
	data : {
		
	},
	methods : {

	},
	computed : {

	}
});
